# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

years_left = 90 - age_int
days_left = years_left * 365
weeks_left = years_left * 52
moths_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {moths_left} months left, and {years_left} years left, if you live up to 90. ")