import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
total_students = len(data)

# Find the mean average GPA of the students
mean_gpa = data["GPA"].mean()

# Find the standard deviation of how much sleep students get per day
sleep_std = data["Sleep_Hours_Per_Day"].std()

# Find the maximum amount of study hours per day
max_study_hours = data["Study_Hours_Per_Day"].max()

# Sort the students by social hours per day ascending (lowest -> highest)
students_by_social_hours = data.sort_values("Social_Hours_Per_Day", ascending=True)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
hours_column = [
    "Study_Hours_Per_Day",
    "Sleep_Hours_Per_Day",
    "Social_Hours_Per_Day",
    "Physical_Activity_Hours_Per_Day"
]

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
high_stress_students = data[data["Stress_level"] == "High"]
low_stress_students = data[data[data["Stress_level"] == "Low"]]

# Can you work out whether having a higher stress level leads to a higher GPA?

# Compare average GPA by stress level
avg_gpa_by_stress = data.groupby("Stress_Level")["GPA"].mean()

#Print results
print("Total students:", total_students)
print("Mean GPA:", mean_gpa)
print("Sleep standard deviation:", sleep_std)
print("Max study hours:", max_study_hours)
print(students_by_social_hours[["GPA", "Social_Hours_Per_Day"]].head())
print(data[["Total_hours"]].head())
print("High stress avg GPA:", high_stress_students["GPA"].mean())
print("Low stress avg GPA:", low_stress_students["GPA"].mean())
print(avg_gpa_by_stress)