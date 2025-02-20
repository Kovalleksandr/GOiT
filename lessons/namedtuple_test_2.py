import collections


# Створення іменованого кортежу Person
Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])


# Створення екземпляра Person
cat = Cat('Simon', 4, 'Krabat')

# Виведення різних атрибутів іменованого кортежу
print(cat.nickname)       
print(cat.owner) 
print(cat.age)        
print(cat[2]) 