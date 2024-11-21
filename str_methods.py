# Creating a string
my_string = "Hello, My Name is Tharun"
print("Original String:", my_string)

# Converting to uppercase
upper_case = my_string.upper()  
print("Uppercase:", upper_case)

# Converting to lowercase
lower_case = my_string.lower()  
print("Lowercase:", lower_case)

# Stripping whitespaces
trimmed = my_string.strip()  # Remove leading/trailing spaces (none in this case)
print("Trimmed String:", trimmed)

# Finding the length of the string
length = len(my_string)  # Get the length of the string
print("Length of String:", length)

# Replacing a substring
replaced = my_string.replace("Tharun", "Kuchulu")  # Replace 'Tharun' with 'Kuchulu'
print("After Replacement:", replaced)

# Splitting the string
split_string = my_string.split(" ")  # Split the string at space character
print("Split String:", split_string)

# Checking if the string starts with "H"
starts_with_h = my_string.startswith("H")  # Check if it starts with 'H'
print("Starts with 'H':", starts_with_h)

# Checking if the string ends with "Tharun"
ends_with_tharun = my_string.endswith("Tharun")  # Check if it ends with 'Tharun'
print("Ends with 'Tharun':", ends_with_tharun)

# Finding the position of a substring
index_of_name = my_string.find("Name")  # Find the index of 'Name' where it starts
print("Index of 'Name':", index_of_name)

# Counting occurrences of a character
count_of_a = my_string.count("a")  # Count how many times 'a' appears
print("Count of 'a':", count_of_a)

# Checking if the string is alphanumeric
is_alnum = my_string.isalnum()  # Check if it's alphanumeric (False because of spaces and punctuation)
print("Is Alphanumeric:", is_alnum)

# Checking if the string is alphabetic
is_alpha = my_string.isalpha()  # Check if it contains only letters
print("Is Alphabetic:", is_alpha)

# Converting to title case
title_case = my_string.title()  # Convert to title case
print("Title Case:", title_case)

# Joining a list of strings
joined_string = "-".join(["My", "Name", "is", "Tharun"])  # Join words with a hyphen
print("Joined String:", joined_string)

# Reversing the string (not a built-in function, doing it manually)
reversed_string = my_string[::-1] 
print("Reversed String:", reversed_string)
