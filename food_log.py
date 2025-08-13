import csv
from datetime import datetime

def log_food_entry():
    """Prompts the user for food details and appends them to food_log.csv."""
    try:
        date = input("Enter date (YYYY-MM-DD, press enter for today): ")
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')

        meal_type = input("Enter meal type (e.g., Breakfast, Lunch, Dinner, Snack): ").strip().title()
        food_item = input("Enter food item: ").strip().title()
        calories = int(input("Enter calories: "))
    except ValueError:
        print("Invalid calorie input. Please enter a number.")
        return

    # Prepare data for CSV
    entry = [date, meal_type, food_item, calories]

    # Open the CSV file in append mode
    with open('food_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(entry)

    print("Food entry logged successfully!")

if __name__ == "__main__":
    log_food_entry()
