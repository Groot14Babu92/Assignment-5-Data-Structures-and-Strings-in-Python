student_data = {
    "Alice": 59,
    "Bob": 75,
    "Charlie": 82,
    "David": 90,
    "Eve": 67,
    "Frank": 88,
    "Grace": 95,
    "Hannah": 72}

name = input("Enter the name of the student: ")
if name in student_data:
    print(f"{name}'s mark is {student_data[name]}")
else:
    print(f"Student {name} not found in the records.")
