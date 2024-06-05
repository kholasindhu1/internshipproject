#calculatorex.py
print("*"*50)
print("CALCULATOR EXAMPLE USING ARITHEMATIC OPERATIONS")
print("*"*50)
print("\t1.Addition")
print("\t2.Subtraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Floor Division")
print("\t6.Modulo")
print("\t7.Exit")
print("*"*50)
while(True):
    ch=int (input("enter ur choice:"))
    match(ch):
        case 1:
            print("----------------------------")
            print("1.Addition")
            a=10
            b=10
            print("sum({}+{})={}".format(a,b,a+b))
            print("-----------------------------")
        case 2:
            print("----------------------------")
            print("2.Subtraction")
            a=100
            b=50
            print("sub({}-{})={}".format(a,b,a-b))
            print("-----------------------------")
        case 3:
            print("----------------------------")
            print("3.Multiplication")
            a = 10
            b = 10
            print("mul({}*{})={}".format(a,b,a*b))
            print("-----------------------------")
        case 4:
            print("----------------------------")
            print("4.Division")
            a = 100
            b = 50
            print("div({}/{})={}".format(a,b,a/b))
            print("-----------------------------")
        case 5:
            print("----------------------------")
            print("5.Floor Division")
            a = 100
            b = 50
            print("floordiv({}//{})={}".format(a,b,a//b))
            print("-----------------------------")
        case 6:
            print("----------------------------")
            print("6.Modulo")
            a = 100
            b = 50
            print("floordiv({}%{})={}".format(a,b,a%b))
            print("-----------------------------")
        case 7:
            print("-----------------------------")
            print("7.power")
            a=2
            b=3
            print("pow({}**{})={}".format(a,b,a**b))
            print("------------------------------")
            break
        case _:
            print("ur choice is wrong-----try again")
print("program execution completed")


