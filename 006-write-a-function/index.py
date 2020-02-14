year = 0


def read_input():
    global year

    input_file = open("input.txt", "r")
    input_str = input_file.read()
    input_file.close()

    parsed_input = input_str.split("\n")
    n = int(parsed_input[0])


read_input()


def write_output(x1):
    print(x1)


# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.


def is_leap(year):
    leap = False

    if (year % 400) == 0:
        leap = True
    elif (year % 100) == 0:
        leap = False
    elif (year % 4) == 0:
        leap = True

    return leap


x1 = is_leap(year)

write_output(x1)
