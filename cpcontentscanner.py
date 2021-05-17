# Imports
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import Request, urlopen, URLError


# function to exclude text from listed parent HTML tags
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


# function to scrape all the visible text
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


# function to validate the site URL
def validate_url(prompt):
    while True:
        site_url = input(prompt)
        if site_url == '':
            print("Enter a complete URL to scan")
            continue
        req = Request(site_url)
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
                continue
            elif hasattr(e, 'code'):
                print('The server could not fulfill the request.')
                print('Error code: ', e.code)
                continue

        if response is None:
            print("Check the URL and Try again.")
            continue
        else:
            print("Site URL Validated...")
            break
    return site_url


# user prompt for site URL to scan
site_url = validate_url("Site URL to scan: ")

# reading and extracting text from site's HTML page
html = urlopen(site_url).read()
text_lst = text_from_html(html)
text_lst = text_lst.lower()

# building final visible text list
final_lst = text_lst.split(' ')
final_lst = [i for i in final_lst if i]

# building profanity word list
profanity_text = open("resources/wordlist.txt", "r")
profanity_text = profanity_text.read()
profanity_lst = profanity_text.split(',')

# finding diff./intersection btw visible text list and profanity word list
trigger_wrd = set(final_lst) & set(profanity_lst)
if trigger_wrd is not None:
    print("Trigger word/words on the web page: ")
    print(*trigger_wrd, sep=", ")
else:
    print("No Trigger word found.")
