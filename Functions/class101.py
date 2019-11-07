
def func1(name):
    print('Hi '+ name)

func1('Bill')
func1('Kilroy')


def func2(a, b, c):
    print(a * b + c)


func2(5, 1, 2)
func2(10, 2, -2)
func2('A', 3, 'K')



def func3(var1, var2):
    var1 *= 100        #var1 = var1 * 100
    var2 += var1       #var1 = var2 + var1
    return var2
new_var = func3(5, 10)
print(new_var)



def greet(first, last):
    return 'H ' + first + ' ' + last +', I never liked you.'

print(greet('Bill', 'Weld'))






def mixed_number(a, b):
    #Do stuff here
    return


var = '8.8'
print(var.count('8'))

def tst_func(a, b, c):
    a = b +c
    c = a + b
    return a, c

print(tst_func(1, 2, 3))

