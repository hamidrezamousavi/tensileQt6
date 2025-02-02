class Computer:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'the {} computer'.format(self.name)
    def execute(self):
        return 'executes a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    def play(self):
        return 'is playing an electronic song'
class Human:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return '{} the human'.format(self.name)
    def speak(self):
        return 'says hello'
class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.obj.__dict__.update(adapted_methods)
    def adapt(self):
        return self.obj
    def __str__(self):
        return str(self.obj)
s = Synthesizer('moog')

c = Computer('Asus')
objects = [Adapter(s,dict(execute = s.play)).adapt(),c]

for item in objects:
    print(item.execute())