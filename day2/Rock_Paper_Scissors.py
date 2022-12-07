import re
txt_file = open('puzzle_input.txt', 'r')
file_content = txt_file.read()
#print("The file content are: ", file_content)

content_list = re.split('\s| \n',file_content)

print("The Array content are: ", content_list)

a = 0
b = 0

for i in range(len(content_list)):
    if i % 2 == 1:
        print(content_list[i])
        if content_list[i] == 'X':
           a = 1 
        elif content_list[i] == 'Y':
           a = 2
        else :
           a = 3

    if i % 2 == 0:
        if content_list[i] == 'A':
            b = 1
        elif content_list[i] == 'B':
            b = 2
        else :
            b = 3

    if a > b:
        print("You are winnner")
    elif b > a:
        print("You are lost")
    elif a == b:
        print("You are draw")


print(a,b)


