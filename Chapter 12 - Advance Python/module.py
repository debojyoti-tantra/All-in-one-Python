def func():
    print("hellow world!!!")


func()
print(__name__)

if __name__ == "__main__":
    # if this code is directly executed by running the file it's present in
    # so basically it's runs if this python file is run
    # if this file is imported any another file and run then this code is not running
    print("we are directly running this code")