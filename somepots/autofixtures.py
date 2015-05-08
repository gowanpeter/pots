#from somepots.models import Piece, Condition, PublicationLookup, publication_link_piece, ExhibitionLookup, exhibition_link_piece, Documentation, documentation_link_piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, Logo,logo_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece, SetCollection, setCollection_link_piece

from somepots.models import Piece, GlazeLookup, glaze_link_piece, HeathLineLookup, heath_line_link_piece, MakerLookup, maker_link_piece, MaterialLookup, material_link_piece, MethodLookup, method_link_piece

from autofixture import generators, register, AutoFixture

class GlazeLookupAutoFixture(AutoFixture):
    field_values = {
        'glaze_name': generators.ChoicesGenerator(
            values="aqua,black,blue,fuchsia,gray,green,lime,maroon,navy, olive,orange,purple,red,silver,teal,white,yellow".split(',')
        )
    }

register(GlazeLookup, GlazeLookupAutoFixture)

class  HeathLineLookupAutoFixture(AutoFixture):
    field_values = {
        'heath_line_name': generators.ChoicesGenerator(
            values="Coupe, Rim, Chez Pannise, Alabama Chanin".split(',')
        )
    }

register(HeathLineLookup, HeathLineLookupAutoFixture)

class  MakerLookupAutoFixture(AutoFixture):
    field_values = {
        'maker_name': generators.ChoicesGenerator(
            values="Erminia Galdamez, Angila Weekly,  Milton Burnley,  Earle Hampshire,  Lael Warford,  Leilani Dennis,  Porsha Nodine,  Tammie Wert,  Tonie Schweinsberg,  Meryl Belville,  Latricia Landrum,  Margorie Galeano,  Josiah Torgrimson,  Kurt Picklesimer, Veola Callaham, Rolf Humphery,  Shari Carpenter , Belen Hott  ".split(',')
        )
    }

register(MakerLookup, MakerLookupAutoFixture)

class  MaterialLookupAutoFixture(AutoFixture):
    field_values = {
        'material_name': generators.ChoicesGenerator(
            values="Clay, Slip, Mixed materials".split(',')
        )
    }

register(MaterialLookup, MaterialLookupAutoFixture)


class  MethodLookupAutoFixture(AutoFixture):
    field_values = {
        'method_name': generators.ChoicesGenerator(
            values="Hand thrown, Hand built, Cast, Jiggered".split(',')
        )
    }

register(MethodLookup, MethodLookupAutoFixture)
