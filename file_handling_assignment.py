try:
    # File Creation
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("This is line 1\n")
        file.write("This is line 2\n")
        file.write("This is line 3\n")
        print("File 'my_file.txt' created and written successfully.")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of 'my_file.txt':")
        for line in file:
            print(line, end="")

    # File Appending
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("This is line 4\n")
        file.write("This is line 5\n")
        file.write("This is line 6\n")
        print("Three additional lines appended to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: The specified file does not exist.")

except PermissionError:
    print("Error: Permission denied to access the file.")

finally:
    print("End of script.")
