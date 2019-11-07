var1 =10
import cmath

def Greeting_1(firstname,lastname):
    return 'Hi '+ firstname +' ' +lastname + '!'
print (Greeting_1('John', 'Harper'))

def Volume_1(a):
    var2 = ((4/3)*(cmath.pi))
    return var2

def Volume_2(a):
    var1 = Volume_1.var2 **3
    return var1
print (Volume_2(3))

