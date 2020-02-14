n = 0


def read_input():
    global n

    input_file = open("input.txt", "r")
    input_str = input_file.read()
    input_file.close()

    parsed_input = input_str.split("\n")
    n = int(parsed_input[0])


read_input()


for i in range(n):
    print(i + 1, end='')
