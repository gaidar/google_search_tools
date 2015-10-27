import requests
import os
import string
import re

# Search term
searchfor = "gaidar"

def querygoogle(searchterm):
    link = 'https://www.google.com/complete/search?client=serp&q=' \
     + searchterm
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; ' \
        'Intel Mac OS X 10_8_2) AppleWebKit/537.36 ' \
        ' (KHTML, like Gecko) Chrome/27.0.1453.116 ' \
        'Safari/537.36'}
    response = requests.get(link, headers = ua)
    return response.text


filename = os.path.join(os.path.dirname(__file__), searchfor + '.txt')

for l in string.ascii_lowercase:
    content = querygoogle(searchfor + ' ' + l)
    # clean up
    content = content.replace('\\u003cb', '')
    content = content.replace('\\u003c\\/b', '')
    content = content.replace('\\u003e', '')
    # extract
    contents = re.findall('\"([A-z0-9 ]+)\"', content)
    # write
    file_ = open(filename, 'a+')
    for item in contents:
        if len(item) > (len(searchfor) + 2) and ' ' in item:
            file_.write("%s\n" % item)
    file_.close()
