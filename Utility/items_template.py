import pandas as pd
import requests
import os

ITEMS_PATH =  os.path.join(os.getcwd(), 'LoLTrainer', 'Items', '')

def generate_items_template():
    """
    Probably there was website from picking all champs and stuff, but this works too.
    Remember to remove the comma at the very end of the template.

    """

    response = requests.get('https://leagueoflegends.fandom.com/wiki/List_of_items%27_stats').content

    df1 = pd.read_html(response)[0].fillna('0')
    df1.columns = ['Item', 'gold', 'AD', 'AS', 'critical_chance', 'life_steal', 'armor_penetration', 'lethality', 'Maps']

    df1['AS'] = df1['AS'].apply(lambda x : int(x.replace('%', ''))/100)
    df1['AD'] = df1['AD'].apply(lambda x : int(x))
    df1['lethality'] = df1['lethality'].apply(lambda x : int(x))
    df1['critical_chance'] = df1['critical_chance'].apply(lambda x : int(x.replace('%', ''))/100)
    df1['life_steal'] = df1['life_steal'].apply(lambda x : int(x.replace('%', ''))/100)
    df1['armor_penetration'] = df1['armor_penetration'].apply(lambda x : int(x.replace('%', ''))/100)


    df2 = pd.read_html(response)[1].fillna('0')
    df2.columns = ['Item', 'gold', 'AP', 'AH', 'mana', 'mana_regen', 'hsp', 'omnivamp', 'magic_penetration', 'Maps']

    df2['AP'] = df2['AP'].apply(lambda x : int(x))
    df2['AH'] = df2['AH'].apply(lambda x : int(x))
    df2['mana'] = df2['mana'].apply(lambda x : int(x))
    df2['mana_regen'] = df2['mana_regen'].apply(lambda x : int(x.replace('%', ''))/100)
    df2['hsp'] = df2['hsp'].apply(lambda x : int(x.replace('%', ''))/100)
    df2['omnivamp'] = df2['omnivamp'].apply(lambda x : int(x.replace('%', ''))/100)
    df2['magic_penetration'] = df2['magic_penetration'].apply(lambda x : int(x.replace('%', ''))/100)


    df3 = pd.read_html(response)[2].fillna('0')
    df3.columns = ['Item', 'gold', 'HP', 'physical_armor', 'magical_armor', 'HP_regen', 'Maps']

    df3['HP_regen'] = df3['HP_regen'].apply(lambda x : int(x.replace('%', ''))/500)

    items = pd.merge(pd.merge(df1,df2,how='outer'),df3, how='outer').fillna(0)

    columns_names = ['Item', 'gold', 'AD', 'AS', 'critical_chance', 'life_steal', 'armor_penetration',
                     'lethality', 'AP', 'AH', 'mana', 'mana_regen', 'hsp', 'omnivamp', 'magic_penetration', 'HP',
                     'physical_armor', 'magical_armor', 'HP_regen', 'Maps']

    items = items.sort_values('Item')
    items=items.reindex(columns=columns_names).reset_index(drop=True)
    items.to_csv(ITEMS_PATH+'items.csv')
