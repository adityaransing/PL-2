def read_file():
    filename = input("Enter file name:")

    try:
         with open(filename,'r') as file:
             content = file.read()
             print("\n File Content:\n")
             print(content)
    except FileNotFoundError:
        print("Error:The file dosent exist.")
    except PermissionError:
        print("Error:You do not have permission to read  this file.")
    except Exception as e:
        print("An unexcepted error occured:{e}")

read_file()