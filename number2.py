def leap_year(years):
    if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
        return True
    else:
        return False

years = int(input("Enter the year: "))
if leap_year(years):
    print(f"{years} is a  leap year.")
else:
    print(f"{years} is not a  leap year.")
