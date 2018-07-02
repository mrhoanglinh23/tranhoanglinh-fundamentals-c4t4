
name = {
    "hc" : "học",
    "ng" : "người",
    "pt" : "phet",
    "eny": "em người yêu",
    "any": "anh người yêu",
    "ns" : "nói sau",
    "ngta": "người ta",
    "lm" : "làm",
    "r" : "rồi",
}

loop = True
while loop:

    for key in name.keys():
        print(key, end="   ")

    print()

    code = input("Your code: ")
    if code in name:
        print("translation:", name[code])
    else:
        print("not found")
        contribute = input("Do you want contribute this word (Y/N): ").lower()
    if contribute == "y":
        trans = input("Your translation")
        name[code] = trans
    else:
        print(name) 
        loop = False
