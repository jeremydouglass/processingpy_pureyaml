"""
Processing.py pureyaml

A simple example of parsing YAML in a Processing.py sketch
using the pureyaml module.

Based on the pureyaml usage example from:

	https://github.com/bionikspoon/pureyaml

pureyaml requires ply as a submodule, and the future module.
These modules are bundled in this example sketch. They may
instead be added to Processing / libraries / site-packages
for use by all Processing.py sketches.

"""

import pureyaml
from textwrap import dedent
from pprint import pprint

yamltext = dedent("""
    marvel:
    - iron man
    - the hulk
    - captain america
    dc:
    - batman
    - the joker
    - superman
""")[1:]

# second example from test_ex_2_01_sequence_of_scalars

from pureyaml.parser import YAMLParser
from pureyaml.nodes import *
parser = YAMLParser(debug=True)
yamltext2 = dedent("""
    - Mark McGwire
    - Sammy Sosa
    - Ken Griffey
    """)[1:]

def parse(text):
    nodes = parser.parse(text)
    return nodes

def setup():

    pprint(pureyaml.load(yamltext))

    # prints:
    # {'dc': ['batman', 'the joker', 'superman'],
    #  'marvel': ['iron man', 'the hulk', 'captain america']}
    
    print(pureyaml.dump(pureyaml.load(yamltext)))

    # prints:
    # dc:
    # - batman
    # - the joker
    # - superman
    # marvel:
    # - iron man
    # - the hulk
    # - captain america

    print(yamltext2)    
    print(parse(yamltext2))
    
    # prints:
    # <Docs:(<Doc:(<Sequence:(<Str:'Mark McGwire'>,
    #   <Str:'Sammy Sosa'>, <Str:'Ken Griffey'>)>,)>,)>

    buildyaml = Docs(
         Doc(
             Sequence(
                 Str('Mark McGwire'),
                 Str('Sammy Sosa'),
                 Str('Ken Griffey'),
             ),
         ),
    )
    
    print(buildyaml)
    