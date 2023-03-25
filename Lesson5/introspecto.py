import package.info as inf
import Lesson4.Human as h
import Lesson4.Student as s
import inspect
import  package.buildingerror as be

#print(inf.__name__)
#print(dir(inf.Info))
info = inf.Info()
'''
print(hasattr(info, "multiplier"))
print(hasattr(info, "multiplier1"))
print(hasattr(info, "showValue"))
print(hasattr(info, "__ge__"))
#print(getattr(info, "multiplier1"))#Throw exception
print(getattr(info, "multiplier1", False))
print(callable(info.multiplier))
print(callable(info.showInfoList))

#human = h.Human()
print(issubclass(inf.Info, h.Human))
print(issubclass(s.Student, h.Human))
print(isinstance(info, h.Human))
print(isinstance(info, inf.Info))
'''
'''
print(inspect.ismodule(inf))
print(f"showValue ismethod - {inspect.ismethod(info.showValue)}")
print(f"showValue isfunction - {inspect.isfunction(info.showValue)}")
print(f"showInfoDict ismethod - {inspect.ismethod(info.showInfoDict)}")
print(f"showInfoDict isfunction - {inspect.isfunction(info.showInfoDict)}")
print(f"getValue ismethod - {inspect.ismethod(info.getValue)}")
print(f"getValue isfunction - {inspect.isfunction(info.getValue)}")
print(inspect.getattr_static(info, "showValue"))
print(inspect.getattr_static(info, "showInfoDict"))
'''
#my_tuple = (10,20,30)
#my_tuple[1]=100
amount = 200
limit = 100

error = be.BuildingError(amount, limit)
#error.check(amount, limit)

try:
    result = 10/0
    #error.check( limit)
except TypeError as terror:
    print(terror)
except be.BuildingError as berror:
    print(berror)
except ArithmeticError as aerror:
    print(aerror)
except ZeroDivisionError as zerror:
    print(zerror)
except Exception as ex:
    print(ex)
except:
    print("Error default!")