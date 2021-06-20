from datetime import date
f_date = date(2020, 8, 31)
l_date = date.today()
delta = l_date - f_date
days = delta.days
print("First date starting program is: (Monday)", f_date)
print("Today date is: ", l_date)
print("Days between : ", days)
print("Weeks done : ", days // 7)

