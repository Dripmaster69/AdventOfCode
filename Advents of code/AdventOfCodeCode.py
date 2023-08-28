def counter():
    with open("input.txt", "r", encoding="utf8") as f:
        total = 0
        list = []
        for x in f.readlines():
            list.append(int(x))
        counter = 0
        for i in list:
            if i > list[counter-1] and counter != 0:
                total += 1
            counter +=1
        print(total)

def countersum():
    with open("input.txt", "r", encoding="utf8") as f:
        total = 0
        list = []
        list_sum = []
        for x in f.readlines(): list.append(int(x))
        for x in range(len(list)):
            pie_slice = slice(-1+x ,2+x)
            var = 0
            print(list[pie_slice])
            for i in list[pie_slice]:
                var = i + var
            if len(list[pie_slice]) == 3:
                list_sum.append(var)
        counter = 0
        for p in list_sum:
            if  counter != 0 and p > list_sum[counter-1]:
                total += 1
            counter +=1
        print(total)

def submovment():
    with open("input2.txt", "r", encoding="utf8") as f:
        list = []
        units_forward = 0
        units_depth = 0
        for x in f.readlines(): list.append(x)
        for x in list:
            line_split = x.split()
            if f"{line_split[0]}" == "forward":
                units_forward = int(line_split[1]) + units_forward
            else:
                if f"{line_split[0]}" == "up":
                    units_depth = units_depth - int(line_split[1])
                else: units_depth = units_depth + int(line_split[1])
        print(units_depth*units_forward)

def submovment2():
    with open("input2.txt", "r", encoding="utf8") as f:
        list = []
        units_forward = 0
        units_depth = 0
        aim = 0
        for x in f.readlines(): list.append(x)
        for x in list:
            line_split = x.split()
            if f"{line_split[0]}" == "forward":
                units_forward = int(line_split[1]) + units_forward
                units_depth = units_depth + (aim * int(line_split[1]))
            else:
                if f"{line_split[0]}" == "up":
                    aim = aim - int(line_split[1])
                else: aim = aim + int(line_split[1])
        print(units_depth*units_forward)

def accounting():
    with open("input3.txt", "r", encoding="utf8") as f:
        list = []
        for x in f.readlines(): list.append(x)
        for x in list:
            for i in list:
                if int(x) + int(i) == 2020:
                    print(int(x)*int(i))

def accounting2():
    with open("input3.txt", "r", encoding="utf8") as f:
        list = []
        for x in f.readlines(): list.append(x)
        for x in list:
            for i in list:
                for q in list:
                    if int(x) + int(i) + int(q) == 2020:
                        print(int(x)*int(i)*int(q))

def passwords():
    with open("input4.txt", "r", encoding="utf8") as f:
        list = []
        configured_list = []
        configured_list2 = []
        for x in f.readlines(): list.append(x)
        for x in list:
            parts = x.split(" ")
            configured_list.append(parts)
        for x in configured_list:
            temp_list = []
            for i in x:
                i = i.strip(":\n")
                temp_list.append(i)
            configured_list2.append(temp_list)

        counter = 0
        for x in configured_list2:
            parameter = x[0].split("-")
            if x[2].count(f"{x[1]}") >= int(parameter[0]) and x[2].count(f"{x[1]}") <= int(parameter[1]):
                counter += 1
        print(counter)

def passwords2():
    with open("input4.txt", "r", encoding="utf8") as f:
        list = []
        configured_list = []
        configured_list2 = []
        for x in f.readlines(): list.append(x)
        for x in list:
            parts = x.split(" ")
            configured_list.append(parts)
        for x in configured_list:
            temp_list = []
            for i in x:
                i = i.strip(":\n")
                temp_list.append(i)
            configured_list2.append(temp_list)
        
        counter = 0
        for x in configured_list2:
            parameter = x[0].split("-")
            if x[2][int(parameter[0])-1] == x[1] or x[2][int(parameter[1])-1] == x[1]:
                if x[2][int(parameter[0])-1] != x[1] or x[2][int(parameter[1])-1] != x[1]:
                    counter += 1
        print(counter)

def module1():
    with open("input5.txt", "r", encoding="utf8") as f:
        total_mass = 0
        list = f.readlines()
        for x in list:
            x = (int(x)//3)-2
            total_mass = x + total_mass
        print(total_mass)

def lanternfish():
    with open("input6.txt", "r", encoding="utf8") as f:
        list = f.readline().split(",")
        list_of_fish = []
        for _ in range(80):
                for x in list:
                    if int(x)!= 0:
                        list_of_fish.append(int(x)-1)
                    else: list_of_fish.append(8)
                list = list_of_fish
    print(len(list))


def advent_of_code_2022_dec_1():
    with open("input7.txt", "r", encoding="utf8") as f:
        list = f.readlines()
        elf_tot_cals = 0
        list2 = []
        for x in list:
            if x != "\n":
                x.strip("\n")
                elf_tot_cals = elf_tot_cals + int(x)
            else:
                list2.append(elf_tot_cals)
                elf_tot_cals = 0
        elf_cals = list2[0]
        for x in list2:
            if x > elf_cals:
                elf_cals = x
        print(elf_cals)

def advent_of_code_2022_dec_2():
    with open("input8.txt", "r", encoding="utf8") as f:
        list = f.readlines()
        ptot = 0
        for x in list:
            battle = x.split(" ")
            battle.append(battle[1].strip("\n"))
            battle.pop(1)
            if battle[0] == "A" and battle[1] == "Y":
                ptot += 6
                ptot += 2
            elif battle[0] == "B" and battle[1] == "Z":
                ptot += 6
                ptot += 3
            elif battle[0] == "C" and battle[1] == "X":
                ptot += 6
                ptot += 1
            elif battle[0] == "A" and battle[1] == "X":
                    ptot += 3
                    if battle[1] == "X": ptot += 1
                    elif battle[1] == "Y": ptot += 2
                    else: ptot += 3
            elif battle[0] == "B" and battle[1] == "Y":
                ptot += 3
                if battle[1] == "X": ptot += 1
                elif battle[1] == "Y": ptot += 2
                else: ptot += 3
            elif battle[0] == "C" and battle[1] == "Z":
                ptot += 3
                if battle[1] == "X": ptot += 1
                elif battle[1] == "Y": ptot += 2
                else: ptot += 3
            else:
                if battle[1] == "X": ptot += 1
                elif battle[1] == "Y": ptot += 2
                else: ptot += 3
        print(ptot)


def advent_of_code_2022_dec_2_part():
    with open("input8.txt", "r", encoding="utf8") as f:
        list = f.readlines()
        ptot = 0
        for x in list:
            battle = x.split(" ")
            battle.append(battle[1].strip("\n"))
            battle.pop(1)
            if battle[1] == "X":
                if battle[0] == "A": ptot += 3
                elif battle[0] == "B": ptot += 1
                else: ptot += 2
            elif battle[1] ==  "Y":
                if battle[0] == "A": ptot += 4
                elif battle[0] == "B": ptot += 5
                else: ptot += 6
            else:
                if battle[0] == "A": ptot += 8
                elif battle[0] == "B": ptot += 9
                else: ptot += 7
        print(ptot)
