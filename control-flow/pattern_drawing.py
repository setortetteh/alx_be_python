# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print '*' in each row
    for col in range(size):
        print("*", end="")  # print without newline
    print()  # move to the next line after one row
    row += 1
