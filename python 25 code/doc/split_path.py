import os

a = os.path.split(os.path.abspath(__file__))
print(a)

b = os.path.split(a[0])
print(b)
print(b[0])