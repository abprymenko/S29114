class BuildingError(Exception):
    def __init__(self, amount, limit):
        self.limit = limit
        self.amount = amount
    def __str__(self):
        return  f"{self.amount} is grater then {self.limit}"
    def check(self, amount, limit):
        if(amount <= limit):
            return True
        else:
            raise BuildingError(amount, limit)
