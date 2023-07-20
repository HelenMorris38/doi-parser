import pandas as pd
from os import path
from src.utils import get_all_publishers, create_publisher_dict, get_data_cite_publisher
import json

def add_publisher_name(filename):
    """Takes a filepath to a csv file. The file must have a column named 'DOI'. It parses the doi prefix and updates the csv file with additional columns: doi_prefix, publisher_name.

    Args:
        filename - path to csv file
    Returns:
        Errors - unable to get publisher
    """
    doi_df = pd.DataFrame(data=pd.read_csv(filename))
    print(doi_df.head())
    doi_df['prefix'] = doi_df['DOI'].str.split('/').str[0]
    print(doi_df.head())
    
    if not path.isfile('publisher_names.json'):
        get_all_publishers()
    
    with open('publisher_names.json') as f:
        publisher_names = json.load(f)
    
    publisher_dict = create_publisher_dict(publisher_names)

    doi_df['publisher_name'] = doi_df['prefix'].map(publisher_dict)

    print(doi_df.head())
    missing_publisher_names_df = doi_df[doi_df['publisher_name'].isna()]
    print(pd.unique(missing_publisher_names_df['prefix']).tolist())
    missing_publisher_names_df = missing_publisher_names_df.drop_duplicates(subset=['prefix'])
    print(missing_publisher_names_df)
    
    if len(missing_publisher_names_df.index) > 0:
        data_cite_pubs_dict = {}
        for doi in missing_publisher_names_df['DOI']:
            data_cite_pub = get_data_cite_publisher(doi)
            data_cite_pubs_dict[data_cite_pub[0]] = data_cite_pub[1]
        print(data_cite_pubs_dict)



add_publisher_name('dois.csv')