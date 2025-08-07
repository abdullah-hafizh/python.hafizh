class Animal:
  name = ''
  color = ''

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
bird.makeSound('citcitcuuitt')