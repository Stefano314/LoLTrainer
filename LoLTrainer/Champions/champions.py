import numpy as np

from .ChampionsInfo.attributes import get_attributes, clear_cache
from LoLTrainer.Trainer.processing import item_recognizer
from LoLTrainer.Items.items import get_items, LoLItems

class LoLChampions:

    '''
    Description
    -----------
    League of Legends champions class.
    This will initialize all champions in the game, giving them their base attributes.
    Once the champion is created, its stats will change according to the level and to the items equipped.

    '''

    def __init__(self,  name : str):

        # PRIVATE
        self._off_attributes = get_attributes(filename = 'offensive_attributes', key = name)
        self._def_attributes = get_attributes(filename = 'defensive_attributes', key = name)
        self._abi_attributes = get_attributes(filename = 'abilities_attributes', key = name)
        self._generalities = get_attributes(filename = 'generalities', key = name)

        # Items hold, it's here because of its function. To check items we have the property.
        self._items = []

        # PUBLIC:

        # Generic stats
        self.name = name
        self.lvl = 1
        self.HP = self._def_attributes['HP']
        self.AP = self._off_attributes['AP']
        self.AD = self._off_attributes['AD']
        self.Ph_armor = self._def_attributes['physical_armor']
        self.Ma_armor = self._def_attributes['magical_armor']
        self.mana = self._def_attributes['mana']

        # Additional stats
        self.lethality = 0
        self.armor_penetration = 0
        self.omnivamp = 0
        self.life_steal = 0
        self.gold = 0


    @property
    def stats(self):
        """
        Description
        -----------
        Get all current stats values of the champion.

        Return
        ------
        list : Champion stats list.

        """

        stats = [self.lvl, self.HP, self.AP, self.AD, self.Ph_armor, self.Ma_armor, self.mana,
                 self.lethality, self.armor_penetration, self.omnivamp, self.life_steal, self.gold]

        return stats


    @property
    def items(self):
        """
        Description
        -----------
        Get all the current items hold by the champion.

        Return
        ------
        list : Items hold list.

        """

        items = self._items
        if isinstance(items, list):
            return [i.name for i in items]



    def level_up(self, lvl : int = 0) -> None:
        """
        Description
        -----------
        Level up or select the level of the champion. The base stats will change accordingly.

        Parameters
        ----------
        lvl : int, optional
            Sets the level of the champion.

        """
        if lvl == 0:
            self.lvl += 1
        else:
            self.lvl = lvl

        # For now missing regens scaling
        self.HP = self._def_attributes['HP'] + self._def_attributes['HP_growth'] * \
                  (self.lvl - 1) * (0.7025 + 0.0175 * (self.lvl - 1))

        self.AD = self._off_attributes['AD'] + self._off_attributes['AD_growth'] * \
                  (self.lvl - 1) * (0.7025 + 0.0175 * (self.lvl - 1))

        if self.mana is not None:

            self.mana = self._def_attributes['mana'] + self._def_attributes['mana_growth'] * \
                        (self.lvl - 1) * (0.7025 + 0.0175 * (self.lvl - 1))


    def remove_items(self, item : list) -> None:
        """
        Description
        -----------
        Remove a given set of items from the champion inventory.

        """

        if isinstance(item, str):
            item = [item]

        try:
            _items_hold = np.array([i.name for i in self._items])
            names_to_remove = np.array(self._items)[np.where(np.in1d(_items_hold, item))[0]]

            for name in names_to_remove:
                self._items.remove(name)

        except:
            print(f"- WARNING: {item} item(s) not found!")


    def item_upgrade(self, item : list) -> None:
        """
        Description
        -----------
        Extend the items hold by the champion.

        """

        if len(self._items) < 6:
            self._items.extend(get_items(item))
            self.evaluate_stats()
        else:
            print("- WARNING: exceeding maximum number of items hold.")
            pass


    def evaluate_stats(self):
        """
        Description
        -----------
        Calculate and substitute every stat value according to the items hold
        by the champion.

        """

        self.level_up(lvl = self.lvl)

        self.HP += np.sum([item.HP for item in self._items if isinstance(item, LoLItems)])
        self.AP += np.sum([item.AP for item in self._items if isinstance(item, LoLItems)])
        self.AD += np.sum([item.AD for item in self._items if isinstance(item, LoLItems)])
        self.Ph_armor += np.sum([item.Ph_armor for item in self._items if isinstance(item, LoLItems)])
        self.Ma_armor += np.sum([item.Ma_armor for item in self._items if isinstance(item, LoLItems)])

        if self.mana is None:
            pass
        else:
            self.mana += np.sum([item.mana for item in self._items if isinstance(item, LoLItems)])

        self.lethality += np.sum([item.lethality for item in self._items if isinstance(item, LoLItems)])
        self.armor_penetration += np.sum([item.armor_penetration for item in self._items if isinstance(item, LoLItems)])
        self.omnivamp += np.sum([item.omnivamp for item in self._items if isinstance(item, LoLItems)])
        self.life_steal += np.sum([item.life_steal for item in self._items if isinstance(item, LoLItems)])


    def update_champ(self) -> None:
        """
        Description
        -----------
        Re-evaluates all the stats of the champ.

        """

        self.level_up(self.lvl)
        self.item_upgrade(item_recognizer())
        self.evaluate_stats()
