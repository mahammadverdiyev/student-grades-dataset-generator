import random
import pandas as pd
import numpy as np

subject_preferences = {
    'Freshman': ['Math', 'Biology', 'English'],
    'Sophomore': ['Math', 'Physics', 'English', 'History'],
    'Junior': ['Math', 'Biology', 'Physics', 'Advanced English'],
    'Senior': ['Calculus', 'Physics', 'History', 'Biology', 'English Literature']
}

student_names = [
    "Aynur", "Farid", "Gunel", "Ilkin", "Kamran",
    "Leyla", "Mahir", "Nigar", "Orkhan", "Ramil",
    "Rufat", "Samir", "Sevil", "Tural", "Vusala",
    "Yusif", "Aysel", "Rashad", "Sona", "Nijat",
    "Aida", "Shahin", "Gulnara", "Ramin", "Khadija"
]

grade_levels = {
    'Freshman': (14, 15),
    'Sophomore': (15, 16),
    'Junior': (16, 17),
    'Senior': (17, 18)
}

columns = ['Student ID', 'Name', 'Age', 'Grade Level', 'Subject', 'Grade', 'Attendance (%)', 'Extracurricular Activity',
           'GPA', 'Parental Education Level', 'Location']


def create_student_record(student_id):
    grade_level = random.choice(list(grade_levels.keys()))
    age_range = grade_levels[grade_level]
    age = random.randint(age_range[0], age_range[1])
    name = random.choice(student_names)

    parental_education = random.choice(['High School', 'Bachelor', 'Master', 'PhD'])

    location = random.choice(['Urban', 'Rural'])

    attendance = random.randint(70, 100)
    return name, age, grade_level, attendance, parental_education, location


# func to create random grade for a student
def create_grade(student_id):
    name, age, grade_level, attendance, parental_education, location = create_student_record(student_id)

    subject = random.choice(subject_preferences[grade_level])

    # here trying to simulate normal dist of grade based on attendance
    base_grade = int(np.random.normal(loc=75, scale=15))
    attendance_effect = (attendance - 70) / 30
    grade = max(min(base_grade + int(attendance_effect * 10), 100), 50)

    extracurricular_activity = random.choice(['Football', 'Debate Club', 'Music Band', 'None'])

    gpa = round(grade / 20, 2)

    return [student_id, name, age, grade_level, subject, grade, attendance, extracurricular_activity, gpa,
            parental_education, location]


def generate_grades_data(num_students):
    data = []
    for student_id in range(1, num_students + 1):
        for _ in range(random.randint(3, 5)):
            data.append(create_grade(student_id))
    return pd.DataFrame(data, columns=columns)


df = generate_grades_data(50)

# Adding some NaN values to make it look like realistic
for _ in range(5):
    df.loc[random.choice(df.index), 'Attendance (%)'] = np.nan

df.to_csv('student_grades_dataset.csv', index=False)
