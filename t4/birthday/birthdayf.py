import datetime
import jdatetime

def main(birthday_user:str) -> str:
    """
    This function takes a string representing 
    the user's date of birth in the format 'yyyy-mm-dd'
    and calculates the following:
        
    1- Total elapsed seconds from the user's birth until now.
        
    2- The number of days and minutes left until the next birthday.
        
    3- The user's date of birth in Jalali format.
        
    Parameters:
    -----------
    birthday_user : str
        A string representing the user's date of birth in the format 'yyyy-mm-dd'.
            
    Returns:
    --------
    str
        A string including the calculated results.
    """
    # Convert the input string
    birthday = datetime.datetime.strptime(birthday_user, "%Y-%m-%d")

    # Calculate the number of seconds
    today = datetime.datetime.now()
    elapsed_seconds = (today - birthday).total_seconds()

    # Calculate the date of the next birthday
    if today.month > birthday.month or (today.month == birthday.month and today.day >= birthday.day):
        next_birthday_year = today.year
    else:
        next_birthday_year = today.year - 1

    next_birthday = datetime.datetime(next_birthday_year, birthday.month, birthday.day)

    # Calculate the number of days and minutes left until the next birthday
    time_left = next_birthday - today
    days_left = time_left.days
    minutes_left = time_left.seconds // 60

    # Convert date of birth to solar date
    jalali_birthday = jdatetime.datetime.fromgregorian(year=birthday.year, month=birthday.month, day=birthday.day)
    jalali_birthday_f = jalali_birthday.strftime("%Y/%m/%d")

    # Create a string including the calculated results
    print(f"Total elapsed seconds from your birth until now: {elapsed_seconds} seconds.")
    print(f"Number of days and minutes left until your next birthday: {days_left} days, {minutes_left} minutes.")
    print(f"Your date of birth in Jalali format: {jalali_birthday_f}.")

    return print

Birthday_user = input("Enter your date of birth (format: yyyy-mm-dd): ")

if __name__ == "__main__":
    main(Birthday_user)