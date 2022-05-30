import pandas as pd
import json
import os

__all__ = ['get_attributes', 'clear_cache', 'load_file', 'modify_attributes']

INFO_PATH = os.path.join(os.getcwd(), 'LoLTrainer', 'Champions', 'ChampionsInfo', '')

# Cache global cache variable
_cache = dict()

def clear_cache(key):
    """
    Description
    -----------
    Remove value stored in cache dictionary.

    """

    if key in _cache:
        _cache.pop(key)

def load_file(filename : str) -> pd.DataFrame:
    """
    Description
    -----------
    Half way function to load .csv files if they haven't been loaded already, otherwise recover their cached value.

    Parameters
    ----------
    filename : str
        Specifies what file to load. It must be one of the file names (without extension),
        which are 'offensive_attributes', 'defensive_attributes', 'abilities_attributes' or 'generalities'.

    """

    key = filename
    if key not in _cache:
        if filename != 'abilities_attributes':
            _cache[key] = pd.read_csv(INFO_PATH+filename+'.csv', index_col = 0)

        elif filename == 'abilities_attributes':
            with open(INFO_PATH + filename + '.json') as file:
                _cache[key] = json.load(file)

    return _cache[key]


def get_attributes(filename : str, key : str):
    """
    Description
    -----------
    Load the .csv file according to the value expressed in 'file_category'.
    Then it recovers the information required by the user from that file.

    Parameters
    ----------
    file_name : str
        Specifies the .csv file to load.
    key : str
        Selects the entry in the .csv file, which correspond to a specific champion.

    """

    return load_file(filename)[key]

def modify_attributes(file : pd.DataFrame, filename : str):
    """
    Description
    -----------
    This function

    Parameters
    ----------
    file : pd.DataFrame
        Copy of the pandas DataFrame related to the champion stats that we want to update.
    filename : str
        Name of the file to modify with "file".

    Example
    -------
    >>> to_modify = load_file('offensive_attributes')
    >>> to_modify['Aatrox']['AD'] = 10 # do stuff with the csv
    >>> modify_attributes(a, 'offensive_attributes')
    """

    response = input("\nWARNING: Do you want to apply the changes? [Y/N]   ")
    if response == 'Y' or response == 'y':
        file.to_csv(INFO_PATH+filename+'.csv')
