welcome_words = "Hello there, it's a investigation."
print(welcome_words+"\n")

dic = {}
arr = []
flag = True
while flag:
    resp = input("Would you like to response?(yes/no)")

    if resp == 'no':
        break
    elif resp != 'yes': 
        continue
    else:
        name = input("Could you kindly tell me your name?")
        age = input("and your age?")
        age = int(age)
        answer = []

        while answer != 'quit':
            answer = input('Then tell me the place you wanna go if possible(enter "quit" to quit)')
            if answer != 'quit':
                arr.append(answer)

        dic[name] = {
            "age": age,
            "place": arr
        }
for name, info in dic.items():
    print("\n")
    print(f"{name.title().lstrip()}'s info:")
    for name_info,name_list in info.items():
        print(f"{name_info.title()}:{name_list}")
