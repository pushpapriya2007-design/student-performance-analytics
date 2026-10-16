# import pandas and numpy libraries
import pandas as pd
import numpy as np
pd.set_option('display.width', 200)
#load the dataset
df=pd.read_csv('students.csv')
#first five rows of the dataset
print(df.head())
#display the size of the dataset
print(df.shape)
#display the column names of the dataset
print(df.columns)
#display the data types and missing values of the dataset
print(df.info())
#list of subjects columns
subjects = ["Python", "Maths", "Physics", "English", "Data_Structures"]
#covert the sujects marks into numpy array
marks = df[subjects].to_numpy() 
#calculate total and average for each student                                              
df['Total'] = np.sum(marks, axis=1)
df['Average'] = np.mean(marks, axis=1)
print(df[["Name", "Total", "Average"]])
#function to give grade based on average marks
def assign_grade(avg):
    if avg >= 90:
        return '0'
    elif avg >= 80:
        return 'A+'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'
#use a loop to find the grade for each student
grades = []
for avg in df['Average']:
    grades.append(assign_grade(avg))
df["Grade"] = grades
print(df[["Name", "Average", "Grade"]])
#minimum marks in each subject to pass
#minimum marks needed in every subject to pass
pass_mark = 50
#function to check pass or fail for one student
def check_result(student_marks, pass_mark):
    if np.all(student_marks >= pass_mark):
        return "Pass"
    else:
        return "Fail"
#use a loop to check the result of each student
results = []
for i in range(len(df)):
    results.append(check_result(marks[i], pass_mark))
df["Result"] = results
print(df[["Name", "Average", "Grade", "Result"]])
#overall class average using numpy
class_avg = np.mean(df["Average"])
print("Overall class average:", round(class_avg, 2))
#student with the highest and lowest average
best = df.loc[df["Average"].idxmax()]
worst = df.loc[df["Average"].idxmin()]
print("Highest average:", best["Name"], "-", best["Average"])
print("Lowest average:", worst["Name"], "-", worst["Average"])
#count of students who passed and failed
passed = (df["Result"] == "Pass").sum()
failed = (df["Result"] == "Fail").sum()
print("Students passed:", passed)
print("Students failed:", failed)
#subject wise analysis: average, highest and lowest marks
print("\nSubject-wise analysis")
for sub in subjects:
    print(sub, "- Average:", round(df[sub].mean(), 2),
          "| Highest:", df[sub].max(),
          "| Lowest:", df[sub].min())
#subject with the best and weakest average
subject_avg = df[subjects].mean()
print("Best subject:", subject_avg.idxmax())
print("Weakest subject:", subject_avg.idxmin())
#function to get the top n students by average
def get_top_students(data, n):
    return data.sort_values("Average", ascending=False).head(n)
top5 = get_top_students(df, 5)
print("\nTop 5 performers")
print(top5[["Name", "Department", "Average", "Grade"]])
#department wise average marks and attendance
print("\nDepartment-wise analysis")
print(df.groupby("Department")[["Average", "Attendance"]].mean().round(2))
#students with low attendance (below 75%)
print("\nLow attendance students")
low_attendance = df[df["Attendance"] < 75]
print(low_attendance[["Name", "Attendance", "Average"]])
#save the final results to a new csv file
df.to_csv("student_results.csv", index=False)
print("\nResults saved to student_results.csv")