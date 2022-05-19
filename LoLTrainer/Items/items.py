import json
import os

__all__ = ['get_item']

INFO_PATH = os.path.join(os.getcwd(), 'LoLTrainer', 'Champions', 'ChampionsInfo', '')

# Cache global variable for .json
_cache = dict()

def clear_cache(key):
    """
    Description
    -----------
    Remove value stored in cache dictionary.

    """

    if key in _cache:
        _cache.pop(key)

def load_file(file_category : str):
    """
    Description
    -----------
    Half way function to load .json files if they haven't been loaded already, otherwise recover their cached value.

    Parameters
    ----------
    file_category : str
        Specifies what file to load. It must be one of the file names (without extension),
        which are 'offensive_attributes', 'defensive_attributes', 'abilities_attributes' or 'generalities'.

    """

    key = file_category
    if key not in _cache:
        with open(INFO_PATH+file_category+'.json') as file:
            _cache[key] = json.load(file)

    return _cache[key]


def get_item(file_category : str, ID : int):
    """
    Description
    -----------
    Load the .json file according to the value expressed in 'file_category'.
    Then it recovers the information required by the user from that file.

    Parameters
    ----------
    file_category : str
        Specifies the .json file to load.
    ID : int
        Selects the entry in the .json file, which correspond to a specific champion.

    """

    champ_info = load_file(file_category)[ID]

    return champ_info
