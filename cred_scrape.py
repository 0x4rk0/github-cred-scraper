#!/usr/bin/env python

import json
import os
import requests
import sys
repo_urls = []

for i in json.loads(requests.get('https://api.github.com/orgs/%s/repos' % sys.argv[1]).content.decode('utf-8')):
    repo_urls.append(i['html_url'])

for i in set(repo_urls):
    print('[+] Hitting: %s' % i)
    os.popen('trufflehog --regex --entropy=False %s >> %s_results.txt' %(i, sys.argv[1]))
