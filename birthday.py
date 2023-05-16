import datetime
import jdatetime

#Enter the user's date of birth
birthday_user = input("Enter your date of birth (format: yyyy-mm-dd): ")

#Convert the input string
birthday = datetime.datetime.strptime(birthday_user, "%Y-%m-%d")

#Calculate the number of seconds
Today = datetime.datetime.now()
Elapsed_seconds = (Today - birthday).total_seconds()

#Print the total elapsed seconds
print("total seconds form age: ", Elapsed_seconds , "secoend")

#Calculate the date of the next birthday
if Today.month > birthday.month or (Today.month == birthday.month and Today.day >= birthday.day):
    next_birthday_year = Today.year
else:
    next_birthday_year = Today.year - 1

next_birthday = datetime.datetime(next_birthday_year, birthday.month, birthday.day)

#Calculate the number of days and minutes left until the next birthday
time_left = next_birthday - Today
days_left = time_left.days
minutes_left = time_left.seconds // 60

#Congratulations print
print("Congratulations! Your next birthday: ", days_left, "day ", minutes_left, " It's another minute")

# Convert date of birth to solar date
jalali_birthday = jdatetime.datetime.fromgregorian(year=birthday.year, month=birthday.month, day=birthday.day)
jalali_birthday_f = jalali_birthday.strftime("%Y/%m/%d")

#Print date of birth in solar format
print("Your date of birth in Jalali format: ", jalali_birthday_f)
