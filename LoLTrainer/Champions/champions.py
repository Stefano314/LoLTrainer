
from .ChampionsInfo.attributes import get_attributes, clear_cache
from LoLTrainer.Trainer.processing import check_items
from LoLTrainer.Items.items import get_item

class LoLChampions():
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

        # PUBLIC:

        # Generic stats
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

        # Items
        self.items = []

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

        self.level_up(self.lvl)
        self.item_upgrade(check_items())

    def remove_item(self, item) -> None:

        if item in self.items:
            self.items.remove(item)
        self.update_champ()

    def item_upgrade(self, item : list) -> None:

        self.items.append(get_item(item))
