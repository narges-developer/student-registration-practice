# ===========================================
# Project: Student Registration System
#
# Description:
# This program simulates a simple student
# registration system using different
# Python data structures.
#
# Concepts Used:
# - Variables
# - Lists
# - Dictionaries
# - Sets
# - Tuples
# - Indexing
# - for loops
# - append()
# - set.add()
# - print()
# ===========================================
students = [
    {
        "name": "Ali",
        "age": 20,
        "courses": {"Python", "Math"},
        "scores": (18, 15)
    },
    {
        "name": "Sara",
        "age": 19,
        "courses": {"Python", "English"},
        "scores": (20, 19)
    }
]
print("---------------------------")
print("The name of the first student: ",students[0]["name"])
print("The second student's age: ",students[1]["age"])
print("The first student's courses: ",students[0]["courses"])
print("The second student's top grade: ",students[1]["scores"][0])
students[0]["courses"].add("English")
students.append({
        "name": "Nares",
        "age": 19,
        "courses": {"Python", "Japanese"},
        "scores": (20, 18)
    })
print("---------------------------")
for info in students:
    print("Student: ",
          " Name: ",info["name"],
          " Age: ",info["age"],
          " Courses: ",info["courses"],
          " Scores: ",info["scores"]
          )