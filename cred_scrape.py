import json
import os
import requests
import sys

organization = input("Enter the name of the organization: ")
repo_urls = []

response = requests.get('https://api.github.com/orgs/%s/repos' % organization)
repos = json.loads(response.content.decode('utf-8'))

for repo in repos:
    repo_urls.append(repo['html_url'])

for url in set(repo_urls):
    print('[+] Hitting: %s' % url)
    os.popen('trufflehog --regex --entropy=False %s >> %s_results.txt' %(url, organization))
