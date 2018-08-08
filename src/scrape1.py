### https://www.skillshare.com/classes/Coding-for-Entrepreneurs-Python-Web-Scraping/1964055571?via=search-layout-grid
import csv
import datetime
import os
import requests
from bs4 import BeautifulSoup
# from stop_words import get_stop_words

from urllib.parse import urlparse
from collections import Counter

def clean_word(word):
        word = word.replace("!", "")
        word = word.replace("?", "")
        word = word.replace(".", "")
        word = word.replace(":", "")
        word = word.replace(";", "")
        word = word.replace("(", "")
        word = word.replace(")", "")
        word = word.replace("--", "")
        return word

def clean_up_words(words):
    new_words = [] # empty list
    # pkg_stop_words = get_stop_words('en')
    my_stop_words = ['the', 'is', 'and']
    for word in words:
        word = word.lower()
        # if word in my_stop_words or word in pkg_stop_words:
        if word in my_stop_words:
            pass
        else:
            cleaned_word = clean_word(word)
            new_words.append(cleaned_word)
    return new_words

def create_csv_path(csv_path):
    if not os.path.exists(csv_path):
        with open(csv_path, 'w') as csvfile: #open that path w = write/create
            header_columns = ['word', 'count', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=header_columns)
            writer.writeheader()

saved_domains = {
    "joincfe.com": "main-container",
    "tim.blog": "content-area"
}

my_url = "http://tim.blog"

print("Grabbing...", my_url)
domain = urlparse(my_url).netloc
response = requests.get(my_url)

if response.status_code != 200:
    print("You can't scrape this", response.status_code)
else: 
    print("Scrapping...")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    body_ = soup.find("div", {"class": "content-area"})
    words = body_.text.split()
    clean_words = clean_up_words(words)
    word_counts = Counter(clean_words)
    print(word_counts.most_common)
    filename = domain.replace(".", "-") + '.csv'
    path = 'csv/' + filename
    timestamp = datetime.datetime.now() # timestamp
    create_csv_path(path)
    with open(path, 'a') as csvfile: #open that path w = write/create
        header_columns = ['word', 'count', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=header_columns)
        for word, count in word_counts.most_common(30):
            writer.writerow({
                "count": count,
                "word": word,
                "timestamp": timestamp
            })

# Next step, learn to scrape structured data
# https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251

# Best source code ever!