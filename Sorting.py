
print('SOLUTION FOR QUESTION 2')
print('''********First enter the total characters count in line 1 , then for line 2 , after the size has been initialised.*********
********After doing so, enter the characters of line 1 first and line 2 respectively.**********''')

print('--'*50)

size_of_list_1 = int(input('Enter the size of string_1(total characters in a line): '))  # initialisation of input line size
size_of_list_2 = int(input('Enter the size of string_2(total characters in a line): '))
list1 = []
list2 = []
print('Enter the elements of first string: ')
for x in range(size_of_list_1):

    x = input()
    list1.append(x)
print('Enter the elements of a second string: ')
for x in range(size_of_list_2):

    y = input()
    list2.append(y)
string1 = ''.join(list1)   # to convert list into string
string2 = ''.join(list2)     # to convert list into string
print ('First String: ', string1)
print ('Second String: ', string2)
list2.sort(key = lambda x: list1.index(x[0]),reverse=False)  # main function that sorts list2 with respect to list 1
sorted_string = ''.join(list2)     # to convert list into string
print('Sorted list is :', sorted_string)     # printing the result

print('--'*50)
