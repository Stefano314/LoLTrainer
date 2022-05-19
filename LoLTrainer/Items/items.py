import json
import os

__all__ = ['get_item']

INFO_PATH = os.path.join(os.getcwd(), 'LoLTrainer', 'Items', '')

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

def load_item(filename : str ='items'):
    """
    Description
    -----------
    Half way function to load .json files if they haven't been loaded already, otherwise recover their cached value.
    At the moment the only file available is 'items.json'.

    """

    key = filename
    if key not in _cache:
        with open(INFO_PATH+filename+'.json') as file:
            _cache[key] = json.load(file)

    return _cache[key]


def get_item(keys : list, filename :str = 'items'):
    """
    Description
    -----------
    Load the .json file according to the value expressed in 'file_category'.
    Then it recovers the information required by the user from that file.

    Parameters
    ----------
    keys : int
        Selects the entry in the .json file, which correspond to a specific champion.
    file_name :str
    """

    items = load_item(filename)
    # !! put controls if items exits !!
    if len([keys]) == 1:
        return items.get(keys)
    else:
        return [items.get(key) for key in keys]
