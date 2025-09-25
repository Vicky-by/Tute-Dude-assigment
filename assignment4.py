#open a text file and read

try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes leading/trailing whitespace including newline
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")



#----Task2---------------
# Step 1: Take user input and write to output.txt
# Step 1: Take user input and write to output.txt

user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data to the same file
additional_input = input("Enter additional text to append to the file: ")
with open("output.txt", "a") :
    file.write(additional_input + "\n")

# # Step 3: Read and display the final content of the file
# print("\nFinal content of output.txt:")
# with open("output.txt", "r") :
#     content = file.read()
#     print(content)
