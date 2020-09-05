import os

basepath = input("\nEnter the entire destination folder directory: ")
print("\n")
elist = []
plist = []
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            #print('*' , entry.name)
            elist.append(entry.name)

for i in elist:
        f_extns = i.split(".")
        if (f_extns[1] == 'py'):
            plist.append(f_extns[0])
            print('*' , f_extns[0])

#print("\n",plist)

print("\n")

user_choice = input("Run all files or a specific file? [all,s]: ")
if (user_choice == 's' or user_choice == 'S'):
    ans = 'y'
    while ans == 'y':
        file_number = input("\n Which file do you want to run? [1,2,3..]: ")
        file_to_run = int(file_number) - 1
        print("\n")
        data_dir = os.path.join(basepath, plist[file_to_run]+'.py')
        exec(open(data_dir).read())
        ans = input("\n Do you want to run another file? [y/N]: ")

else:
    print("\n")
    for i in plist:
        data_dir = os.path.join(basepath, i+'.py')
        exec(open(data_dir).read())
    
    print("\n")

