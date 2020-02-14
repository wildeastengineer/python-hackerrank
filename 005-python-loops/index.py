n = 0


def read_input():
    global n

    input_file = open("input.txt", "r")
    input_str = input_file.read()
    input_file.close()

    parsed_input = input_str.split("\n")
    n = int(parsed_input[0])


read_input()


def write_output(x1):
    for item in x1:
        print(item)


def solve(n):
    result = []

    for i in range(n):
        result.append(i ** 2)

    return result


x1 = solve(n)

write_output(x1)
