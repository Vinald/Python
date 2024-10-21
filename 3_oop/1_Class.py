# Example 1
class Person:
    def __init__(self, name=None, marks=None):
        self.name = name
        self.marks = marks
    
    def __del__(self):
        print('Objected being deleted')
        

person_1 = Person('Samuel', 84)
name = person_1.name
mark = person_1.marks

print(f'Person with name {name} and marks {mark}')

# Example 2
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        
    def __add__(self, other):
        vector = self.x + other.x, self.y + other.y
        return (vector)


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)