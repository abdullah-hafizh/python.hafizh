class Animal:
  name = ''
  color = ''

  def __init__(self):
    print('Hello')

  def makeSound(self, sound):
    print(f'{self.name} with color {self.color} is making {sound}')

#buat object
cat = Animal()
print(type(cat))
cat.name = 'Miko'
print(cat.name)
cat.color = 'white'
print(cat.color)
cat.makeSound('meoww')

bird = Animal()
bird.name = 'Gagak'
print(bird.name)
bird.color = 'black'
print(bird.color)
bird.makeSound('koakkoakkoakk')



class Hewan:
  name = color = ''

  def __init__(self, animal_name, animal_color):
    self.name = animal_name
    self.color = animal_color

  def info(self):
    print(f'Hewan dengan nama {self.name} memiliki warna {self.color}') 

  def makeSound(self, sound):
    print(f'{self.name} with color {self.color} is making {sound}')

  def eat(self, food):
    print(f'{self.name} is eating {food}')

kucing = Hewan('Tom', 'black')
kucing.info()
kucing.makeSound('meoww')
kucing.eat('fish')

tikus = Hewan('Jerry', 'black')
tikus.info()
tikus.makeSound('cittcitt')
tikus.eat('cheese')