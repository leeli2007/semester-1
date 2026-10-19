# Week 4, Session 1: Task 3

# You are given function calculate_grade and a docstring.
# Your task is to write the body of the function based on the
# details in the docstring


def calculate_grade(marks):
    """
    This function returns a grade based on the provided mark, according to
    the following grading scale:

    Grading Rules:
    - Marks < 50: Grade is 'F'
    - Marks >= 50 and < 60: Grade is 'D'
    - Marks >= 60 and < 70: Grade is 'C'
    - Marks >= 70 and < 80: Grade is 'B'
    - Marks >= 80: Grade is 'A'

    Validity Checks:
    - Returns `None` if `marks` is not a valid positive integer between
      0 and 100 (inclusive)
    - Returns `None` if `marks` is greater than 100, as it falls outside
      the valid range

    Args:
        marks (int): A positive integer representing the student's marks.
        Valid range is 0 to 100 (inclusive)

    Returns:
        str: The grade corresponding to the marks ('A', 'B', 'C', 'D', 'F').
        None: If `marks` is not a valid integer or is outside the allowed
              range (greater than 100 or negative)
    """

    if marks.is_integer() == False:
      return None
    
    if marks > 100 or marks < 0:
      return None

    match marks:
      case x if x >= 80:
        return 'A'

      case x if x >= 70 and x < 80:
        return 'B'
      
      case x if x >= 60 and x < 70:
        return 'C'
      
      case x if x >= 50 and x < 60:
        return 'D'
    
      case x if x < 50:
        return 'F'
  

# Check if the following tests produce the correct output
print(calculate_grade(39))
print(calculate_grade(55))
print(calculate_grade(-20))
print(calculate_grade(100))
