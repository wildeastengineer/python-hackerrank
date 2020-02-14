a = 0
b = 0


def read_input():
    global a
    global b

    input_file = open("input.txt", "r")
    input_str = input_file.read()
    input_file.close()

    parsed_input = input_str.split("\n")
    a = int(parsed_input[0])
    b = int(parsed_input[1])


read_input()


def write_output(r1, r2):
    print(r1)
    print(r2)


def solve(a, b):
    return [
        a // b,
        a / b
    ]


[x1, x2] = solve(a, b)

write_output(x1, x2)
