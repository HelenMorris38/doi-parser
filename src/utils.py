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

def get_data_cite_publisher(doi):
    if len(doi) > 3:
        endpoint = f'https://api.datacite.org/dois/{doi}'
    
        response = requests.get(endpoint)
        data_cite_publisher = []
        data_cite_publisher.append(doi.split('/')[0]) 
        try:
            data_cite_publisher.append(response.json()['data']['attributes']['publisher'])
        except:
            data_cite_publisher.append('publisher name not found')

        return data_cite_publisher
    else:
        return ['', 'publisher name not found']

get_data_cite_publisher('10.15122/isbn.978-2-8124-3374-0.p.0469')

def tidy_csv(filename):
    data = pd.read_csv(filename)
    doi_df = pd.DataFrame(data=data)
    doi_df = doi_df.dropna(axis=0)
    doi_df.to_csv(filename)

def create_publisher_dict(data):
    """Transforms publisher names data into a dictionary with key value pairs of prefix and corresponding publisher name. This dict is easier to work with than raw response from api and is used to populate the publisher name column in the csv file.
    Args:
    A list of dictionaries (response from api)
    Returns:
    A dict with key value pairs of prefix and corresponding publisher name
    """
    publisher_dict = {}
    for prefix in data:
        for p in prefix['prefixes']:
            publisher_dict[p] = prefix['name']

    return publisher_dict

