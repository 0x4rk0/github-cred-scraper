# Organization Cred Scraper

## Requirements

```python
pip3 install -r requirements.txt
```

### This will scrape an entire organization's content on github for plain text creds, API keys, SSH keys, etc

### Example

```
python3 cred_scan.py
```

This will append results into

```
ORG_results.txt
```

Not sure what an "Org" is? Search using the github search bar for "org:foo"

From here, you can grep through the results

Big thanks to @metacortex for the help on the Python!
