#class Person:
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age

#  def __str__(self):
#    return f'{self.name} lat {self.age}'

#p = Person('Slawek', 22)

#print(p)

#class Car:
#  def __init__(self, brand, model, country, age):
#    self.brand = brand
#    self.model = model
#    self.country = country
#    self.age = age

#  def __str__(self):
#    return f'{self.brand}, {self.model}, {self.country}, {self.age}'

#audi = Car('Audi', 'A4', 'Germany', 10)

#print(audi);

class Point: 
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f'{self.x},{self.y}'

class Quadraticfunction(Point):
  def __init__(self, x, y, A, B, C):
    super().__init__(x, y)
    self.A = A
    self.B = B
    self.C = C

  def __str__(self):
    return f'Wierzchołek: {self.x, self.y}, Współczynniki:{self.A}, {self.B}, {self.C}'

  def zero(self): 
    if self.A < 0 and self.x > 0 and self.y > 0:
      print(f'Funkcja ma miejsca zerowe')
    elif self.A > 0 and self.x < 0 and self.y < 0:
      print('Funkcja ma miejsca zerowe')
    else:
      print('Nie ma miejsc zerowych')

p = Quadraticfunction(5,5,-1,2,4)
p.zero()
