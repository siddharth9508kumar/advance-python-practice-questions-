class Simpleintrest:
    def __int__(self,principal,rate,time):
        self.principal=principal
        self.rate=rate
        self.time=time
    def simpleintrest(self):
        simpleintrest=(self.principal*self.rate*self.time)/100
        print(f"Simple intrest is: {simpleintrest}")
simpleintrest1=Simpleintrest()
simpleintrest1.__int__(1000,5,2)
simpleintrest1.simpleintrest()
