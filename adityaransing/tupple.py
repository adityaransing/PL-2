# 1. Create and Access Tuple
print("1. Create and Access Tuple")

t1 = (10, 20, 30, 40)

print("Tuple:", t1)
print("First element:", t1[0])
print("Last element:", t1[-1])
print()


# 2. Nested Tuple
print("2. Nested Tuple")

nested_tuple = (1, 2, (3, 4, 5), 6)

print("Nested Tuple:", nested_tuple)
print("Access nested element:", nested_tuple[2][1])
print()


# 3. Repetition of Tuple
print("3. Repetition of Tuple")

t2 = (7, 8)
repeated_tuple = t2 * 3

print("Original Tuple:", t2)
print("Repeated Tuple:", repeated_tuple)
print()


# 4. Concatenation of Tuples
print("4. Concatenation of Tuples")

t3 = (100, 200)
t4 = (300, 400)

concatenated_tuple = t3 + t4

print("First Tuple:", t3)
print("Second Tuple:", t4)
print("Concatenated Tuple:", concatenated_tuple)