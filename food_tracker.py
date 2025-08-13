import pandas as pd
import matplotlib.pyplot as plt

def plot_weekly_calories():
    """Reads data from the CSV and plots a bar chart of daily calories over the last 7 days."""
    try:
        df = pd.read_csv('food_log.csv')
    except FileNotFoundError:
        print("Food log not found. Please log some food first.")
        return

    # Convert 'Date' to datetime objects and 'Calories' to a numeric type
    df['Date'] = pd.to_datetime(df['Date'])
    df['Calories'] = pd.to_numeric(df['Calories'])

    # Group by date and sum calories
    daily_calories = df.groupby('Date')['Calories'].sum()

    # Filter for the last 7 days of data
    last_week = daily_calories.tail(7)

    # Define a list of colors for the bars
    colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7']

    # Create the plot
    plt.figure(figsize=(10, 6))
    last_week.plot(kind='bar', color=colors)
    plt.title('Weekly Calorie Consumption')
    plt.xlabel('Date')
    plt.ylabel('Total Calories')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

    #---------------------------------------------------------------

def plot_daily_breakdown(date):
    #Plots a pie chart showing calorie breakdown by meal type for a specific date.
    try:
        df = pd.read_csv('food_log.csv')
    except FileNotFoundError:
        print("Food log not found. Please log some food first.")
        return

    df['Calories'] = pd.to_numeric(df['Calories'])

    # Filter data for the specified date
    daily_data = df[df['Date'] == date]
    if daily_data.empty:
        print(f"No data found for {date}.")
        return

    # Group by meal type and sum calories
    meal_calories = daily_data.groupby('Meal')['Calories'].sum()

    # Create the plot
    plt.figure(figsize=(8, 8))
    plt.pie(meal_calories, labels=meal_calories.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(f'Calorie Breakdown for {date}')
    plt.axis('equal')  # Equal aspect ratio ensures the pie is circular.
    plt.show()


if __name__ == "__main__":
    plot_weekly_calories()
    plot_daily_breakdown("2025-08-12")
