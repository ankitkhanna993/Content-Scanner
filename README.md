# oit-whs-cpcontentscanner
CampusPress ContentMonitor Scanner

#### Python version: 3.7
#### Dependencies: beautifulsoup4
```pip install beautifulsoup4```

#### Execute script: 
```python3 cpcontentscanner.py```

#### Explanation: 
1. Prompt will ask for a site URL to scan. Enter a complete URL like https://blog.uta.edu/xxxx/xxxx
2. The script first validates the URL entered and re-prompts for an input if the URL cannot be reached.
3. After successful validation, the URL is scraped for visible text and stored in a python list.
4. A profanity list is then used to find the difference between the visible web page text and the profanity list to find any common words.
5. The script returns any trigger word/words that are found.

##### NOTE: (For MacOS users)
If one receives an SSL issue while running the script. Kindly, goto Finder > Applications > Python 3.7 > (Double Click) Install Certificates.command
Once the process completes, re-run the script.
