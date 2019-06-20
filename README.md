# Organization Cred Scraper

## Requirements

```python
pip install truffleHog
```

### This will scrape an entire organization's content on github for plain text creds, API keys, SSH keys, etc

### Example

```
python git_scan.py ORG
```

This will append results into

```
ORG_results.txt
```

From here, you can grep through the results

Big thanks to @metacortex for the help on the Python!
