import pandas as pd
import matplotlib.pyplot as plt

# 4.1 Create & clean data

# Example dataset: 8 students, marks in 3 subjects
student_data = {
    "Student": ["Aarav", "Bhavya", "Charan", "Deepa",
                "Emma", "Farhan", "Gita", "Hari"],
    "Maths":   [78, 92, 65, 88, 73, 85, 91, 69],
    "Science": [81, 89, 70, 90, 76, 80, 95, 72],
    "English": [74, 86, 68, 84, 79, 82, 88, 71]
}
students_df = pd.DataFrame(student_data)

# Calculate total and average marks
subject_cols = ["Maths", "Science", "English"]
students_df["Total"] = students_df[subject_cols].sum(axis=1)
students_df["Average"] = students_df[subject_cols].mean(axis=1)

# Grade based on average
def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

students_df["Grade"] = students_df["Average"].apply(get_grade)

print("Student performance data:")
print(students_df)
print()


# 4.2 Basic numeric analysis

print("Overall statistics (per subject and total):")
print(students_df[subject_cols + ["Total", "Average"]].describe())
print()

# Average score per subject
subject_means = students_df[subject_cols].mean()
print("Average marks per subject:")
print(subject_means)
print()

# Best and weakest student by total
best_student = students_df.loc[students_df["Total"].idxmax(), "Student"]
worst_student = students_df.loc[students_df["Total"].idxmin(), "Student"]

print(f"Best overall student (by total marks): {best_student}")
print(f"Weakest overall student (by total marks): {worst_student}")
print()


# 4.3 Chart Type 1 – Bar chart
#     Average marks per subject

plt.figure(figsize=(8, 5))
plt.bar(subject_means.index, subject_means.values)
plt.title("Average Marks per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()


# 4.4 Chart Type 2 – Line chart
#     Total marks of each student

plt.figure(figsize=(8, 5))
plt.plot(students_df["Student"], students_df["Total"], marker="o")
plt.title("Total Marks by Student")
plt.xlabel("Student")
plt.ylabel("Total Marks")
plt.ylim(0, 300)
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()


# 4.5 (Optional) Chart Type 3 – Pie chart
#     Grade distribution

grade_counts = students_df["Grade"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    grade_counts.values,
    labels=grade_counts.index,
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Grade Distribution")
plt.tight_layout()
plt.show()


# 4.6 Text Insights (printed)

print("INSIGHTS FROM STUDENT PERFORMANCE ANALYSIS")
print("----------------------------------------")
print(f"• The subject with highest average marks is: {subject_means.idxmax()} "
      f"({subject_means.max():.2f} marks).")
print(f"• The subject with lowest average marks is: {subject_means.idxmin()} "
      f"({subject_means.min():.2f} marks).")
print(f"• {best_student} has the highest total marks among all students.")
print(f"• {worst_student} has the lowest total marks among all students.")
print("• Most students are in grade category/ies:",
      ", ".join(grade_counts.index.astype(str)), "based on average marks.")
print("• Overall, performance is good, but the weakest subject can be focused on for improvement.")