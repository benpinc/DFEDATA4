teams = ["A","BC","DEF","GHIJ","KLMNOP"]

# with open("teams.txt", "w") as file:
#     for i in teams:
#         name = str(i) + "\n"
#         file.write(name)


# file = open("teams.txt", "r")
# lines = file.readlines()
# file.seek(0)
# print(lines[0],lines[3])
# file.close()

file = open("teams.txt", "w")

newline = "This is a new line" + "\n"
file.write(newline)
for i in teams:
        name = str(i) + "\n"
        file.write(name)
file.close()
