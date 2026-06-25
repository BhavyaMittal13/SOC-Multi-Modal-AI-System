
#  Defining a simple function 
def greet():
    print("Hello! Welcome to ML SOC.")

greet()   # Call the function

#  Function with parameters 
def greet_student(name):
    print(f"Hello, {name}! Hope your SOC is going well.")

greet_student("Bhavya")
greet_student("Alice")

#  Function with return value 
def add(a, b):
    return a + b

result = add(10, 25)
print(f"\n10 + 25 = {result}")

#  The difference between print and return 
def square_with_print(n):
    print(n * n)       # just displays, nothing comes back

def square_with_return(n):
    return n * n       # sends the value back to caller

# With print — can't use the result in a calculation
square_with_print(5)   # displays 25

# With return — can use the result
val = square_with_return(5)
print(f"Square + 10 = {val + 10}")  # works! prints 35

#  Default parameter values 
def introduce(name, role="student", college="IIT Bombay"):
    print(f"Hi, I'm {name}, a {role} at {college}.")

introduce("Bhavya")
introduce("Prof. Sharma", "professor")
introduce("Ali", "researcher", "IIT Delhi")

# ============================
# PART 2: FUNCTIONS FOR ML-STYLE CALCULATIONS
# ============================

print("\n" + "="*40)
print("CALCULATION FUNCTIONS")
print("="*40)

def calculate_average(marks_list):
    """
    Calculate the average of a list of marks.
    
    Parameters:
        marks_list (list): list of numerical marks
    
    Returns:
        float: the average value
    """
    if len(marks_list) == 0:
        return 0   # avoid division by zero
    return sum(marks_list) / len(marks_list)

def find_topper(students_dict):
    """
    Find the student with the highest marks.
    
    Parameters:
        students_dict (dict): {name: marks}
    
    Returns:
        tuple: (name, marks) of the topper
    """
    topper_name = max(students_dict, key=students_dict.get)
    return topper_name, students_dict[topper_name]

def assign_grade(marks):
    """
    Assign a letter grade based on marks.
    
    Parameters:
        marks (int or float): the score
    
    Returns:
        str: the grade (O, A, B, C, D, F)
    """
    if marks >= 90:
        return "O"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

# Testing our functions
sample_marks = [88, 92, 75, 95, 80, 70]
avg = calculate_average(sample_marks)
print(f"\nMarks: {sample_marks}")
print(f"Average: {avg:.2f}")

students = {"Alice": 91, "Bob": 74, "Charlie": 88, "Diana": 95}
topper, top_marks = find_topper(students)
print(f"\nTopper: {topper} ({top_marks} marks)")

for name, score in students.items():
    print(f"  {name}: {score} → Grade {assign_grade(score)}")

# PART 3: MULTIPLE RETURN VALUES

print("\n" + "="*40)
print("MULTIPLE RETURN VALUES")
print("="*40)

def get_stats(data):
    """Return min, max, average of a list."""
    return min(data), max(data), sum(data) / len(data)

data = [55, 90, 43, 78, 82, 36, 91, 65, 50, 88]
minimum, maximum, average = get_stats(data)   # unpacking
print(f"\nData: {data}")
print(f"Min: {minimum}, Max: {maximum}, Average: {average:.2f}")

# PART 4: SCOPE

print("\n" + "="*40)
print("VARIABLE SCOPE")
print("="*40)

# Variables inside a function are LOCAL — they don't exist outside
def demo_scope():
    local_var = "I only exist inside this function"
    print(local_var)

# Global variables can be read inside functions
global_msg = "I exist everywhere"

def read_global():
    print(global_msg)  # can read it

read_global()


# Common use: sorting with custom key
students_list = [("Alice", 91), ("Bob", 74), ("Charlie", 88)]
sorted_by_marks = sorted(students_list, key=lambda s: s[1], reverse=True)
print("\nRanking by marks:")
for rank, (name, score) in enumerate(sorted_by_marks, 1):
    print(f"  {rank}. {name}: {score}")
