# Hard-coded values
start = 3
end = 8

# Outer loop
for table in range(start, end + 1):

    # Create filename dynamically
    filename = str(table) + ".txt"

    # Open the file
    file = open(filename, "w")

    # Write heading
    file.write("Table of " + str(table) + "\n")

    # Print multiplication table
    for i in range(1, 11):
        file.write(str(table) + " * " + str(i) + " = " + str(table * i) + "\n")

    # Close the file
    file.close()

print("All files created successfully.")