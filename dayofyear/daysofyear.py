def is_year_leap(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return None

def days_months(year, month):
     
     days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

     if (month == 2) and (is_year_leap == True):
         return 29
     else:
         return days_per_month[month - 1]
     
def day_of_year(year, month, day):
    
    is_year_leap(year)
    days_months(year, month)

    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = sum(days_per_month[:month - 1]) + day
    
    return days
    

print(day_of_year(2024, 11, 26))
 