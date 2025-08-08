class Motor:
    merk = color = speed = ''

    def __init__(self, merk_motor, color_motor, speed_motor):
      self.merk = merk_motor
      self.color = color_motor
      self.speed = speed_motor

    def info(self):
      print(f'Motor dengan merk {self.merk} bewarna {self.color} sedang berjalan dengan kecepatan {self.speed} km/jam')


kawasaki = Motor('ninja', 'Hitam', '400')
kawasaki.jalan()