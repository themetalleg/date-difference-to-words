from datetime import datetime
from dateutil.relativedelta import relativedelta

def date_difference_in_words(date_str):
    # Parse the input date string into a datetime object
    input_date = datetime.strptime(date_str, "%Y-%m-%d")
    # Get today's date
    today = datetime.today()
    # Calculate the difference using relativedelta
    diff = relativedelta(today, input_date)
    
    # Create a list to hold each part of the difference
    difference_parts = []
    
    # Add years, months, and days to the list if they are non-zero
    if diff.years > 0:
        years_word = "year" if diff.years == 1 else "years"
        difference_parts.append(f"{diff.years} {years_word}")
    if diff.months > 0:
        months_word = "month" if diff.months == 1 else "months"
        difference_parts.append(f"{diff.months} {months_word}")
    if diff.days > 0:
        days_word = "day" if diff.days == 1 else "days"
        difference_parts.append(f"{diff.days} {days_word}")
    
    # Join the parts with commas and return the result
    return ", ".join(difference_parts)

# Example usage:
date_str = "2020-01-01"
print(date_difference_in_words(date_str))
