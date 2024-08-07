import datetime
from datetime import timedelta
from datetime import datetime
#import timedelta
data = datetime.datetime.now()
print(data)




def string_to_date(date_string):
    formatted_date_string = datetime.strptime(date_string, "%Y.%m.%d").date() 
    print(formatted_date_string)

string_to_date("2021.05.21")

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

"""def date_to_string(date):
    return date.strftime(date, "%Y.%m.%d")"""

users =[
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}]
for i in users:
    a = i.get("birthday")
    #string_to_date(a)
    i.update({"birthday" : string_to_date(a)})
    
    print(type(i))
print(users)   

# def find_next_weekday(start_date, weekday):
#     datum1 = string_to_date(start_date)
#     wdnum = datum1.weekday()
#     weekint = timedelta(days = (6-wdnum) )
#     if wdnum <= weekday:
#         datum1 = datum1 + timedelta(days = (weekday- wdnum))
#         print(datum1,21)
#     datum1 = datum1 + weekint 

#     datum1 = datum1.strftime("%Y.%m.%d")
#     print(datum1, type(datum1))
# find_next_weekday("2024.07.31", 1)
    
#date_to_string(delta)
def prepare_user_list(user_data):
    prepared_list = []
    user_data = users
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    #today = date.today()
    #bdays = prepare_user_list(users).replace(year = today.year())
    #upcoming_birthdays.append(bdays)


print(prepare_user_list(users)) #upcoming_birthdays)


