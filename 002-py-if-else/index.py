def read_input():
    input_file = open("input.txt", "r")
    input_number = int(input_file.read())
    input_file.close()
    return input_number

def write_output(value):
    output = open("output.txt", "w")
    output.write(value)
    output.close()

def solve(num):
    if (num % 2 == 1):
        return "Weird"
    else:
        if (num >= 2 and num <= 5):
            return "Not Weird"
        elif (num >= 6 and num <= 20):
            return "Weird"
        else:
            return "Not Weird"

n = read_input()
result = solve(n)
write_output(result)