#  Integers 
age = 20
year = 2025
num_subjects = 6

print("Age:", age)
print("Year:", year)
print("Number of subjects:", num_subjects)

#  Floats (decimal numbers) 
pi = 3.14159
temperature = 36.6
cgpa = 8.75

print("\nPi:", pi)
print("Temperature:", temperature)
print("CGPA:", cgpa)

#  Strings 
name = "Bhavya"
department = "Engineering"
college = "IIT Bombay"

print("\nName:", name)
print("Department:", department)
print("College:", college)

# combining strings using +
greeting = "Hello, " + name + "!"
print(greeting)

#  Booleans 
is_enrolled = True
has_paid_fees = False

print("\nEnrolled:", is_enrolled)
print("Fees paid:", has_paid_fees)

#  Checking the type of a variable 
print("\n type() checks ")
print(type(age))
print(type(cgpa))
print(type(name))          
print(type(is_enrolled))   

#  Basic Arithmetic 
a = 15
b = 4

print("\n Arithmetic ")
print("Addition:", a + b)        # 19
print("Subtraction:", a - b)     # 11
print("Multiplication:", a * b)  # 60
print("Division:", a / b)        # 3.75  (always gives float)
print("Floor Division:", a // b) # 3     (integer part only)
print("Remainder:", a % b)       # 3     (modulo)
print("Power:", a ** b)          # 50625 (15^4)

#  String operations 
sentence = "machine learning is fun"

print("\n String Operations ")
print("Uppercase:", sentence.upper())
print("Length:", len(sentence))
print("Replace:", sentence.replace("fun", "challenging but rewarding"))

# String indexing
word = "Python"
print("First char:", word[0])   # P
print("Last char:", word[-1])   # n  (negative index goes from the end)

#  Multiple assignment 
x, y, z = 10, 20, 30
print("\nMultiple assignment:", x, y, z)

#  Constants (by convention, use ALL_CAPS) 
# Python doesn't enforce constants but it's a naming convention
MAX_MARKS = 100
PASSING_MARKS = 40
print("\nMax marks:", MAX_MARKS)
print("Passing marks:", PASSING_MARKS)
