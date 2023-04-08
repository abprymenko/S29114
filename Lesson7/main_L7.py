from Lesson7.callobjects import Helper
from Lesson7.closing import Close
from Lesson7.counter_l7 import Counter
from Lesson7.decorators import Calc
from Lesson7.generators import Generator

# my_list = [1,2,3]
# iterator = iter(my_list)
#1
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#2
# for item in iterator:
#     print(item)
# for item in iterator:
#     print(item)
#3 Counter
# count = Counter(5)
# for i in count:
#     print(i)
#4 Generator
# generator = Generator(0)
# res = generator.raise_to_the_degrees_F(122345, 500)
# print(res)
# for item in generator.raise_to_the_degrees_F(122345, 500):#res:
#     print(f"{item}\n")
# generator = Generator(0)
# res = generator.raise_to_the_degrees_W(122345)
# print(res)
# for item in res:
#     print(f"{item}\n")
#5 Call objects
# helper = Helper("homework")
# print(helper)
# print(helper("cleaning"))
#6 Closing
# close = Close()
# my_close_func = close.closing("homework")
# print(my_close_func("cleaning"))
# print(my_close_func("driving"))
#7 decorators
# calc = Calc()
# calc.calculate("2**3")
# calc.calculate("2/0")