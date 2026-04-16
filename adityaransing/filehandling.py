file = open("Sample.txt","w")
file.write("Hello, this is the first line of the file.\n")
file.write("File handling in python is easy to learn.\n")
file.close()
print("Data written successfully!")

file = open("Sample.txt","r")
print("Reading file contents!")
content = file.read()
print(content)
file.close()

file = open("Sample.txt","a")
file.write("This line is added to the file using append mode.\n")
file.close()
print("\nData appended successfully!.\n")

file = open("Sample.txt","r")
print("Updated file contents:")
print(file.read())
file.close()

