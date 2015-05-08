import autofixture
from autofixture import AutoFixture

GlazeLookupFixture = AutoFixture(GlazeLookup, --overwrite-defaults = True, )

class GlazeLookupFixture(AutoFixture):

     class Values:
          glaze_description = generators.StringGenerator(self, chars=None, multiline=False,
                                               min_length=10, max_length= 30)
          glaze_name = generators.ChoicesGenerator(
               values="aqua,black,blue,fuchsia,gray,green,lime,maroon,navy, olive,orange,purple,red,silver,teal,white,yellow".split(',')
          )
          glaze_begin_date = generators.DateTimeGenerator(
               min_date=datetime(2009,1,1),
               max_date=datetime(2009,12,31))
          glaze_end_date = generators.DateTimeGenerator(
               min_date=datetime(2009,1,1),
               max_date=datetime(2009,12,31))
autofixture.register(GlazeLookup, GlazeLookupFixture, overwrite=False, fail_silently=False)


