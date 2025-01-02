class StepValueError(ValueError):
    pass

class Iterator:
    pointer = 0
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')


    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0:
            self.pointer += self.step
            if self.pointer > self.stop:
                raise StopIteration()
            return self.pointer
        if self.step < 0:
            self.pointer += self.step
            if self.pointer < self.stop:
                raise StopIteration()
            return self.pointer










try:
    iter1 = Iterator(10, 1, 1)

    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('шаг указан неверно')


