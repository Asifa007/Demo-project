#lasrgest increasing subsequence
list1 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
current = 1
longest = 1
for i in range(len(list1)-1):
    if list1[i] < list1[i + 1]:
        current += 1
    else:
        current = 1
    if current > longest:
        longest = current   
print(longest)