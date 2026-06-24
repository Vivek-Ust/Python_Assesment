 
#1: Perform Basic List Operations
def list_operation(n1, n2):
    #Adding element to n1 and n2
    n1.insert(1, "orange")
    n2.append(5)
    print(f"Adding element, \n List1:{n1}\n List2:{n2}")
 
    #Modifying an elment
    n1[2] = "Mango"
    print("Modified List1:", n1)
 
    #Removing element
    n1.remove("kiwi") #delete by value
    n2.pop(1) #delete by index
    print(f"After removing elements, \n List1:{n1}\n List2:{n2}")
 
    #concating 2 list
    n1.extend(n2)
    print("Concating list:", n1)
 
    #Slicing
    print("Slicing the List:", n1[1:len(n1):2])
   
input1=['apple', 'banana', 'kiwi']
input2=[1, 2, 3, 4]
list_operation(input1, input2)
 
#2: Perform List Manipulation
def manip(fruits):
    print("The original list of fruits:",fruits)
    fruits.append("fig")
    fruits.insert(3, "cherry")
    fruits.extend(["date", "kiwi"])
    fruits.pop(1)
    print("The manipulated list of fruits:", fruits)
 
manip(["apple", "banana", "elderberry"])
 
#3: Sum and average of all numbers in a list
def list_data(lst_data):
    total=0
    for i in lst_data:
        total += i
    print("Sum = ", total)
    print("Average = ", (total/len(lst_data)))
list_data([2,3,4,5,6,7,8,9])
 
#4: Reverse a list
def reverse_List(lst):
    print("Reversed List using slicing: ",lst[::-1]) #slicing
#OR
    temp = []
    for i in range(len(lst)-1, -1, -1):
        temp.append(lst[i])
    print("Reversed List without using slicing:", temp )
 
reverse_List(["apple", "banana", "elderberry", "data"])
 
#Exercise 5: Turn every item of a list into its square
def square(num):
    new = list(map(lambda x: x**2, num))
    print("Square of numbers in list:",new)
square([2,3,4,5,6,7,8])
 
#Exercise 6: Find Maximum and Minimum
def max_min(lst):
    print("Maximum: ", max(lst))
    print("Minimum: ", min(lst))
    print("----Without using max/min function:----")
    mx = mn = lst[0]
    for i in lst:
        if i > mx:
            mx = i
        if i < mn:
            mn = i
    print("Maximum: ", mx)
    print("Minimum: ", mn)      
max_min([19, 67, 98, 56, 45])
 
#Exercise 7: Count Occurrences
def occurrences(lst):
    dic = {}
    for i in lst:
        dic[i] = dic.get(i, 0) + 1
    print("Count Occurrences",dic)
occurrences([1,2,3,2,4,2,4,3,5,1])
 
#Exercise 8: Sort a list of numbers
def sort_list(lst):
    print("Ascending order:", sorted(lst))
    print("Desending order:", sorted(lst, reverse=True))
    #without using sort function
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:  #for descending lst[i] < lst[j]
                lst[i], lst[j] = lst[j], lst[j]
    print("Ascending order, without using sort function", lst)
sort_list([19, 67, 98, 56, 45])
 
#Exercise 9: Create a copy of a list
def copylist(lst):
    print("Original list:", lst)
    copylst = lst.copy()
    print("Copied list:", copylst)
copylist(['a', 'b', 'c', 'd'])
 
#Exercise 10: Combine two lists
def combine(n1, n2):
    print("Combine two lists:")
    print(n1+n2)              # method:1  
    l=[]
    for j in (n1, n2):
        l.extend(j)
    print(l)                  # method:2
    n2.extend(n1)
    print(n2)                 # method:3
   
input1=['a', 'b', 'c']
input2=[1, 2, 3]
combine(input1, input2)
 
#Exercise 11: Remove empty strings from the list of strings
def empty_str(strs):
    temp = []
    for i in strs:
        if i != "" and i != " ":
            temp.append(i)
    print("Remove empty strings from the list of strings:",temp)
empty_str(["python", "", "C-programming", " ", "", "Cpp", "Java", " "])
 
#Exercise 12: Remove Duplicates from list
def duplicate(lst):
    temp = []
    for i in lst:
        if i not in temp:
            temp.append(i)
    print("Remove Duplicates from list: ", temp)
duplicate([1,2,3,4,2,5,1,6])
 
#Exercise 13: Remove all occurrences of a specific item from a list
def remove_occur(lst, remove):
    emt = []
    for i in lst:
        if i != remove:
            emt.append(i)
    print(f"Remove all occurrences of '{remove}' from the list", emt)
remove_occur(['apple', 'banana', 'apple', 'kiwi', 'apple', 'orange'], 'apple')
 
#Exercise 14: List Comprehension for Numbers
def lst_comprehensive(lst):
    even = [i for i in lst if i%2==0]
    print("List Comprehension for Numbers finding even numbers:", even)
lst_comprehensive([1,2,3,4,5,6,7,8,9])
 
#Exercise 15: Access Nested Lists
def access_nested(data):
    print("Access Nested Lists:")
    print(data[1])
    print(data[2][1])
    print(data[2][1][2])
access_nested([1, [2, 3], [4, [5, 6, 9]], 7])
 
#Exercise 16: Flatten Nested List
def flat_nested(lst):
    emt= []
    for i in lst:
        if isinstance(i, list):
            emt.extend(flat_nested(i))
        else:
            emt.append(i)  
    return emt
print(f"Flatten Nested List:",flat_nested([1, [2, 3], [4, [5, 6]], 7]))
 
#Exercise 17: Concatenate two lists index-wise
def combine(l1, l2):
    res = []
    for i in range(len(l1)):
        res.append(l1[i] + l2[i])
    print("Concatenate two lists index-wise:", res)
combine(['a', 'b', 'c'], ['1', '2', '3'])
 
#Exercise 19: Iterate both lists simultaneously
def iterate(l1, l2):
    print("Iterate both lists simultaneously:")
    for i, j in zip(l1, l2):
        print(i, j)
iterate(['a', 'b', 'c'], ['1', '2', '3'])
 
#Exercise 21: Add new item to list after a specified item
def additem(lst, specified, item):
    temp = []
    for i in lst:
        temp.append(i)
        if i == specified:
            temp.append(item)
    print("Original Lisr:", lst)
    print(f"After adding new item to list after a '{specified}' item",temp)
additem(['banana', 'kiwi', 'date', 'orange'], 'date','apple')
 
#Exercise 22: Extend nested list by adding the sublist
def nested_add(l1, l2):
    temp = []
    for i in l1:
        if isinstance(i, list):
            temp.append(i + l2)
        else:
            temp.append(i)
    print("Original list:", l1)
    print("Extend nested list by adding the sublist:",temp)
 
nested_add([1, 2, [3, 4], 5], ['a', 'b'])
 
#Exercise 23: Replace list’s item with new value if found
def replace(lst, olditem, newitem):
    print("Original list:", lst)
    for i in range(len(lst)):
        if lst[i] == olditem:
            lst[i] = newitem
    print("Replace lists item with new value",lst)
replace(['banana', 'kiwi', 'date', 'orange'], 'date', 'apple')