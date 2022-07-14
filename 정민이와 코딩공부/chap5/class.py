'''

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
'''

class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second=second
    def add(self):
        result = self.first + self.second
        return result

a= Fourcal()
a.setdata(4,2)
print(a.add())