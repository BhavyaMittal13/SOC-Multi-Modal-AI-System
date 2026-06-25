# Creating a list
subjects = ["Maths", "Physics", "Chemistry", "CS", "English", "PE"]
marks = [88, 92, 75, 95, 80, 70]

print("Subjects:", subjects)
print("Marks:", marks)

#  Accessing elements 
print("\nFirst subject:", subjects[0])    
print("Last subject:", subjects[-1])      
print("Third subject:", subjects[2])

#  Slicing 
print("\nFirst three subjects:", subjects[0:3])
print("Last two subjects:", subjects[-2:]) 

#  Modifying a list 
marks[5] = 85  # updating PE marks
print("\nUpdated PE marks:", marks[5])

#  Adding elements 
subjects.append("Biology")
marks.append(78)
print("\nAfter adding Biology:", subjects)

#  Removing elements 
subjects.remove("PE")   # removes by value
marks.pop(5)            # removes by index (index 5 was PE's mark)
print("After removing PE:", subjects)
print("Marks after removal:", marks)

#  Useful list operations 
print("\n List Operations ")
print("Length:", len(marks))
print("Max marks:", max(marks))
print("Min marks:", min(marks))
print("Sum of marks:", sum(marks))
print("Average:", sum(marks) / len(marks))  

#  Sorting 
sorted_marks = sorted(marks)  # sorted() returns a new list
print("Sorted marks:", sorted_marks)
print("Original still:", marks)   # still same order

marks.sort(reverse=True)  # sort() changes the list in-place, reverse=True for descending
print("Sorted descending:", marks)

#  Looping through a list 
print("\n Looping through subjects ")
for subject in subjects:
    print(" -", subject)

# Loop with index using enumerate
print("\n With index ")
for i, subject in enumerate(subjects):
    print(f"  {i+1}. {subject}") 

#  List comprehension
high_scores = [m for m in marks if m >= 85]
print("\nMarks above 85:", high_scores)

squared = [x**2 for x in [1, 2, 3, 4, 5]]
print("Squares of 1-5:", squared)



print("\n" + "="*40)
print("DICTIONARIES")
print("="*40)


student = {
    "name": "Bhavya",
    "roll_no": "22B1234",
    "branch": "Engineering",
    "cgpa": 8.75,
    "year": 2,
    "hostel": "H4"
}

print("\nStudent info:", student)
print("Name:", student["name"])
print("CGPA:", student["cgpa"])


#  Modifying and adding 
student["cgpa"] = 9.0    
student["phone"] = "98XXXXXXXX" 
print("\nUpdated student:", student)

#  Removing 
del student["phone"]
print("After deleting phone:", student)

#  Looping through dictionary 
print("\n Student Details ")
for key, value in student.items():
    print(f"  {key}: {value}")

#  Dictionary of student marks 
class_marks = {
    "Alice": 91,
    "Bob": 74,
    "Charlie": 88,
    "Diana": 95,
    "Eve": 62
}

print("\nClass marks:", class_marks)
print("Keys (student names):", list(class_marks.keys()))
print("Values (marks):", list(class_marks.values()))

# Find the highest scoring student
# max() with key parameter
topper = max(class_marks, key=class_marks.get)
print(f"\nTopper: {topper} with {class_marks[topper]} marks")

#  Nested dictionary 
student_records = {
    "S001": {"name": "Alice", "marks": 91, "grade": "A"},
    "S002": {"name": "Bob", "marks": 74, "grade": "B"},
    "S003": {"name": "Charlie", "marks": 88, "grade": "A"},
}

print("\n Student Records ")
for roll, info in student_records.items():
    print(f"  Roll {roll}: {info['name']} — {info['marks']} marks ({info['grade']})")

#  Checking if key exists 
if "S001" in student_records:
    print("\nS001 found:", student_records["S001"]["name"])
