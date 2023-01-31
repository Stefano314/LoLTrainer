from .abilities_template import generate_abilities_template
from .champions_stats_template import generate_champions_stats_template
from .items_template import generate_items_template
from .images_downloader import get_item_images

def update_game():
    """
    Description
    -----------
    Run this script everytime a new League of Legends game update is released.
    """

    print("- Retrieving champions stats from 'leagueoflegends.fandom.com' ...")
    generate_champions_stats_template()

    print("- Retrieving items stats from 'leagueoflegends.fandom.com' ...")
    generate_items_template()

    print("- Downloading items images from 'leagueoflegends.fandom.com' ...")
    get_item_images()
    
    print("Compleated!")


def generate_templates():

    print("- Generating ability template for all champions ...")
    generate_abilities_template()
    
    print("Compleated!")