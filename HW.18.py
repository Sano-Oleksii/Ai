current_day = 48
next_year_name = "Год Тигра"

def days_left(current_day):
    return 365 - current_day
def print_greeting(days_remaining, year_name):
    print(f"Через {days_left(current_day)} дня наступит {next_year_name}")
print_greeting(days_left(current_day), next_year_name)