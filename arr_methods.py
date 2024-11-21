# Creating an list
tharun_list = [10, 20, 30, 40, 50]
print("Original List:", tharun_list)

# Add an element to the end
tharun_list.append(60)  # Adding 60 to the list
print("After adding 60:", tharun_list)

# Inserting an element at index 2
tharun_list.insert(2, 25)  # Adding 25 at index 2
print("After inserting 25 at index 2:", tharun_list)

# Extending the list with new elements
tharun_list.extend([70, 80])  
print("After adding [70, 80]:", tharun_list)

# Removing a specific element
tharun_list.remove(30)  
print("After removing 30:", tharun_list)

# Removing an element at a specific index
removed_item = tharun_list.pop(3)  # Removing the element at index 3
print("After removing element at index 3:", tharun_list)
print("Removed element:", removed_item)

# Finding the index of an element
index_of_50 = tharun_list.index(50)  # Finding the index of 50
print("Index of 50:", index_of_50)

# Counting occurrences of an element
count_of_20 = tharun_list.count(20)  # Counting how many times 20 appears
print("Count of 20:", count_of_20)

# Reversing the list
tharun_list.reverse()  # Reversing the order of the list
print("After reversing:", tharun_list)

# Sorting the list
tharun_list.sort()  # Sorting the list in ascending order
print("After sorting:",tharun_list)

# Copying the list
copied_list = tharun_list.copy()  # Creating a copy of the list
print("Copied list:", copied_list)

# Clearing the list
tharun_list.clear()  # Clearing all elements in the list
print("After clearing the list:", tharun_list)
