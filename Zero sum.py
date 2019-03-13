class zero_sum():

    def __init__(self,array):
        self.array=array
        self.result=[]

    def returner(self):
        for i,x in enumerate(self.array[:len(self.array)]):
            for j,y in enumerate(self.array[i+1:]):
                if -(x+y) in self.array[i+j:]:
                    for z in (x,y,-(x+y)):
                        self.array.remove(z)
                    self.result.append([x,y,-(x+y)])
                    return zero_sum.returner(self)
        return self.result

a=zero_sum([-25])
print(a.returner())