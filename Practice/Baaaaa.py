from Mooooo import Cow
from Mooooo import Sheep
from Mooooo import Angel


inToThePut = int(input('Do you want Cow = 1 or sheep = 2 or Angel = 3 '))
if inToThePut == 1:
    animal = Cow()

elif inToThePut == 2:
    animal = Sheep()

else:
    animal = Angel()
someName = animal.NameOfAnimal()
inTheToPut = input(f'Do you want to kick the {someName}? ')