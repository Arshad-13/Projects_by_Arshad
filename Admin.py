import liblogin as llg

x = int(input("Enter the number of members to input: "))

for i in range(x):
    name = input("Ente the name: ")
    ID = input("Enter the ID: ")
    password = input("Enter the password: ")
    add = llg.LoginID(name, ID, password)
    add.add_member()

# add = llg.LoginID("Arshad", "U24AI112", "1234")

add.display_members()