from dotenv import load_dotenv
import requests
import xml.etree.ElementTree as ET
from os import environ

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



get_publisher('10.1037/a0040251', 'test-data.xml')

