from datetime import date

# Get today's date
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"The current date is {day} / {month} / {year}"
filename = f"MMF_{year}_{month}_{day}"

# Heading
print(heading)
print(f"The file name will be {filename}.txt")
