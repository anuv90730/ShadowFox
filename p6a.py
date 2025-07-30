friends = ["Anu", "Eshi", "Maclin", "Lekh", "Deeksha"]

# Step 2: Create a list of tuples with (name, length of name)
name_length_tuples = [(name, len(name)) for name in friends]

# Print the result
print("List of tuples (Name, Length):")
print(name_length_tuples)