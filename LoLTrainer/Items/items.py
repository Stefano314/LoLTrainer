import pandas as pd
import os
from PIL import Image
import numpy as np


__all__ = ['LoLItems', 'get_items']

ITEMS_PATH = os.path.join(os.getcwd(), 'LoLTrainer', 'Items', '')
ITEMS_IMAGES_PATH = os.path.join(os.getcwd(), 'Images', 'Items', '')

# Cache global variable for .csv
_cache = dict()


def clear_cache(key):
    """
    Description
    -----------
    Remove value stored in cache dictionary.

    """

    if key in _cache:
        _cache.pop(key)


def _load_items(filename : str = 'items'):
    """
    Description
    -----------
    Half way function to load .csv files if they haven't been
    loaded already, otherwise recover their cached value.
    At the moment the only file available is 'items.csv'.

    """

    key = filename

    if key not in _cache:

        _cache[key] = pd.read_csv(ITEMS_PATH+filename+'.csv', index_col=0)

    return _cache[key]


def _get_item(key : str, filename : str = 'items'):
    """
    Description
    -----------
    Load the items.csv file and recovers the information required by the user from that file.

    Parameters
    ----------
    key : str
        Selects the entry in the items.csv file, which correspond to a single specific item.

    filename :str
        Name of the items.csv file. At the moment there is only 'items.csv'.

    Return
    ------
    pd.DataFrame : The item row that will be used in items class to generate the object.

    """

    items = _load_items(filename)
    return items.loc[items['Item'] == key]


def _link_to_image(key : str) -> str:
    """
    Description
    -----------
    Check if the item name is found inside Images/Items folder.
    If the image exists, then its path is returned.

    Parameters
    ----------
    key : str
        Name of the item.

    Returns
    -------
    str : Path of the image.

    """

    img_name = ''.join((key, '.png'))

    if img_name in os.listdir(ITEMS_IMAGES_PATH):

        return os.path.join(ITEMS_IMAGES_PATH, img_name)

    else:
        print(f"-WARNING: image {img_name} not found!\n")
        return None


def get_items(keys : list):

    """
    Description
    -----------
    Create LoLItems objects according to the names specified in 'keys'.

    Parameters
    ----------
    keys : list
        Objects names.

    Return
    ------
    list : List of LoLItems objects

    """

    if isinstance(keys, str):
        return [LoLItems(name = keys)]

    else:
        return [LoLItems(name = key) for key in keys if key is not None]


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
        self._items_stats = _get_item(filename = 'items', key = name)
        self._image = None

        # PUBLIC:
        self.name = self._items_stats['Item']
        self.gold = self._items_stats['gold']

        self.HP = self._items_stats['HP']
        self.AP = self._items_stats['AP']
        self.AD = self._items_stats['AD']
        self.AS = self._items_stats['AS']
        self.AH = self._items_stats['AH']
        self.mana = self._items_stats['mana']

        self.Ph_armor = self._items_stats['physical_armor']
        self.Ma_armor = self._items_stats['magical_armor']

        self.mana_regen = self._items_stats['mana_regen']
        self.HP_regen = self._items_stats['HP_regen']

        self.crit_chance = self._items_stats['critical_chance']
    
        self.lethality = self._items_stats['lethality']
        self.armor_penetration = self._items_stats['armor_penetration']
        self.magic_penetration = self._items_stats['magic_penetration']

        self.omnivamp = self._items_stats['omnivamp']
        self.life_steal = self._items_stats['life_steal']
        self.hsp = self._items_stats['hsp']

        self.Maps = self._items_stats['Maps']
        # self.bonus = self._items_stats['BONUS']


    def item_image(self, png = False):
        """
        Description
        -----------
        Conversion from PIL.Image object to numpy array.

        """
        image = _link_to_image(key = self.name)

        if png:
            return Image.open(image)

        else:
            self._image = np.asarray(Image.open(image).convert("L"))
            return self._image
