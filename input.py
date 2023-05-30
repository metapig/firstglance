welcome_words = "Hello there, it's a investigation."
print(welcome_words)

dic = {}
arr = []
flag = True
while flag:
    resp = input("\nWould you like to response? (yes/no) ")

    if resp == 'no':
        break
    elif resp != 'yes': 
        continue
    else:
        name = input("\nCould you kindly tell me your name? ")
        age = input("\nand your age? ")
        age = int(age)
        answer = []

        while answer != 'quit':
            prompt = '\nThen tell me the place you wanna go if possible (enter "quit" to quit)'
            prompt += '\n'+"you can enter for multiple times "
            answer = input(prompt)
            if answer != 'quit':
                arr.append(answer)

        dic[name] = {
            "age": age,
            "place": arr
        }
for name, info in dic.items():
 
    print(f"\n{name.title().lstrip()}'s info:")
    for name_info,name_list in info.items():
        print(f"\t{name_info.title()}:{name_list}")

input("Press ang key to quit")
