ar = []

while True:
    ar.append(input("Please insert an item\n   > "))
    rep = input("\nHave all items been entered?\n   > ")
    if str.lower(rep) in ["y", "yes"]:
        break
    else:
        print()

search = input("\nSearch\n   > ")

flag = 0
for i in range(0,len(ar)):
    if ar[i] == search:
        flag = 1

print()
if flag == 1:
    print(search,"is present in the array")
else:
    print(search,"is not present in the array")
