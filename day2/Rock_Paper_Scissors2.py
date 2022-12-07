import re
txt_file = open('puzzle_input.txt', 'r')
file_content = txt_file.read()
#print("The file content are: ", file_content)

content_list = re.split('\s| \n',file_content)

print("The Array content are: ", content_list)

my_score = 0

for i in range(len(content_list)):
    if i % 2 == 1:
       if content_list[i] == 'X':
            my_score += 1
            if content_list[i-1] == 'A':
               my_score += 3  #draw
            elif content_list[i-1] == 'B':
               my_score += 0  
            elif content_list[i-1] == 'C':
               my_score += 6 
       elif content_list[i] == 'Y':
            my_score += 2
            if content_list[i-1] == 'A':
               my_score += 6
            elif content_list[i-1] == 'B':
               my_score += 3
            elif content_list[i-1] == 'C':
               my_score += 0
       elif content_list[i] == 'Z':
            my_score += 3
            if content_list[i-1] == 'A':
               my_score += 0
            elif content_list[i-1] == 'B':
               my_score += 6
            elif content_list[i-1] == 'C':
               my_score += 3



print(my_score)
    
        

