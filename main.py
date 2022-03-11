import datetime

a = 2020
b = 12
c = 3
years = 0

input1, input2, input3 = input("Enter your birth year, month and day including space(i.e 2020(year) 12(month) 3(day)): ").split(" ")
# input4, input5, input6 = input("Enter 2nd datetime including space(i.e 2020(year) 12(month) 3(day)): ").split(" ")

p = datetime.datetime(int(input1), int(input2), int(input3))
# c = datetime.datetime(int(input4), int(input5), int(input6))
c = datetime.datetime.now()

if p>c:
	result = p-c
else:
	result = c-p

remains = str(result).split(' ')[0]
r = int(remains)

if r > 365:
	years = r//365
months = (r-(years*365))//30
days = (r-(years*365))%30

print(f'{years} years, {months} months and {days} days have passed till your birth')
