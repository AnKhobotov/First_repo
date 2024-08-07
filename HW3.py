import datetime
from datetime import datetime
import random

#print(datetime.today())

def getDaysFromToday(datum):
    try:
        datum = str(datum)
        a = datetime.strptime(datum, "%Y.%m.%d").date()
        today = datetime.now().date()
        diff = (today - a)
        print(diff.days)
        return diff.days
    except ValueError:
        print(f"Datum should be in 'YYYY-MM-DD' format")
getDaysFromToday("2024.07.30")

def get_numbers_ticket(min, max, quantity):
    num_set = set()
    nlist = []
    q = quantity
    print(q)
    #min, max, quantity = int()
    #a = random.randint(min, max)
    try:
        if 0 < min and max < 1000:
            if min < quantity < max:
                while  len(num_set) < q :
                    a = random.randint(min, max)
                    num_set.add(a)
                    #num_list.sort()
                    quantity -=1
                    len(num_set)
                    for i in num_set:
                        nlist.append(i)
                        nlist.sort()
                        #num_list = list[num_list]
                        #num_list.sort(a)
                    print(a, nlist, q)
            print (f"{quantity} should be positive number less then {max}")    
        print( f"{min} and {max} should be positive number less then 1000")
    except ValueError:
        print("Please check! All numbers  should be positive number less then 1000") 
                    #print(a, nlist, q)
get_numbers_ticket(1,49,0)     