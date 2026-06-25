# This is my first proper Python project!
# It stores student marks, calculates averages,
# finds the topper, and displays grades for each student.
# I tried to use everything I learned this week.


# STUDENT DATA


# Using a list of dictionaries — each dict represents one student
# (I first tried using two separate lists for names and marks,
#  but that got messy. Dicts are cleaner.)

students = [
    {"name": "Alice",   "roll": "101", "marks": [88, 92, 75, 80, 91]},
    {"name": "Bob",     "roll": "102", "marks": [55, 60, 48, 72, 58]},
    {"name": "Charlie", "roll": "103", "marks": [95, 98, 90, 92, 97]},
    {"name": "Diana",   "roll": "104", "marks": [40, 38, 45, 50, 42]},
    {"name": "Eve",     "roll": "105", "marks": [70, 75, 68, 80, 74]},
    {"name": "Frank",   "roll": "106", "marks": [30, 25, 35, 40, 28]},
]

subjects = ["Maths", "Physics", "Chemistry", "CS", "English"]
TOTAL_MARKS_PER_SUBJECT = 100


# HELPER FUNCTIONS

def calculate_average(marks_list):
    """Return the average of a list of marks."""
    return sum(marks_list) / len(marks_list)

def calculate_percentage(marks_list, max_per_subject=100):
    """Return percentage score out of total possible marks."""
    total_obtained = sum(marks_list)
    total_possible = max_per_subject * len(marks_list)
    return (total_obtained / total_possible) * 100

def assign_grade(percentage):
    """
    Assign letter grade based on percentage.
    Using IIT-style grading (approximate):
      O  = Outstanding (>=90)
      A+ = Excellent   (>=80)
      A  = Very Good   (>=70)
      B  = Good        (>=60)
      C  = Average     (>=50)
      D  = Marginal    (>=40)
      F  = Fail        (<40)
    """
    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def get_status(grade):
    """Return Pass or Fail based on grade."""
    return "FAIL" if grade == "F" else "PASS"

def find_topper(students_data):
    """Return the student with the highest average marks."""
    best = None
    best_avg = -1
    for student in students_data:
        avg = calculate_average(student["marks"])
        if avg > best_avg:
            best_avg = avg
            best = student
    return best, best_avg

def find_weakest_subject(marks_list, subjects_list):
    """Return the subject in which the student scored least."""
    min_idx = marks_list.index(min(marks_list))
    return subjects_list[min_idx], min(marks_list)


# MAIN PROGRAM


def display_report():
    """Display the full marks report for all students."""
    
    print("=" * 65)
    print("       STUDENT MARKS REPORT - SEMESTER 1")
    print("=" * 65)
    print(f"{'Roll':<6} {'Name':<10} {'Avg':>6} {'%':>7} {'Grade':>6} {'Status':>7}")
    print("-" * 65)
    
    all_averages = []
    
    for student in students:
        avg = calculate_average(student["marks"])
        pct = calculate_percentage(student["marks"])
        grade = assign_grade(pct)
        status = get_status(grade)
        
        all_averages.append(avg)
        
        # Format output neatly
        print(f"{student['roll']:<6} {student['name']:<10} {avg:>6.2f} {pct:>6.1f}% {grade:>6} {status:>7}")
    
    print("-" * 65)
    
    # Class average
    class_avg = sum(all_averages) / len(all_averages)
    print(f"\n{'Class Average:':<20} {class_avg:.2f}")
    
    # Pass/Fail count
    pass_count = sum(1 for s in students
                     if get_status(assign_grade(calculate_percentage(s["marks"]))) == "PASS")
    print(f"{'Students Passed:':<20} {pass_count}/{len(students)}")
    print(f"{'Pass Percentage:':<20} {pass_count/len(students)*100:.1f}%")

def display_topper():
    """Display information about the class topper."""
    topper, top_avg = find_topper(students)
    pct = calculate_percentage(topper["marks"])
    
    print("\n" + "=" * 65)
    print("  🏆  TOPPER OF THE CLASS")
    print("=" * 65)
    print(f"  Name   : {topper['name']}")
    print(f"  Roll   : {topper['roll']}")
    print(f"  Average: {top_avg:.2f}")
    print(f"  Total  : {sum(topper['marks'])}/{TOTAL_MARKS_PER_SUBJECT * len(subjects)}")
    print(f"  Grade  : {assign_grade(pct)}")
    print(f"\n  Subject-wise breakdown:")
    for subj, mark in zip(subjects, topper["marks"]):
        print(f"    {subj:<12}: {mark}")

def display_detailed_report():
    """Display detailed per-student subject breakdown."""
    print("\n" + "=" * 65)
    print("  DETAILED SUBJECT-WISE REPORT")
    print("=" * 65)
    
    for student in students:
        avg = calculate_average(student["marks"])
        pct = calculate_percentage(student["marks"])
        grade = assign_grade(pct)
        weak_subj, weak_score = find_weakest_subject(student["marks"], subjects)
        
        print(f"\n  [{student['roll']}] {student['name']} — Grade: {grade}")
        for subj, mark in zip(subjects, student["marks"]):
            bar = "█" * (mark // 10)  # visual bar
            print(f"    {subj:<12}: {mark:>3}  {bar}")
        print(f"    {'Average':<12}: {avg:.2f}")
        print(f"    Needs work in: {weak_subj} ({weak_score} marks)")

def display_grade_distribution():
    """Show how many students got each grade."""
    print("\n" + "=" * 65)
    print("  GRADE DISTRIBUTION")
    print("=" * 65)
    
    grade_count = {}
    for student in students:
        pct = calculate_percentage(student["marks"])
        grade = assign_grade(pct)
        grade_count[grade] = grade_count.get(grade, 0) + 1
    
    grade_order = ["O", "A+", "A", "B", "C", "D", "F"]
    for g in grade_order:
        count = grade_count.get(g, 0)
        if count > 0:
            bar = "■" * count
            print(f"  {g:<4}: {bar} ({count})")


if __name__ == "__main__":
    display_report()
    display_topper()
    display_detailed_report()
    display_grade_distribution()

