from datetime import datetime
import random

curent_date = datetime.now()

def get_days_from_today(date):
    super_date = datetime.strptime(date, '%Y-%m-%d')
    interval = super_date - curent_date
    return interval.days


print(get_days_from_today("2021-10-09"))




def get_numbers_ticket(min, max, quantity):
    rand_range = set()
    while len(rand_range) != quantity:
        if min >=1 and max <= 1000:
            rand_range.add(random.randint(min, max))
        else:
            break
    return sorted(list(rand_range))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

            

    

    

