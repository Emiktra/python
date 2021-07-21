student_table ={'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, 
'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, 
'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, 
'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, 
'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}

def Student_avg(student_table):
    grade_table = {}
    for student in student_table.keys():
        avg_grade = 0
        for i in range(len(student_table['Student-1'])):
            avg_grade += student_table[student][f'Lesson-{i +1}']
        avg_grade = avg_grade/len(student_table['Student-1'].values())
        grade_table[f"{student}"] = avg_grade
    return grade_table

def Lowest_avg(table):
    lowest = [101, None]
    for i in range(1, len(table) + 1):
        if table[f"Student-{i}"] < lowest[0]: lowest = [table[f"Student-{i}"], f"Student-{i}"]
    return lowest
        

def Highest_avg(table):
    highest = [0, None]
    for i in range(1, len(table) +1):
        if table[f"Student-{i}"] > highest[0]: highest = [table[f"Student-{i}"], f"Student-{i}"]
    return highest

#flow
lowest_avg = Lowest_avg(Student_avg(student_table))
highest_avg = Highest_avg(Student_avg(student_table))
print(f"The highest average belongs to {highest_avg[1]} with the average score of {highest_avg[0]}")
print(f"The lowest average belongs to {lowest_avg[1]} with the average score of {lowest_avg[0]}")

#proud of this one. Very clean logic. Except you can literally do this with 1-3 lines of code :(