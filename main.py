def second_lowest_grade(students):
    """Finds the second-lowest grade and prints the corresponding student names.

    Args:
        students: A nested list containing student names and their grades.
    """

    # Create a dictionary to store grades as keys and student names as values
    grade_dict = {}
    for name, grade in students:
        grade_dict.setdefault(grade, []).append(name)

    # Find the second-lowest grade
    grades = sorted(grade_dict.keys())
    second_lowest = grades[1]

    # Print the names of students with the second-lowest grade
    print(second_lowest)
    for name in sorted(grade_dict[second_lowest]):
        print(name)

# Example usage
students = [
    ["Harry", 37.21],
    ["Berry", 37.21],
    ["Tina", 37.2],
    ["Akash", 37.2],
]

second_lowest_grade(students)
