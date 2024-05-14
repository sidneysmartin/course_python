# The Python Standard Library 👇
# https://docs.python.org/3/library/index.html

from datetime import datetime
# long form
"""
specific_date = datetime(year=2025, month=6, day=1, hour=7,
                         minute=15, second=0, microsecond=0)
print(specific_date)

"""

# short form
specific_date = datetime(2025, 6, 1, 7, 15, 0, 0)
print(specific_date)


# Get a specific property

print(f'Year: {specific_date.year}')

print(f'Month: {specific_date.month}')

print(f'Day: {specific_date.day}')

print(f'Hour: {specific_date.hour}')

print(f'Minute: {specific_date.minute}')

print(f'Second: {specific_date.second}')

print(f'Microsecond: {specific_date.microsecond}')

# Get the current date and time
current_date = datetime.now()
print(current_date)

# Get the current time
current_time = datetime.now()
print(current_time)
