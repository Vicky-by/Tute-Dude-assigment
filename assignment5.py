# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

st_recod={ "Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 90, "Ethan": 88}
st_name=input("Enter  Student Name: ")

if st_name in st_recod:
    print(f"{st_name}'s mark: {st_recod[st_name]}")
else:
    print("Student not found")



#task 2---------------
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

list=[1,2,3,4,5,6,7,8,9,10,11]
print(list)
first5=list[1:5]     #first five element 
print(first5)

