def friend(x):
    result = []
    for n in x:
        if len(n) == 4:
            result.append(n)
    return result

print(friend(["Ryan", "Kieran", "Mark",])) # ["Ryan", "Mark"]
print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"])) # ["Ryan"]
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"])) # ["Jimm", "Cari", "aret"]