#studentgrade.py
class student:
    def readstuddata(self):
        self.tel=98
        self.hin=90
        self.eng=79
        self.mat=67
        self.sci=82
        self.soc=80

    def totmarks(self):
        totmarks=self.tel+self.hin+self.eng+self.mat+self.sci
        print("totmarks={}".format(self.tel+self.hin+self.eng+self.mat+self.sci+self.soc))
        percentage=totmarks/600*100
        print("percentage={}".format(percentage))


        if(totmarks <= 600):
            print("grade A------excellent".format(self.totmarks))
        elif(totmarks >= 450):
            print("grade B-------average".format(self.totmarks))
        elif(totmarks >= 350):
            print("grade C-------try to improve ur study".format(self.totmarks))
        elif(totmarks >= 250):
            print("grade D-------u have to improve much".format(self.totmarks))
        elif(totmarks >= 200):
            print("grade zero-----fail")

#main program
s=student()
s.readstuddata()
s.totmarks()
