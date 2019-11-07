import cmath

def mixed_number(a, b):
    var1 = a//b
    var2 = a%b
    return str(var1) +' ' + str(var2) + '/' + str(b)

print(mixed_number(9,2))


def vowel_count_1(a):
    var1 = a.count('a')
    var1 += a.count('e')
    var1 += a.count('i')
    var1 += a.count('o')
    var1 += a.count('u')
    return var1
print (vowel_count_1('hi my name is'))


def vowel_count_2(a):
    var1 = a.count('a')
    var2 = a.count('e')
    var3 = a.count('i')
    var4 = a.count('o')
    var5 = a.count('u')
    return var1, var2, var3, var4, var5

print(vowel_count_2('Hi my dhjian jja'))


def sphere_volume(a):
    var1 = 4/3 * (cmath.pi) * a**3
    return round(var1, 2)

print(sphere_volume(10))


def sphere_surface_area(a):
    var1 = 4 * cmath.pi * a **2
    return round(var1, 2)
print(sphere_surface_area(10))


def sphere_metrics(a):
    var1 = sphere_volume(a)
    var2 = sphere_surface_area(a)
    return 'Sphere Volume ' +str(var1) + '\n' + 'Sphere Surface: '+ str(var2)
print(sphere_metrics(10))



# def name_function(name):



def rgb_to_hex(a, b, c):
    var1 =  hex(a).replace('0x','')
    var2 = hex(b).replace('0x','')
    var3 = hex(c).replace('0x','')
    return var1 + var2 + var3
print(rgb_to_hex(255,100,104))

def hex_to_rgb(a, b, c):
    var1 = str(int(a, 16))
    var2 = str(int(b, 16))
    var3 = str(int(c, 16))
    return var1 + ',' + var2 + ',' + var3
print(hex_to_rgb('FF', 'C5', '00'))















