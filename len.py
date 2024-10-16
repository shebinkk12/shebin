# Function to demonstrate len()
def demonstrate_len():
    string_example = "Hello, World!"  # A string
    list_example = [1, 2, 3, 4, 5]     # A list
    tuple_example = (10, 20, 30)        # A tuple
    dict_example = {'a': 1, 'b': 2}     # A dictionary

    print(f"The length of the string '{string_example}' is: {len(string_example)}")
    print(f"The length of the list {list_example} is: {len(list_example)}")
    print(f"The length of the tuple {tuple_example} is: {len(tuple_example)}")
    print(f"The length of the dictionary {dict_example} is: {len(dict_example)}")

# Run the demonstration
demonstrate_len()
