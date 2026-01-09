# x=open("div.txt", "r")
# y=x.read()
# print(y)

# x=open("div.txt","w")
# x.write("this is a new context\n")
# x.write("welcome to new code")

# x=open("new.txt","w")
# x.write("this is a new context\n")
# x.write("welcome to new code")

# x=open("new.txt","a")
# x.write("new line added \n")
# file.close()


# with open ("div.txt", "r") as file:

#     print(file.read())

# with open ("div.txt", "a") as file:
#     file.write("""\n hey, are you there? 
# where are you?\n""") 
#     print()

# with open ("new.txt", "r") as file:
#     lines=file.readlines() 
#     word= "new line added"
#     with open ("new.txt", "w") as file:
#         for line in lines:
#             if word not in line:
#                 file.write(line)

# remove=1
# with open ("new.txt", "r") as file:
#     lines=file.readlines()
# with open ("new.txt", "w") as file:
#     for i,line in enumerate(lines):
#         if i!= remove:
#             file.write(line) 