from random import random

class learning:
    def __init__(self, input, output, w=0.1, learning_rate=0.1) -> None:
        self.input = input
        self.output = output
        self.w = w 
        self.learning_rate = learning_rate
        self.prediction = None

    @classmethod
    def accuration(cls, base, number):
        return (number/base) * 100

    def predict(self, i) -> float:
        return i*self.w

    def linear_regression(self) -> None:
        """ Return true if it's totally accurated. """

        self.prediction = [self.predict(i) for i in input]
        errors = [o-p for o, p in zip(output, self.prediction)]
        accur = [round(self.accuration(i, e)) for i, e in zip(self.input, errors)]
        costs = sum(errors)/len(self.output)
        self.w += costs * self.learning_rate
        totally_accurated = all(list(map(lambda i: not i, accur)))
        if(totally_accurated):   
            return True

input = [2,4,6,8,10]
b = round(random() * 100) + random() 
output = [i*b for i in input]
inter = learning(input, output)

for _ in range(0, 100):
    if (inter.linear_regression()):
        break