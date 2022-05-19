
from .ChampionsInfo.attributes import get_attributes, clear_cache

from LoLTrainer.Items.items import get_item

class LoLChampions():
    '''
    Description
    -----------
    League of Legends champions class.
    This will initialize all champions in the game, giving them their base attributes.
    Once the champion is created,  its stats will change according to the level and to the items equipped.

    '''

    def __init__(self,  ID : str):

        # PRIVATE
        self._off_attributes = get_attributes(file_name = 'offensive_attributes', ID = ID)
        self._def_attributes = get_attributes(file_name ='defensive_attributes', ID = ID)
        self._abi_attributes = get_attributes(file_name ='abilities_attributes', ID = ID)
        self._generalities = get_attributes(file_name ='generalities', ID = ID)

        # PUBLIC:
        self.lvl = 1
        self.HP = self._def_attributes['HP']
        self.AP = self._off_attributes['AP']
        self.AD = self._off_attributes['AD']
        self.Ph_armor = self._def_attributes['physical_armor']
        self.Ma_armor = self._def_attributes['magical_armor']
        self.mana = self._def_attributes['mana']

        self.lethality = 0
        self.armor_penetration = 0
        self.omivamp = 0
        self.life_steal = 0

    def level_up(self, lvl : int = 0) -> None :
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

    def item_upgrade(self):
        # Probably it's better to put flags on every item
        pass