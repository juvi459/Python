new_file = open("myfile2.txt", "x")
new_file.close()

import os
print("Checking If My File exits or not ....")
if os.path.exists("myfile1.txt"):
    os.remove("myfile1.txt")
else:
    print("MY FILE DOES NOT exist....")

my_file = open("myfile1.txt","w")
my_file.write("Hi I am Penguin I am one year old")
my_file.close()


