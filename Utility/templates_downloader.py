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

    generate_champions_stats_template()
    generate_items_template()
    get_item_images()


def generate_templates():

    generate_abilities_template()
