import json
import os

__all__ = ['LoLItems', 'get_items']

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


def _load_item(filename : str = 'items'):
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


def _get_item(keys : str, filename : str = 'items'):
    """
    Description
    -----------
    Load the .json file according to the value expressed in 'file_category'.
    Then it recovers the information required by the user from that file.

    Parameters
    ----------
    keys : str
        Selects the entry in the .json file, which correspond to a single specific item.
    filename :str
        Name of the .json file. At the moment we only have 'items.json'.

    Return
    ------
    dict : The items dictionary that will be used in items class to generate the object.

    """

    items = _load_item(filename)
    return items.get(keys)


def get_items(keys : list):

    """
    Description
    -----------
    Create LoLItems objects according to the names specified in 'keys'.

    Parameters
    ----------
    keys : list
        Objects names.

    """

    if isinstance(keys, str):
        return LoLItems(name = keys)

    else:
        return [LoLItems(name = key) for key in keys]


class LoLItems:

    '''
    Description
    -----------
    League of Legends items class.
    This class will serve the champion class when evaluating stats after the acquisition of an item.
    Because of that, the structure is actually the same of the champion class, with the addition of few features.

    '''

    def __init__(self, name: str):
        # PRIVATE
        self._items_stats = _get_item(filename = 'items', keys = name)

        # PUBLIC:
        self.name = self._items_stats['name']
        self.gold = self._items_stats['gold']
        self.HP = self._items_stats['HP']
        self.AP = self._items_stats['AP']
        self.AD = self._items_stats['AD']
        self.Ph_armor = self._items_stats['physical_armor']
        self.Ma_armor = self._items_stats['magical_armor']
        self.mana = self._items_stats['mana']
        self.lethality = self._items_stats['lethality']
        self.armor_penetration = self._items_stats['armor_penetration']
        self.omivamp = self._items_stats['omivamp']
        self.life_steal = self._items_stats['life_steal']
        self.bonus = self._items_stats['BONUS']

