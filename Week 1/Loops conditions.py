
print("="*40)
print("CONDITIONAL STATEMENTS")
print("="*40)

#  if / elif / else 
marks = 73

if marks >= 90:
    grade = "O"   # Outstanding hehe
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"   

print(f"Marks: {marks} → Grade: {grade}")

#  Chained comparisons 
x = 55
if 50 <= x <= 60:
    print(f"{x} is between 50 and 60")

#  Logical operators: and, or, not 
age = 20
has_id = True

if age >= 18 and has_id:
    print("Eligible to vote")

if age < 13 or age > 60:
    print("Special category")
else:
    print("Regular category")

#  Ternary (one-line if-else) 
result = "Pass" if marks >= 40 else "Fail"
print(f"Result: {result}")




print("\n" + "="*40)
print("FOR LOOPS")
print("="*40)


print("\nrange(5) gives:")
for i in range(5):
    print(i, end=" ")
print()  # newline

# range(start, stop, step)
print("\nOdd numbers from 1 to 9:")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

print("\nCountdown:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("Go!")

#  Looping over a list 
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruits:")
for fruit in fruits:
    print(f"  - {fruit}")

#  Nested for loop 
# Multiplication table
print("\n Multiplication Table (3x3) ")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:3}", end="")  # :3 pads to width 3 for alignment
    print()

#  for loop with enumerate 
students = ["Alice", "Bob", "Charlie"]
print("\n Roll Numbers ")
for idx, name in enumerate(students, start=1):
    print(f"  Roll {idx}: {name}")

#  for loop with zip (two lists at once) 
names = ["Alice", "Bob", "Charlie"]
scores = [91, 74, 88]

print("\n Score Report ")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")



print("\n" + "="*40)
print("WHILE LOOPS")
print("="*40)

#  Basic while loop 
count = 1
print("\nCounting to 5:")
while count <= 5:
    print(count, end=" ")
    count += 1   # IMPORTANT: always update the counter or it loops forever!
print()

#  while loop with break 
print("\nSearch for first mark below 50:")
exam_marks = [88, 92, 73, 45, 80, 61]
i = 0
while i < len(exam_marks):
    if exam_marks[i] < 50:
        print(f"  Found at index {i}: {exam_marks[i]}")
        break
    i += 1

#  while loop with continue 
print("\nPrint only even numbers from 1 to 10:")
n = 0
while n < 10:
    n += 1
    if n % 2 != 0:
        continue   # skip odd numbers
    print(n, end=" ")
print()



print("\n" + "="*40)
print("BREAK, CONTINUE, PASS")
print("="*40)

# break
print("\nbreak example:")
for i in range(1, 11):
    if i == 6:
        print("  Stopped at 6!")
        break
    print(i, end=" ")
print()

# continue
print("\ncontinue example (skip multiples of 3):")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# pass
for i in range(5):
    if i == 3:
        pass  
    else:
        print(i, end=" ")
print()

# PRACTICAL EXAMPLE
print("\n" + "="*40)
print("GRADE SUMMARY FOR CLASS")
print("="*40)

class_scores = [55, 90, 43, 78, 82, 36, 91, 65, 50, 88]
grade_count = {"O": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for score in class_scores:
    if score >= 90:
        grade_count["O"] += 1
    elif score >= 75:
        grade_count["A"] += 1
    elif score >= 60:
        grade_count["B"] += 1
    elif score >= 50:
        grade_count["C"] += 1
    elif score >= 40:
        grade_count["D"] += 1
    else:
        grade_count["F"] += 1

print("\nGrade Distribution:")
for grade, count in grade_count.items():
    print(f"  {grade}: {'█' * count} ({count})")

print(f"\nClass average: {sum(class_scores)/len(class_scores):.2f}")
print(f"Pass percentage: {sum(1 for s in class_scores if s >= 40) / len(class_scores) * 100:.1f}%")
