
class Person:
    def __init__(self, n, a, e, y, b):
        self.name = n
        self.attitude = a
        self.education = e
        self.age = y
        self.sitting = b

    def self_introduction(self):
        print("My name is", self.name)
        print("I am a", self.attitude, "person.")
        print("On what is related to the education, I am", self.education)
        print("I am", self.age, 'years old')
        print("Am i sitting? : ", self.sitting)

p1 = Person("Jodick", "loving", 'enrolled in college', 26, True)

print('')

p1.self_introduction()
print('')
p2 = Person('Danny', 'courageous', 'about to start university', 20, False)

class Robot:

    def __init__(self, i, o, r, k):
        self.izina = i
        self.ingeso = o
        self.indero = r
        self.imyaka = k
        
    def umwidondoro(self):
        print('I am a robot and I am given a name of', self.izina)
        print('For us robots,we do not have attitude because that is personal bias')
        print('therefore, it is', self.ingeso, 'we do not have attitudes')
        print('as for what is related to education, our programmer disigned us with special software')
        print('like', self.indero, 'which enable us to accomplish any task assigned to us')
        print('It has been', self.imyaka, 'years ever since we were developped.')

print('')

r1 = Robot('Sophie', True, 'face app or audio playe list', 10)
r2 = Robot('Lea', True, 'face recognition or talk back app', 5)

r1.umwidondoro()
print('')
r2.umwidondoro()
r2 = p1
print('')
r2.self_introduction()


