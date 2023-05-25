# Write a function to flatten a nested dictionary. Namespace the keys with a period.

# For example, given the following dictionary:

# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
# it should become:

# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }
# You can assume keys do not contain dots in them, i.e. no clobbering will occur.

import ast

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# define a nested dictionary
nested_dict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

user_input = input("Please enter a nested dictionary (e.g. {'a': 1, 'b': {'c': 2}}): ")

nested_dict = ast.literal_eval(user_input)

print("Original dictionary:")
print(nested_dict)

flat_dict = flatten_dict(nested_dict)
print("\nFlattened dictionary:")
print(flat_dict)