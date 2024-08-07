print("Hello world!!!")

print("Hello Git!")

"""my_list = []
my_list.insert(0,2024) 
print(my_list)"""

"""def discount_price(price, discount):
    price = 100

    def apply_discount():
        nonlocal price
        print(price)
        price = price * (1 - discount)
    apply_discount()
    return price
    print(price, discount)
discount_price(100, 0.1)"""


"""def get_fullname(first_name, last_name, middle_name = ""):
    if middle_name is not True:
        return f"{first_name} {middle_name} {last_name}"
    return f"{first_name} {last_name}"
get_fullname("a", "b", "c")
print(get_fullname("a","b","c"))"""

"""def format_string(string, length):
    a = len(string)
    b = (length - a)//2
    if a >= length:
        string = string
    else:
        string = f" {b * ' '} {string}"
    print(string)    
format_string("str", 2)
print(format_string("str", 2))
print("a" * 5)"""

"""def format_string(string, length):
    a = len(string)
    b = ((length - a)//2)
    if a < length:
        string = f"{b*' '}{string}"
    return string
    print(string)
format_string("aaaaaaaaaaaaaaaaac", 22)"""

"""def first(size,*args):
    #a =(*args)
    b = 0
    suma = 0
    for i in args:
        b= b+1
    suma = size + b
    print(suma)
    return suma
    #print(suma)
first(5, 2)"""

def second(size,**kwargs):
    b = 0
    summ = 0
    for i in kwargs:
        b= b+1
    summ = size + b
    return summ
print(second(3, name = "a"))