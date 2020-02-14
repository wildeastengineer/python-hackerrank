n = 0
a = []


def read_input():
    global n
    global a

    input_file = open("input.txt", "r")
    input_str = input_file.read()
    input_file.close()

    parsed_input = input_str.split("\n")
    n = int(parsed_input[0])
    a = list(map(int, parsed_input[1].split(" ")))


read_input()

result = list(dict.fromkeys(a))
result.sort()
result.reverse()


print(result[1])

