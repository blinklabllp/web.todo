def get_todos(filepath="todos.txt", mode='r'):
    with open(filepath, mode) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt", mode='w'):
    with open(filepath, mode) as file_local:
        file_local.writelines(todos_arg)


def parse(user_input):
    """Extract the values split by a comma in a string
    and return the two values via a dictionary.
    """
    # Get the two values in a list
    parts = user_input.split(",")

    # Store the two values in variables
    lower_bound = int(parts[0])
    upper_bound = int(parts[1])

    # Inject the values in a dictionary
    return {"lower_bound": lower_bound, "upper_bound": upper_bound}
