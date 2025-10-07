### ACTIVITY NO. 1 ###

# ROUND OFF A NUMBER TO 2 DECIMAL PLACES
def grade_conversion (raw_grade : float):
    
    grade_equivalents = (
        {"grade_point": 1.00, "min_range": 97, "max_range": 100},
        {"grade_point": 1.25, "min_range": 94, "max_range": 96.99},
        {"grade_point": 1.50, "min_range": 91, "max_range": 93.99},
        {"grade_point": 1.75, "min_range": 88, "max_range": 90.99},
        {"grade_point": 2.00, "min_range": 85, "max_range": 87.99},
        {"grade_point": 2.25, "min_range": 82, "max_range": 84.99},
        {"grade_point": 2.50, "min_range": 79, "max_range": 81.99},
        {"grade_point": 2.75, "min_range": 76, "max_range": 78.99},
        {"grade_point": 3.00, "min_range": 75, "max_range": 75.99},
        {"grade_point": 5.00, "min_range": 0,  "max_range": 74.99},
    )
    
    try:
        raw_grade = round(float(user_input), 2)
        res = None

        for grade in grade_equivalents:
            if grade.get("min_range", 0) <= raw_grade <= grade.get("max_range", 0):
                res = grade.get('grade_point', 0)
                    
        if res is not None:
            print(f"Equivalent Grade Point (GPA): {res}")
        else:
            print("Raw grade is out of bounds.")
        
    except ValueError:
         print("Invalid input: Grade must be a number.")    
    
# ROUND DOWN
def grade_conversion_ver2 (raw_grade : float):

    grade_equivalents = {
        1.00 : (97, 100),
        1.25: (94, 97),
        1.50 : (91, 94),
        1.75 : (88, 91),
        2.00 : (85, 88),
        2.25 : (82, 85),
        2.50 : (79, 82),
        2.75 : (76, 79),
        3.00 : (75, 76),
        5.00 : (0, 75),
    }
    
    try:
        raw_grade = float(raw_grade)
        res = None

        for grade_point_str, (min_range, max_range) in grade_equivalents.items():
            if min_range <= raw_grade < max_range:
                res = grade_point_str
                break
        
        if res is not None:
            print(f"Equivalent Grade Point (GPA): {res}")
        else:
            print("Raw grade is out of bounds.")
    except ValueError:
        print("Invalid input: Grade must be a number.")

    
user_input = input("Enter Raw Grade : ")
grade_conversion(user_input);