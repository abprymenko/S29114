class Calc:
    def __init__(self):
        pass
    def checker(self, *exc_types):
        def checker(function):
            def checker(*args, **kwargs):
                try:
                    result = function(*args, **kwargs)
                except exc_types as exc:
                    print(f"We have problems {exc}")
                else:
                    print(f"No problems. Result – {result}")
            return checker
        return checker
    @checker(NameError, TypeError, SyntaxError, ZeroDivisionError)
    def calculate(self, expression):
        return eval(expression)