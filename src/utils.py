from dotenv import load_dotenv
import requests
import xml.etree.ElementTree as ET
from os import environ
import pandas as pd
import json

load_dotenv()

def get_prefix_as_dict(doi):
    prefix = {}
    prefix['prefix'] = doi.split('/')[0]
    return prefix

def write_to_xml(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def get_publisher(doi, filename):
    endpoint = 'http://doi.crossref.org/getPrefixPublisher/'
    prefix = get_prefix_as_dict(doi)
    header = {}
    header['email'] = environ.get('MY_EMAIL')
    header['user'] = environ.get('USER')

    response = requests.get(endpoint, params=prefix, headers=header)

    if response.status_code == 200:
        write_to_xml(filename, response.text)
        tree = ET.parse(filename)
        root = tree.getroot()
        return root.find('./publisher/publisher_name').text

    else:
        print(f'Unable to get publisher. Received response status {response.status_code}')

def get_all_publishers():
    endpoint = 'http://doi.crossref.org/getPrefixPublisher/'
    header = {}
    header['email'] = environ.get('MY_EMAIL')
    header['user'] = environ.get('USER')

    response = requests.get(endpoint, params={'prefix': 'all'}, headers=header)

    with open('publisher_names.json', 'w') as f:
        json.dump(response.json(), f, indent=4)

def tidy_csv(filename):
    data = pd.read_csv(filename)
    doi_df = pd.DataFrame(data=data)
    doi_df = doi_df.dropna(axis=0)
    doi_df.to_csv(filename)

get_all_publishers()

