x = 0
y = 0
z = 0
n = 0


def read_input():
    global x
    global y
    global z
    global n

    input_file = open("input.txt", "r")
    input_str = input_file.read()
    input_file.close()

    parsed_input = input_str.split("\n")
    x = int(parsed_input[0])
    y = int(parsed_input[1])
    z = int(parsed_input[2])
    n = int(parsed_input[3])


read_input()

l = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]


print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)])


