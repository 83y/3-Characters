# Generate every 3 letter name with A-Z and including 0-9
# 36x36x36 = 46656
# Do it like this (eg. 000, 001, 009, 00A, 00Z, 010, 019, 01A, 01Z, 02Z

string = "000"

letter = 97
number = 48

loops = 36

def to_letter(string, num):
    temp_list = list(string)
    temp_list[num] = chr(letter)
    string = "".join(temp_list)
    return string

def increase(string, num1, num2):
    temp_list = list(string)
    temp_list[num1] = chr(ord(temp_list[num1])+1) # Increases index 0 by +1
    temp_list[num2] = chr(number) # Sets index 1 to 0
    temp_list[2] = chr(number) # Sets index 1 to 0
    string = "".join(temp_list)
    return string

def regular_increase(string):
    temp_list = list(string)
    temp_list[2] = chr(ord(temp_list[2])+1)
    string = "".join(temp_list)
    return string

def log():
    file = open("3letters.txt", "a")
    file.write(string + "\n")
    file.close()

file = open("3letters.txt", "a")
file.truncate(0)
file.close()

isLog = False

for i in range(loops):
    if ord(string[0]) == 57 and ord(string[1]) == 122 and ord(string[2]) == 122:
        string = to_letter(string, 0)
    for j in range(loops):
        for k in range(loops):
            if ord(string[1]) == 57:
                string = to_letter(string, 1)
            if ord(string[1]) == 122 and ord(string[2]) == 122:
                string = increase(string, 0, 1)
            if ord(string[2]) == 57:
                log()
                isLog = True
                string = to_letter(string, 2)
                log()
            if ord(string[2]) == 122:
                log()
                isLog = True
                string = increase(string, 1, 2)
                log()
            if isLog == False:
                log()
            string = regular_increase(string)
            isLog = False
