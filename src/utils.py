import requests
import xml.etree.ElementTree as ET

def get_prefix(doi):
    return doi.split('/')[0]

def write_to_xml(filename, data):
    with open(filename, 'w') as f:
        f.write(data)


def get_publisher(doi, filename):
    endpoint = 'http://doi.crossref.org/getPrefixPublisher/'
    prefix = get_prefix(doi)
    response = requests.get(endpoint, params=prefix)
    write_to_xml(filename, response.text)



get_publisher('10.1037/a0040251', 'test-data.xml')

