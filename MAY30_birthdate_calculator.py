# from datetime import datetime

# # Your birthdate
# birth_date = datetime(1995, 7, 20)

# # Todays date
# today = datetime.today()

# # Calculate the difference in days
# days_old = (today - birth_date).days

# years_old = days_old // 365

# print(f"You are {days_old} days old.")


from datetime import datetime

birth_input = input("Enter your birth date (YYYY-MM-DD): ")

# Your birthdate
birth_date = datetime.strptime(birth_input, "%Y-%m-%d")

# Todays date
today = datetime.today()

# Calculate the difference in days
days_old = (today - birth_date).days

# Calculate the difference in years
years_old = days_old // 365

print(f"You are {days_old} days old.")
print(f"You are {years_old} years old.")
