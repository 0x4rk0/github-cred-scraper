import json
import os
import requests
import sys

def get_repos(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return json.loads(response.content.decode('utf-8'))
    except requests.exceptions.HTTPError as e:
        print("Error:", e)
        return None
    except ValueError as e:
        print("Error: Invalid JSON response.")
        return None

if len(sys.argv) != 2:
    print("Usage: python script_name.py <organization_or_username>")
    sys.exit(1)

name = sys.argv[1]
repo_urls = []

# Try organization first
repos = get_repos('https://api.github.com/orgs/%s/repos' % name)
if repos is None:
    # If organization does not exist, try user
    repos = get_repos('https://api.github.com/users/%s/repos' % name)
    if repos is None:
        print("Provided name does not correspond to a valid organization or user.")
        sys.exit(1)

for repo in repos:
    repo_urls.append(repo['html_url'])

for url in set(repo_urls):
    print('[+] Hitting: %s' % url)
    os.popen('trufflehog --regex --entropy=False %s >> %s_results.txt' % (url, name))

