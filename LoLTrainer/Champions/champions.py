import numpy as np

from .ChampionsInfo.attributes import get_attributes, clear_cache
from LoLTrainer.Trainer.processing import check_items
from LoLTrainer.Items.items import get_items


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
        self.omivamp = 0
        self.life_steal = 0
        self.gold = 0


    @property
    def items(self):
        items = self._items
        if isinstance(items, list):
            return [i.name for i in items]
        else:
            return [items.name]


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

    def update_champ(self) -> None:
        """
        Description
        -----------
        Re-evaluates all the stats of the champ.
        """
        self.level_up(self.lvl)
        self.item_upgrade(check_items())
        self.evaluate_stats()

    def remove_items(self, item : list) -> None:

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

        self._items = get_items(item)


    def evaluate_stats(self):
        pass

