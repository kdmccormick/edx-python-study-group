
class MyClass:
    pass

my_object = MyClass()

print()
print('This is my_object:', my_object)
print('This is my_object.__dict__:', my_object.__dict__)

print()
print('> my_object.my_attr = 1')
my_object.my_attr = 1
print()

print('This is my_object.__dict__:', my_object.__dict__)
print('This is my_object.my_attr:', my_object.my_attr)
print()