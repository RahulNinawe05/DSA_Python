# ==============================
# PYTHON STRING BASICS
# ==============================

name = "Rahul It's Good"

print(name[0])  
# Access first character (index starts from 0)


# ==============================
# SLICING CONCEPT
# ==============================

slice_name = name[0:5]
print(slice_name)
# Extract characters from index 0 to 4 (5 is excluded)

num_list = "0123456789"

print(num_list[:])
# Print full string (copy of string)

print(num_list[3:])
# Start from index 3 to end

print(num_list[:7])
# Start from 0 to 6 (7 excluded)

print(num_list[0:8:2])
# Step slicing: take every 2nd character from 0 to 7

print(num_list[-3:])
# Last 3 characters

print(num_list[3:-5])
# From index 3 to 4 (because -5 cuts last part)


# ==============================
# STRING METHODS
# ==============================

name_strip = "        Rahul is a Boy     "

print(name.lower())
# Convert all letters to lowercase

print(name.upper())
# Convert all letters to uppercase

print(name_strip.strip())
# Remove extra spaces from left and right side


# ==============================
# REPLACE METHOD
# ==============================

name_replace = "The Boy is Beutifule"

print(name_replace.replace("Beutifule", "handsome"))
# Replace wrong word with correct word


# ==============================
# SPLIT METHOD
# ==============================

name_str_to_lst = "Rahul, Badal, Sahil, Sagar, Harish, Rahul, Badal,"

print(name_str_to_lst.split())
# Split by space (default behavior)

print(name_str_to_lst.split(", "))
# Split string into list using comma + space


# ==============================
# SEARCH METHODS
# ==============================

print(name_str_to_lst.find("i"))
# Returns index of first occurrence of "i"

print(name_str_to_lst.count("Rahul"))
# Count how many times "Rahul" appears


# ==============================
# EXTRA IMPORTANT POINTS
# ==============================

print(name.startswith("Rahul"))
# Check if string starts with "Rahul"

print(name.endswith("Good"))
# Check if string ends with "Good"

print("Rahul".isalpha())
# Check if all characters are alphabets

print("12345".isdigit())
# Check if all characters are numbers only


words = ["Rahul",   "Badal", "Sahil"]
print(words)
print(" ".join(words))
# Join list elements into one string with space separator