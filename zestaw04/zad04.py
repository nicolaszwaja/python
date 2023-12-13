# Dynamiczny charakter języka Python nie pozwala na bezpośrednie przeładowywanie funkcji o tych samych 
# nazwach, ale różnych argumentach. Z pomocą dekoratorów pojawiają się w język techniki emulujące takie 
# zachowania. W ramach zadania proszę przestudiować materiał na temat singledispatch oraz 
# singledispatchmethod z modułu functools oraz napisać dowolny kod ilustrujący te przypadki 

from functools import singledispatch

@singledispatch
def greet_person(name):
    print(f"Hello, {name}!")

@greet_person.register(str)
def _(name):
    print(f"Hey, {name}!")

@greet_person.register(int)
def _(name):
    print(f"Greetings to person number {name}!")

@greet_person.register(list)
def _(name):
    print(f"Shout out to {', '.join(name)}!")
    
@greet_person.register(bool)
def _(name):
    if(name):
        print(f"Hello!")
    else:        
        print(f"Bye!") 

greet_person("Alice")                                 
greet_person(["Harry", "Taylor", "Zayn"])    
greet_person(13)                  
greet_person(False)