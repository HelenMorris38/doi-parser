import pandas as pd

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

add_publisher_name('dois.csv')