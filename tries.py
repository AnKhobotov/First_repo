# from datetime import datetime, timedelta, date

# users =[
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}]


# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()
     

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")


# def prepare_user_list(user_data):
#     users =[
#     {"name": "Bill Gates", "birthday": "1955.3.25"},
#     {"name": "Steve Jobs", "birthday": "1955.3.21"},
#     {"name": "Jinny Lee", "birthday": "1956.3.22"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"}]
#     user_data = users
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list


# def get_upcoming_birthdays(users, days):
#     upcoming_birthdays = []
#     upcoming_birthdays1 = []
#     today = datetime.today().date()
#     timedelta1 = today +timedelta(days)
#     b_dthy = []
#     for user in users:
#         b_dthy.append({"name": user["name"], "birthday":string_to_date(user["birthday"]).replace(year = 2025)})
#     for user in b_dthy:
#         c = user.get("birthday")
#         if (c-today).days <= days:
#             upcoming_birthdays.append({"name": user["name"], "birthday":date_to_string(user["birthday"])})

    # for user in upcoming_birthdays:
    #    upcoming_birthdays1.append({"name": user["name"], "birthday":prepare_user_list(user["birthday"])}) 
       
        # if
        #     upcoming_birthdays.append(user)
        

    # #b_dthy.append(prepare_user_list(users).replace(year = today.year()))
    # for user in users:
    #     b_dthy.append({"name": user["name"], "birthday":prepare_user_list(user["birthday"])})
    #     for user in users:
    #         for k in user:
    #             if k == "birthday":
    #                 if today < value <= timedelta1:
    #                     upcoming_birthdays.append({"name": user["name"], "birthday":user["birthday"]})
    # for i in upcoming_birthdays:
    #     upcoming_birthdays.append({"name": user["name"], "birthday":date_to_string(user["birthday"])}) 
    # return upcoming_birthdays
#     print(upcoming_birthdays)
# get_upcoming_birthdays(users, 180)

"""def fonc(date):

    if  date
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        print(birthday_this_year)
        if today >= eday:
            birthday_this_year=(user["birthday"].replace(year=(today.year + 1))).date()
        return birthday_this_year"""
        
        # """
        # Додайте на цьому місці перевірку, чи не буде 
        # припадати день народження вже наступного року.
        # """
                  

        # """if 0 <= (birthday_this_year - today).days <= days:
        #     return adjust_for_weekend(birthday_this_year)
        # return adjust_for_weekend(birthday_this_year)
            
            # """ 
            # Додайте перенесення дати привітання на наступний робочий день,
            # якщо день народження припадає на вихідний. 
            # """
            
            # congratulation_date_str = date_to_string(birthday_this_year)
    #         upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    # return upcoming_birthdays"""