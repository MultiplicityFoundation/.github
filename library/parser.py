# parser.py
# Lark-based parser for Multiplicity DSL
# Translates DSL into MultiplicityManager calls
# Aligned with Ξ-Constitution and Λᵖ-Archivum

from lark import Lark, Transformer
from manager import MultiplicityManager, MultiplicityBound

class MultiplicityTransformer(Transformer):
    def __init__(self, manager: MultiplicityManager):
        self.manager = manager
        self.multiplicity_map = {
            "0..1": MultiplicityBound.ZERO_TO_ONE,
            "1": MultiplicityBound.ONE,
            "0..*": MultiplicityBound.ZERO_TO_MANY,
            "1..*": MultiplicityBound.ONE_TO_MANY
        }

    def assoc_stmt(self, items):
        source_class, source_mult, target_class, target_mult = items
        assoc_id = self.manager.define_association(
            source_class=str(source_class),
            source_multiplicity=self.multiplicity_map[str(source_mult)],
            target_class=str(target_class),
            target_multiplicity=self.multiplicity_map[str(target_mult)]
        )
        return assoc_id

    def link_stmt(self, items):
        source_class, source_id, target_class, target_id = items
        self.manager.link_instances(
            assoc_id=self.manager.associations.keys()[0],  # Assume first assoc for simplicity
            source_instance=str(source_id),
            target_instance=str(target_id)
        )
        return True

    def multiplicity(self, items):
        return items[0]

    def IDENTIFIER(self, token):
        return token.value

def parse_multiplicity_dsl(dsl_code: str, manager: MultiplicityManager):
    """Parse Multiplicity DSL and execute actions."""
    with open("multiplicity.lark", "r") as f:
        grammar = f.read()
    parser = Lark(grammar, start="start")
    tree = parser.parse(dsl_code)
    MultiplicityTransformer(manager).transform(tree)
