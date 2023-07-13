# GPACalc
A mini-assignment I did awhile back in first year programming. At UofC. 


The given code is a program designed to calculate a student's term grade point average (GPA) and corresponding letter grade based on their input. The program prompts the user to enter their term grade point on a scale of 0 to 4.3.

The code starts by defining a function called GPA(), which seems to be intended for inputting the grade point. However, this function is never called or used in the code. So, it can be removed to simplify the program.

Next, the code uses a series of conditional statements (if, elif, and else) to determine the GPA and letter grade based on the input grade point. However, the implementation is inefficient and repetitive, leading to unnecessary lines of code.

To optimize the code, the inefficient logic can be replaced with a more concise and streamlined approach. The optimized code provided calculates the GPA and letter grade in a single function called calculate_gpa(). This function takes the grade point as input and uses a series of if and elif statements to determine the appropriate range and corresponding GPA and letter grade. It also includes a check for invalid grade points outside the range of 0-4.3.

By using this optimized version of the code, the program becomes more efficient and eliminates unnecessary repetition, resulting in cleaner and more maintainable code.
