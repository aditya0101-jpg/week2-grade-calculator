# Student Grade Calculator

# Function to validate marks (0–100)
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent"
    elif avg >= 80:
        return "B", "Very Good"
    elif avg >= 70:
        return "C", "Good"
    elif avg >= 60:
        return "D", "Needs Improvement"
    else:
        return "F", "Failed"


# Main program
def main():
    students = []
    averages = []

    try:
        n = int(input("Enter number of students: "))
    except ValueError:
        print("Invalid number!")
        return

    for i in range(n):
        print(f"\nStudent {i+1}")
        name = input("Enter student name: ")

        math = get_valid_marks("Math")
        science = get_valid_marks("Science")
        english = get_valid_marks("English")

        avg = (math + science + english) / 3
        grade, comment = calculate_grade(avg)

        students.append([name, math, science, english, avg, grade, comment])
        averages.append(avg)

    # Display Results
    print("\n--- Student Results ---")
    print(f"{'Name':<10}{'Math':<10}{'Science':<10}{'English':<10}{'Avg':<10}{'Grade':<10}{'Comment'}")

    for s in students:
        print(f"{s[0]:<10}{s[1]:<10}{s[2]:<10}{s[3]:<10}{round(s[4],2):<10}{s[5]:<10}{s[6]}")

    # Class Statistics
    print("\n--- Class Statistics ---")
    print("Class Average:", round(sum(averages)/len(averages), 2))
    print("Highest Score:", round(max(averages), 2))
    print("Lowest Score:", round(min(averages), 2))


# Run program
main()