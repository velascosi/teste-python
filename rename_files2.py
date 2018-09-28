import os
def rename_files():
    #(1) Get file names from a folder 
    file_list = os.listdir(r"C:\Users\t-siparq\www\python\prank")
    #print (file_list)
    saved_path = os.getcwd()
    print("Our current working directory is " + saved_path)
    os.chdir(r"C:\Users\t-siparq\www\python\prank")
    new_path = os.getcwd()
    print("Our current working directory is ", new_path)
    #(2) For each file, rename filename
    for file_name in file_list:
        #print("Old Name - " + file_name)
        #print("New Name - " + file_name.translate("0123457689"))
        os.rename(file_name, ''.join([i for i in file_name if not i.isdigit()])) # This works on my machine
    os.chdir(saved_path)
    print("Our current working directory is ", saved_path)
rename_files()
