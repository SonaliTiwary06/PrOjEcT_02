
# 🍽️ Daily Diet Log Analyzer (Python + Visualization)

A Python-based tool to **log daily meals**, track **calorie intake**, and visualize **weekly trends** using **Pandas** and **Matplotlib**.  
Perfect for anyone who wants to monitor their eating habits and stay on track with fitness goals.



## 📌 Features

- 📝 Log daily food entries (meal type, food name, calories)
- 💾 Automatically save entries to a CSV file
- 📊 Calculate total calories per day
- 🥗 Pie chart for **meal-type calorie split**
- 📅 Weekly bar chart for **calorie trends**
- 🚀 Works offline and requires no external database



## 🛠️ Technologies Used

- **Python 3**
- **Pandas** → Data handling and analysis
- **Matplotlib** → Data visualization
- **CSV module** → File storage



## 📂 Project Structure

Daily-Diet-Log-Analyzer/
│
├── food\_log.py        # Script to log daily food entries
├── food\_tracker.py    # Script to view charts & calorie totals
├── food\_log.csv       # Auto-generated food data file
└── README.md          # Project documentation





## 🚀 How to Run

### 1️⃣ Install required libraries

pip install pandas matplotlib


### 2️⃣ Log a food entry
python food_log.py

Example prompt:

Enter date (YYYY-MM-DD, press enter for today): 
Enter meal type (e.g., Breakfast, Lunch, Dinner, Snack): Lunch
Enter food item: Rice
Enter calories: 450
Food entry logged successfully!


### 3️⃣ View calorie trends & breakdown

python food_tracker.py

* **Weekly Calorie Trend** → Bar chart of total daily calories
* **Daily Meal Breakdown** → Pie chart of calorie share by meal type


## 📊 Example Outputs

### **Weekly Calorie Trend**

![Weekly Calorie Chart][(screenshots/weekly_chart.png)](https://github.com/SonaliTiwary06/PrOjEcT_02/blob/main/Bar-chart%202025-08-13%20103009.png)

### **Daily Meal Breakdown**

![Meal Pie Chart](screenshots/pie_chart.png)



## 📌 Future Improvements

* Add BMI and daily calorie goal tracking
* GUI interface using Tkinter or PyQt
* Export charts as PNG/JPEG



## 👩‍💻 Author

**Sonali**
📧 Email: [sonai.dtg1@gmail.com](mailto:sonai.dtg1@gmail.com)
📍 India



## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify.



