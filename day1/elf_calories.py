txt_file = open('puzzle_input.txt', 'r')
file_content = txt_file.read()
#print("The file content are: ", file_content)

content_list = file_content.split("\n")

print("The Array content are: ", content_list)
count = 0
sum = 0
max_cal = 0
max_count = 0



for i in content_list:
    if i :
        sum = sum + int(i)
        #print(i)

    if not i:
        count +=1
        print("Elf{} carrying: {}".format(count,sum))
        if sum > max_cal:
           max_cal = sum
           max_count = count
        sum = 0

if sum != 0:
    count +=1
    print("Elf{} carrying: {}".format(count,sum))
    if sum > max_cal:
           max_cal = sum
           max_count = count


print("Most calories:",max_cal)
print("number of elfs:",max_count)

txt_file.close()