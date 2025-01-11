#Simple Calculator Using Arithmetic Operators

class Arithmetic:
    def getvals(self):
        print("=" * 50)
        self.a=float(input("Enter First Value:"))
        self.b = float(input("Enter Second Value:"))
        self.op=input("Enter Any Arithmetic Operator:")
        print("="*50)
class Calculator:
    
    def cal(ao):
        match(ao.op):
            case "+":
                print("sum({},{})={}".format(ao.a,ao.b,ao.a + ao.b))
            case "-":
                print("sub({},{})={}".format(ao.a, ao.b, ao.a - ao.b))
            case "*":
                print("mul({},{})={}".format(ao.a, ao.b, ao.a * ao.b))
            case "/":
                print("div({},{})={}".format(ao.a, ao.b, ao.a / ao.b))
            case "//":
                print("div({},{})={}".format(ao.a, ao.b, ao.a // ao.b))
            case "%":
                print("mod({},{})={}".format(ao.a, ao.b, ao.a % ao.b))
            case "**":
                print("pow({},{})={}".format(ao.a, ao.b, ao.a ** ao.b))
            case _:
                print("{} is not Arithmetic Operator-try again".format(ao.op))

#Main Program
ao=Arithmetic()
while(True):
    try:
        ao.getvals()
        Calculator.cal(ao)
    except ValueError:
        print("Don't enter alnums,strs and symbols--try again")
    else:
        break