'''

Mixin案例

'''

class person():
    name = 'leilei'
    age = 18
    def eat(self):
        print('Eating....')
    def drink(self):
        print('Drinking...')
    def sleep(self):
        print('Sleeping...')

class teacher(person):
    def work(self):
        print('working...')

class student():
    def study(self):
        print('Studying...')

class tutor(teacher,student):
    pass

t = tutor()
print(tutor.__mro__)
print(t.__dict__)
print(tutor.__dict__)

print('*'*50)

class teacherMixin():
    def work(self):
        print('work')

class studentMixin():
    def study(self):
        print('study')

class tutorMixin(person,teacherMixin,studentMixin):
    pass

tt = tutorMixin()
print(tutorMixin.__mro__)
print(tt.__dict__)
print(tutorMixin.__dict__)