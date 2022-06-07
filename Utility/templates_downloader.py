from .abilities_template import generate_abilities_template
from .champions_stats_template import generate_champions_stats_template
from .items_template import generate_items_template

def generate_templates():

    generate_champions_stats_template()
    generate_abilities_template()
    generate_items_template()
