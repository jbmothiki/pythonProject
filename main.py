# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    try:
        open('config.txt')
    except FileNotFoundError:
        print_hi("Config file not found")
    except IsADirectoryError:
        print_hi("config.txt is a directory, not a file. Couldn't read it!")
    except PermissionError:
        print_hi("Permission denied")


def gen():
    try:
        open('mars.jpg')
    except Exception as e:
        print("Problem opening mars.jpg", e)


def openfile():
    error_map = {12: "File not found",
                 13: "Can't open file"}
    try:
        open('mars.jpg')
    except OSError as e:
        try:
            print(error_map[e.errno])
        except KeyError as key:
            print("Problem opening mars.jpg", key)


loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

true = ["yes", "y", "true", "t"]
false = ["no", "n", "false", "f"]


def parse(file_name):
    parsed_config = {}
    for line in file_name.split("\n"):
        try:
            key, value = line.split('=')
            parsed_config[key] = value
        except ValueError:
            print(f"unable to parse: \x1B[3m{line}\x1B[0m")
    print(parsed_config)


def water_est(astronauts, water_left, days_left):
    """
    A function to check whether the remaining water is sufficiently low.

    The input is provided in the form of a dictionary (no newlines). States are subclasses of the `state` class. For
    example: The astronauts is a list of the names of the astronauts.
    """
    # Check if all parameters are int and raise a TypeError if not
    for arg in [astronauts, water_left, days_left]:
        if not isinstance(arg, int):
            raise TypeError(f"Expected an int, got {type(arg)}")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    # ValueError RuntimeError
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days")
    print(f'Total water left after {days_left} days is {total_water_left} litres')


def alert_navigation_system(er):
    print(f"f*ck! {er}")


def str_to_bool(s):
    if s.lower() in true:
        print(True)
    elif s.lower() in false:
        print(False)
    else:
        raise ValueError(f"Unrecognized input: {s}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    str_to_bool('t')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
