import numpy as np
from arithmetic import Number


class Minus:
    def minus(self, ):
        self.number = self.number - 1


class Double(Number, Minus):
    def __init__(self, float_number):
        super(Double, self).__init__(float_number)


if __name__ == '__main__':
    n = Number(5)
    n.add_one()
    n.minus()
    print(n.number)
