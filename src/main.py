import pandas as pd

def add_publisher_name(filename):
    """Takes a csv file with a column named 'DOI'. It parses the doi prefix and returns a new csv file with additional columns: doi_prefix, publisher_name.

    Args:
        filename - a csv file
    Returns:
        A new csv file with additional columns
        Errors - unable to get publisher
    """
    doi_df = pd.DataFrame(data=pd.read_csv(filename))
    print(doi_df.head())
    doi_df['prefix'] = doi_df['DOI'].str.split('/').str[0]
    print(doi_df.head())

add_publisher_name('dois.csv')