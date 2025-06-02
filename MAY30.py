from datetime import datetime

# Your birthdate
birth_date = datetime(1995, 7, 20)

# Today's date
today = datetime.today()

# Calculate the difference in days
days_old = (today - birth_date).days

print(f"You are {days_old} days old.")
