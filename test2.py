from selectorlib import Extractor
import requests 
import json 
import argparse

argparser = argparse.ArgumentParser()
#argparser.add_argument('url', help='Amazon Product Details URL')

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('amazon.txt')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}

# Download the page using requests
args = argparser.parse_args()
r = requests.get('https://www.amazon.in/Carbon-Sticker-Colors-Adjustable-Muticolor/dp/B07FVHDDWS/ref=sr_1_1?keywords=rubiks+cube&qid=1578848138&sr=8-1', headers=headers)
# Pass the HTML of the page and create 
data = e.extract(r.text)
# Print the data 
print(json.dumps(data, indent=True))