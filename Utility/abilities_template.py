import pandas as pd
import requests

def generate_abilities_template():
    """
    Generate abilities template for all champions.

    """

    response = requests.get('https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics').content

    df = pd.read_html(response)[0]

    df = df[df['Champions'] != "Kled & Skaarl"]
    df = df[df['Champions'] != "Mega Gnar"]

    champs = df['Champions'].values

    with open('abilities_template.txt', 'w') as file:
        file.write('{')
        file.write('\n')
        for champ in champs:

            entry = f"""
    \"{champ}\" : {{
        "q": {{
        
        }},
        
        "w": {{
        
        }},
        
        "e": {{
        
        }},
        
        "r": {{
        
        }}
    }},
            """
            file.write(entry)
            file.write('\n')
        file.write('}')
