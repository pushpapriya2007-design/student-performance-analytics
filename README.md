# Student Performance Analytics System

# Name:PUSHPAPRIYA M G 

# Degree and College: B.Tech CSE-AIML,HITS,Chennai

# Course: Python with AI – EWB Courses

# Objective
To read student marks from a CSV file and analyse them using Python, NumPy and Pandas. The program finds each student's total, average, grade and result, and shows the top performers and subject-wise performance.

# Technologies Used
- Python 3
- NumPy
- Pandas
- VS Code, Git and GitHub

# Dataset
`students.csv` has 20 student records with these columns: Student_ID, Name, Department, Python, Maths, Physics, English, Data_Structures, Attendance.

# How It Works
1. Load the CSV file into a Pandas DataFrame and check its size and columns.
2. Calculate each student's total and average using NumPy.
3. Give a grade using a function and a loop
4. Find the result: a student passes only if they score 50 or more in every subject.
5. Analyse the data:
   - class average, highest and lowest average
   - number of students who passed and failed
   - subject-wise average, highest and lowest marks
   - top 5 students
   - department-wise average and low attendance students
6. Save the final table to `student_results.csv`.

# Functions Used
- `assign_grade()` – gives a grade from the average
- `check_result()` – gives Pass or Fail for one student
- `get_top_students()` – returns the top n students

# Final Outcome
- 16 of 20 students passed (80%).
- Kavya Shree (CSE) is the top performer with an average of 95.8.
- English is the strongest subject and Maths the weakest.
- CSE has the best department average (85.23) and MECH the lowest (52.33).
- The 4 students with low attendance are the same 4 who failed.

## Challenges & Learning
The student faced a few challenges while doing this project. Some errors occurred in VS Code, such as unsaved files and indentation mistakes, and they were fixed by reading the error messages. Understanding `axis=1` in NumPy was also difficult at first.
Through this project, the student learned how to use Pandas and NumPy to analyse data, and how to use loops and functions. The student also learned to use Git and GitHub to submit the project.

# GitHub Repository
https://github.com/pushpapriya2007-design/student-performance-analytics
