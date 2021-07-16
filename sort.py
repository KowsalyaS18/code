list1 = []
while True:
    input_list = input()
    if not input_list:
        break
    list1.append(input_list)tuple(input_list.split(","))
 
print(sorted(list1))
