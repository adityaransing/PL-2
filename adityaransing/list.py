num = [26,6,17,4,3,12]
print("Orginal list is",num)
print("The first element from the list is",num[0])
print("The third number from  the list is",num[2])
print("The second last elment from  the list is",num[-2])

num.append(28)
num.insert(4, 95)
print("The new list after adding elements to it is:",num)

num.remove(28)
num.pop(-1)
print("The new list after removing elements is:",num)

num.sort()
print("Sorted list is",num)

num.reverse()
print("The reverse of the given list is:",num)