set1={26,6,17,4,12}
set2={3,11,91,56,11}

print("Elements from set1 are:")
for elem in set1:
    print(elem,end="")
    print("\nElements from set2 are:")
for elem in set2:
    print(elem,end="")
    print()

union_set=set1.union(set2)
print("The union of given sets is:",union_set)

intersection_set=set1.intersection(set2)
print("The intersection os given set is:",intersection_set)


difference_set=set2.difference(set1)
print("The difference of given set is:",difference_set)

