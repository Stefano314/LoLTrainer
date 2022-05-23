from .abilities_template import generate_abilities_template
from .generalities_template import generate_generalities_template
from .items_template import generate_items_template
from .champions_offensive_template import generate_offensive_champions_template
from .champions_defensive_template import generate_defensive_champions_template

def generate_templates():

    generate_abilities_template()
    generate_generalities_template()
    generate_items_template()
    generate_offensive_champions_template()
    generate_defensive_champions_template()
