#split the list into chunks of list of given size
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
for i in range(0, len(list1), k):
    print(list1[i:i + k])
    
