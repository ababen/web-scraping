import csv
import datetime
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import Counter

my_url = "https://www.truecar.com/used-cars-for-sale/listings/lexus/rx-350/price-0-45000/location-westbury-ny/?drivetrain=AWD&mileageHigh=25000"
path = "\\Dev\\alexbaben\\src\\webpage_to_be_scrapped.html"
text = open(path, "r").read()

soup_beauty = BeautifulSoup(text, 'html.parser')