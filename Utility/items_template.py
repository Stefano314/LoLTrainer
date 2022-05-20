
def generate_items_template():
    """
    Probably there was website from picking all champs and stuff, but this works too.
    Remember to remove the comma at the very end of the template.

    """
    starter_items = ['Cull', 'Dark Seal', "Doran's Blade", "Doran's Ring", "Doran's Shield", 'Emberknife',
                     'Hailblade', "Guardian's Blade", "Guardian's Hammer", "Guardian's Horn", "Guardian's Orb",
                     'Relic Shield', 'Spectral Sickle', "Spellthief's Edge", "Steel Shoulderguards",
                     'Tear of the Goddess']

    boots = ['Boots', "Berserker's Greaves", "Boots of Swiftness", "Ionian Boots of Lucidity", "Mercury's Treads",
             'Mobility Boots', "Plated Steelcaps", "Sorcerer's Shoes"]

    basic_items = ['Amplifying Tome', 'B. F. Sword', "Blasting Wand", "Stopwatch", "Broken Stopwatch",
                   'Cloak of Agility', 'Cloth Armor', "Dagger", "Faerie Charm", "Long Sword", 'Needlessly Large Rod',
                   'Null-Magic Mantle', 'Pickaxe', "Rejuvenation Bead", "Ruby Crystal", 'Sapphire Crystal', 'Sheen']

    epic_items = ['Aegis of the Legion', 'Aether Wisp', "Bami's Cinder", "Bandleglass Mirror", "Blighting Jewel",
                  'Bramble Vest', "Caulfield's Warhammer", "Chain Vest", "Executioner's Calling", "Fiendish Codex",
                  'Forbidden Idol', 'Frostfang', "Crystalline Bracer", "Giant's Belt", "Glacial Buckler",
                  'Harrowing Crescent', 'Hearthbound Axe', 'Hexdrinker', 'Hextech Alternator', 'Ironspike Whip',
                  'Kindlegem', 'Kircheis Shard', 'Last Whisper', 'Leeching Leer', 'Lost Chapter', 'Negatron Cloak',
                  'Noonquiver', 'Oblivion Orb', 'Phage', 'Quicksilver Sash', 'Rageknife', 'Recurve Bow',
                  'Runesteel Spaulders', "Seeker's Armguard", 'Serrated Dirk', "Spectre's Cowl", "Targon's Buckler",
                  'Tiamat', "Vampiric Scepter", 'Verdant Barrier', "Warden's Mail", "Watchful Wardstone",
                  "Winged Moonplate", 'Zeal']

    legendary_items = ["Abyssal Mask", "Anathema's Chains", "Archangel's Staff", "Ardent Censer", "Axiom Arc",
                       "Banshee's Veil", "Black Cleaver", "Black Mist Scythe", "Blade of the Ruined King",
                       "Bloodthirster", "Bulwark of the Mountain", "Chempunk Chainsword", "Chemtech Putrifier",
                       "Cosmic Drive", "Dead Man's Plate", "Death's Dance", "Demonic Embrace", "Edge of Night",
                       "Essence Reaver", "Fimbulwinter", "Force of Nature", "Frozen Heart", "Gargoyle Stoneplate",
                       "Guardian Angel", "Guinsoo's Rageblade", "n Focus", "Hullbreaker", "Infinity Edge",
                       "Knight's Vow", "Lich Bane", "Lord Dominik's Regards", "Manamune", "Maw of Malmortius",
                       "Mejai's Soulstealer", "Mercurial Scimitar", "Mikael's Blessing", "Morellonomicon",
                       "Mortal Reminder", "Muramana", "Nashor's Tooth", "Navori Quickblades", "Pauldrons of Whiterock",
                       "Phantom Dancer", "Rabadon's Deathcap", "Randuin's Omen", "Rapid Firecannon", "Ravenous Hydra",
                       "Redemption", "Runaan's Hurricane",
                       "Rylai's Crystal Scepter", "Seraph's Embrace", "Serpent's Fang", "Serylda's Grudge",
                       "Shadowflame", "Shard of True Ice", "Silvermere Dawn", "Spirit Visage",
                       "Staff of Flowing Water", "Sterak's Gage", "Stormrazor", "The Collector", "Thornmail ",
                       "Titanic Hydra", "Umbral Glaive", "Vigilant Wardstone",
                       "Void Staff", "Warmog's Armor", "Winter's Approach", "Wit's End", "Youmuu's Ghostblade",
                       "Zeke's Convergence", "Zhonya's Hourglass"]

    mythic_items = ["Crown of the Shattered Queen", "Divine Sunderer", "Duskblade of Draktharr", "Eclipse",
                    "Evenshroud", "Everfrost", "Frostfire Gauntlet", "Galeforce", "Goredrinker", "Hextech Rocketbelt",
                    "Immortal Shieldbow", "Imperial Mandate", "Kraken Slayer", "Liandry's Anguish",
                    "Locket of the Iron Solari", "Luden's Tempest", "Moonstone Renewer", "Night Harvester",
                    "Prowler's Claw", "Riftmaker", "Shurelya's Battlesong", "eaker", "Sunfire Aegis",
                    "Trinity Force", "Turbo Chemtank"]



    with open('items_template.txt', 'w') as file:
        file.write('{')
        file.write('\n')

        # Starter Items
        file.write('"_comment": "Starter Items",')

        for item in starter_items:
            entry = f"""
    "{item}" : {{
        "name": "{item}",
        "gold": 0,
        "HP": 0,
        "AP": 0,
        "AD": 0,
        "physical_armor": 0,
        "magical_armor": 0,  
        "mana": 0,
        "lethality": 0,
        "armor_penetration": 0,
        "omivamp": 0,
        "life_steal": 0,
        "BONUS": {{}}
    }},
        """
            file.write(entry)
            file.write('\n')

        # Boots
        file.write('"_comment": "Boots",')

        for item in boots:
            entry = f"""
    "{item}" : {{
        "name": "{item}",
        "gold": 0,
        "HP": 0,
        "AP": 0,
        "AD": 0,
        "physical_armor": 0,
        "magical_armor": 0,  
        "mana": 0,
        "lethality": 0,
        "armor_penetration": 0,
        "omivamp": 0,
        "life_steal": 0,
        "BONUS": {{}}
    }},
        """
            file.write(entry)
            file.write('\n')

        # Basic Items
        file.write('"_comment": "Basic Items",')

        for item in basic_items:
            entry = f"""
    "{item}" : {{
        "name": "{item}",
        "gold": 0,
        "HP": 0,
        "AP": 0,
        "AD": 0,
        "physical_armor": 0,
        "magical_armor": 0,  
        "mana": 0,
        "lethality": 0,
        "armor_penetration": 0,
        "omivamp": 0,
        "life_steal": 0,
        "BONUS": {{}}
    }},
        """
            file.write(entry)
            file.write('\n')

        # Epic Items
        file.write('"_comment": "Epic Items",')
        for item in epic_items:
            entry = f"""
    "{item}" : {{
        "name": "{item}",
        "gold": 0,
        "HP": 0,
        "AP": 0,
        "AD": 0,
        "physical_armor": 0,
        "magical_armor": 0,  
        "mana": 0,
        "lethality": 0,
        "armor_penetration": 0,
        "omivamp": 0,
        "life_steal": 0,
        "BONUS": {{}}
    }},
        """
            file.write(entry)
            file.write('\n')

        # Legendary Items
        file.write('"_comment": "Legendary Items",')
        for item in legendary_items:
            entry = f"""
    "{item}" : {{
        "name": "{item}",
        "gold": 0,
        "HP": 0,
        "AP": 0,
        "AD": 0,
        "physical_armor": 0,
        "magical_armor": 0,  
        "mana": 0,
        "lethality": 0,
        "armor_penetration": 0,
        "omivamp": 0,
        "life_steal": 0,
        "BONUS": {{}}
    }},
        """
            file.write(entry)
            file.write('\n')

        # Mythic Items
        file.write('"_comment": "Mythic Items",')
        for item in mythic_items:
            entry = f"""
    "{item}" : {{
        "name": "{item}",
        "gold": 0,
        "HP": 0,
        "AP": 0,
        "AD": 0,
        "physical_armor": 0,
        "magical_armor": 0,  
        "mana": 0,
        "lethality": 0,
        "armor_penetration": 0,
        "omivamp": 0,
        "life_steal": 0,
        "BONUS": {{}}
    }},
        """
            file.write(entry)
            file.write('\n')

        # End file
        file.write('}')
