import json
import os
import requests
import sys

organization = input("Enter the name of the organization: ")
repo_urls = []

try:
    response = requests.get('https://api.github.com/orgs/%s/repos' % organization)
    response.raise_for_status()
    repos = json.loads(response.content.decode('utf-8'))
except requests.exceptions.HTTPError as e:
    print("Error:", e)
    sys.exit(1)
except ValueError as e:
    print("Error: Invalid JSON response.")
    sys.exit(1)

for repo in repos:
    repo_urls.append(repo['html_url'])

for url in set(repo_urls):
    print('[+] Hitting: %s' % url)
    os.popen('trufflehog --regex --entropy=False %s >> %s_results.txt' %(url, organization))
