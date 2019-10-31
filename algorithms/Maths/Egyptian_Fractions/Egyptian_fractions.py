import math

def EFN(nf , df):
    if(nf > 0 or df > 0):
        if(df % nf == 0)
            print("1/" + str(df // nf))
            return

        if(nf % df == 0):
            print("{}".format(int(nr // dr)))
            return
        
        if(df < nf):
            print("{}".format(int(nf//df)),end=" + ")
            EFN(nf % df, df)
            return
       
        if(nf < df):
            p=math.ceil(df / nf)
            print("1/{}".format(int(p)),end=" + ")
            EFN((nf * p) - df, df * p)
            return

nr = int(input("Enter the Numerator: "))
dr = int(input("Enter the Denominator: "))
print("The Egyptian Fraction of %d / %d is: "%(nr , dr))
EFN(nr , dr)
