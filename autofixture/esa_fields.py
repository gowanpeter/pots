
#Okay, the field_values takes a class instance from autofixture.generators, so all I had to do was: generate the list of states;

from autofixture.generators import ChoicesGenerator

states = "waiting|email|post|einv".split('|')
rsg = ChoicesGenerator(values=states)
self.create_test_foo(10, values={'state': rsg})

#the misunderstanding rose from confusing autofixture's generators with generic python generators.