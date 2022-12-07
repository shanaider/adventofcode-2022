import re
txt_file = open('puzzle_input.txt', 'r')
file_content = txt_file.read()
#print("The file content are: ", file_content)

content_list = re.split('\s| \n',file_content)

print("The Array content are: ", content_list)

my_score = 0

for i in range(len(content_list)):
    if i % 2 == 0:
       if content_list[i] == 'A':
            
            if content_list[i+1] == 'X':
               my_score += 0 + 3
            elif content_list[i+1] == 'Y':
               my_score += 3 + 1  
            elif content_list[i+1] == 'Z':
               my_score += 6 + 2
       elif content_list[i] == 'B':
            if content_list[i+1] == 'X':
               my_score += 0 + 1
            elif content_list[i+1] == 'Y':
               my_score += 3 + 2
            elif content_list[i+1] == 'Z':
               my_score += 6 + 3
       elif content_list[i] == 'C':
            if content_list[i+1] == 'X':
               my_score += 0 + 2
            elif content_list[i+1] == 'Y':
               my_score += 3  + 3
            elif content_list[i+1] == 'Z':
               my_score += 6 + 1



print(my_score)
    
        

