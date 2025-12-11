#Nama	: Mahmuddin Mursalim
#Nim	: D0425509
#Kelas	: B Sistem Informasi

class TwoStack:
    def __init__(self, size):
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = value

    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = value

    def pop1(self):
        if self.top1 >= 0:
            val = self.arr[self.top1]
            self.top1 -= 1
            return val

    def pop2(self):
        if self.top2 < len(self.arr):
            val = self.arr[self.top2]
            self.top2 += 1
            return val

ts = TwoStack(10)
ts.push1(1)
ts.push2(10)
ts.push1(2)
ts.push2(20)

print("Pop1:", ts.pop1())
print("Pop2:", ts.pop2())