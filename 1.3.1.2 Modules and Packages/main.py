# from module import suml, prodl
from sys import path
import module

path.append('..\\modules')

# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(suml(zeroes))
# print(prodl(ones))

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

