def gradingStudents(grades):
    rounded_grades = []  # List to store final grades

    for grade in grades:
        if grade < 38:  # No rounding for failing grades
            rounded_grades.append(grade)
        else:
            lower = (grade // 5) * 5  # Lower multiple of 5
            upper = lower + 5  # Next multiple of 5
            
            # If the difference is less than 3, round up
            if (upper - grade) < 3:
                rounded_grades.append(upper)
            else:
                rounded_grades.append(grade)

    return rounded_grades  # Return the modified grades

# Example usage:
grades = [73, 67, 38, 33]
print(gradingStudents(grades))  # Output: [75, 67, 40, 33]
