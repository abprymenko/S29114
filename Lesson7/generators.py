class Generator:
    def __init__(self, i):
        self.i = i
    def raise_to_the_degrees_F(self, number, max_degree):
        for _ in range(max_degree):
            yield number ** self.i
            self.i += 1
    def raise_to_the_degrees_W(self, number):
        while True:
            if(self.i > 500):
                break
            yield number ** self.i
            self.i += 1
