import pandas as pd
import requests
import numpy as np
import os

INFO_PATH = os.path.join(os.getcwd(), "LoLTrainer", "Champions", "ChampionsInfo", "")

def generate_champions_stats_template():
    """
    Generates all the csv files containing the information related to every champion.

    """

    response = requests.get('https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics').content
    df = pd.read_html(response)[0]
    df = df[df['Champions'] != "Kled & Skaarl"]
    df = df[df['Champions'] != "Mega Gnar"]

    champs = df['Champions'].values

    def_stats = ["HP", "HP_growth", "mana", "mana_growth", "HP_regen", "HP_regen_growth", "mana_regen",
                 "mana_regen_growth", "physical_armor", "magical_armor", "tenacity"]
    off_stats = ["AD", "AP", "att_speed", "att_speed_growth", "att_range", "AD_growth", "mov_speed", "crit_dmg", "crit_%", "AH"]

    info = ["nickname", "resource_type", "class", "position", "range_type", "release date", "latest_patch", 'blue_essence']

    # Defensive stats
    defensive = pd.DataFrame(0, index = def_stats, columns = champs)

    defensive.loc['HP'] = df['HP'].values
    defensive.loc['HP_growth'] = df['HP+'].values
    defensive.loc['HP_regen'] = np.around(df['HP5'].values/5, decimals=2)
    defensive.loc['HP_regen_growth'] = np.around(df['HP5+'].values/5, decimals=2)
    defensive.loc['mana'] = df['MP'].values
    defensive.loc['mana_growth'] = df['MP+'].values
    defensive.loc['mana_regen'] = np.around(df['MP5'].values/5, decimals=2)
    defensive.loc['mana_regen_growth'] = np.around(df['MP5+'].values/5, decimals=6)
    defensive.loc['physical_armor'] = df['AR'].values
    defensive.loc['magical_armor'] = df['MR'].values

    defensive.to_csv(INFO_PATH+'defensive_attributes.csv')

    # Offensive stats
    offensive = pd.DataFrame(0, index = off_stats, columns = champs)

    df['AS+'] = df['AS+'].apply(lambda x : float(x.replace('+', '').replace("%", '')))

    offensive.loc['AD'] = df['AD'].values
    offensive.loc['att_speed'] = df['AS'].values
    offensive.loc['att_speed_growth'] = np.around(df['AS+'].values/100, decimals=5)
    offensive.loc['att_range'] = df['Range'].values
    offensive.loc['AD_growth'] = df['AD+'].values
    offensive.loc['mov_speed'] = df['MS'].values
    offensive.loc['crit_dmg'] = 1.75

    offensive.to_csv(INFO_PATH+'offensive_attributes.csv')


    # Generalities
    response = requests.get('https://leagueoflegends.fandom.com/wiki/List_of_champions').content
    df = pd.read_html(response)[1]

    
    def func(word, stopwords):
        for stopword in stopwords:
            word = word.replace(stopword, '')
        return word

    df['Champion'] = df['Champion'].apply(lambda x : func(x, champs))
    df = df[df['Classes'] != 'TBA']
    generalities = pd.DataFrame(0, index = info, columns = champs)

    # print()
    generalities.loc['nickname'] = df['Champion'].values
    generalities.loc['class'] = df['Classes'].values
    generalities.loc['release date'] = df['Release Date'].values
    generalities.loc['latest_patch'] = df['Last Changed'].values
    generalities.loc['blue_essence'] = df['Blue Essence'].values

    generalities.to_csv(INFO_PATH+'generalities.csv')
