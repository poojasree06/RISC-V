import re
import sys

# instructions=['add','sub,,'addi','lw','sw','lui','slt','and','andi','beq','bne','bge','ble','li','slli','sll','j']

# add,sub,addi                  arithmetic                3  -->done
# and,slli,andi,sll             boolean                   4  -->done
# lw,sw,lui                     memory                    3  -->done
# bne,beq,bge,ble,bgt           conditional jumps         5  -->done
# j                             unconditional jumps       1  -->done


base_address = 0x10010000  # 4KB
PC = 0

# bne_stat = ''
# beq_stat = ''
# j_stat = ''
# bge_stat=''
# ble_stat=''

Reg = {"zero": 0, "ra": 0, "sp": 0, "gp": 0, "tp": 0, "t0": 0, "t1": 0, "t2": 0, "s0": 0, "s1": 0,
       "a0": 0, "a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "s2": 0, "s3": 0, "s4": 0,
       "s5": 0, "s6": 0, "s7": 0, "s8": 0, "s9": 0, "s10": 0, "s11": 0, "t3": 0, "t4": 0, "t5": 0, "t6": 0}


def perform_instructions(instruction, PC):
    if instruction[0] == 'add':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg0 = instruction[1]
            reg1 = instruction[2]
            reg2 = instruction[3]
            if type(Reg[reg1]) == str and type(Reg[reg2]) == str:
                Reg[reg0] = hex(int(Reg[reg1], 16) + int(Reg[reg2], 16))
            elif type(Reg[reg1]) == str and type(Reg[reg2]) == int:
                Reg[reg0] = hex(int(Reg[reg1], 16) + Reg[reg2])
            elif type(Reg[reg2]) == str and type(Reg[reg1]) == int:
                Reg[reg0] = hex(int(Reg[reg2], 16) + Reg[reg1])
            else:
                Reg[reg0] = Reg[reg1] + Reg[reg2]
            PC += 1

    elif instruction[0] == 'sub':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg0 = instruction[1]
            reg1 = instruction[2]
            reg2 = instruction[3]
            if type(Reg[reg1]) == str and type(Reg[reg2]) == str:
                Reg[reg0] = hex(int(Reg[reg1], 16) + int(Reg[reg2], 16))
            elif type(Reg[reg1]) == str and type(Reg[reg2]) == int:
                Reg[reg0] = hex(int(Reg[reg1], 16) + Reg[reg2])
            elif type(Reg[reg2]) == str and type(Reg[reg1]) == int:
                Reg[reg0] = hex(int(Reg[reg2], 16) + Reg[reg1])
            else:
                Reg[reg0] = Reg[reg1] - Reg[reg2]
            PC += 1

    elif instruction[0] == 'lw':
        if len(instruction) != 3:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2_d = instruction[2].split('(', 1)
            offset = int(reg2_d[0])
            reg2 = reg2_d[1][:-1]  # string reg name
            # print(reg2)
            # print(Reg[reg2])
            if int(Reg[reg2], 16) >= base_address and (int(Reg[reg2], 16) - base_address) % 4 == 0 and offset % 4 == 0:
                # print(int(Reg[reg2], 16))
                index = int((int(Reg[reg2], 16) - base_address) / 4 + offset / 4)
                # print(index)
                Reg[reg1] = data['.word'][index]  # data
            PC += 1

    elif instruction[0] == 'sw':
        if len(instruction) != 3:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2_d = instruction[2].split('(', 1)
            offset = int(reg2_d[0])
            reg2 = reg2_d[1][:-1]  # string reg name
            if int(Reg[reg2], 16) >= base_address and (int(Reg[reg2], 16) - base_address) % 4 == 0 and offset % 4 == 0:
                index = int((int(Reg[reg2], 16) - base_address) / 4 + offset / 4)
                if index >= len(data['.word']):  # data
                    count = index - len(data['.word'])  # data
                    for i in range(count):
                        data['.word'].append(0)  # data
                    data['.word'].append(Reg[reg1])
                else:
                    data['.word'][index] = Reg[reg1]
            PC += 1

    elif instruction[0] == 'lui':  # [ 'lui','a0','0x10101'] upper 20bits
        if len(instruction) != 3:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            Reg[reg1] = hex(int(instruction[2] + '000', 16))
            PC += 1

    elif instruction[0] == 'slt':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            Reg[reg1] = 0
            reg2 = instruction[2]
            reg3 = instruction[3]
            if Reg[reg2] < Reg[reg3]:
                Reg[reg1] = 1
            PC += 1

    elif instruction[0] == 'bne':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
        if Reg[reg1] != Reg[reg2]:
            bne_stat = instruction[3]
            PC = main[bne_stat]  # main
        else:
            bne_stat = ''
            PC += 1

    elif instruction[0] == 'bge':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            if Reg[reg1] >= Reg[reg2]:
                bge_stat = instruction[3]
                PC = main[bge_stat]
            else:
                bge_stat = ''
                PC += 1

    elif instruction[0] == 'bgt':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            if Reg[reg1] > Reg[reg2]:
                bgt_stat = instruction[3]
                PC = main[bgt_stat]
            else:
                bgt_stat = ''
                PC += 1

    elif instruction[0] == 'ble':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            if Reg[reg1] <= Reg[reg2]:
                ble_stat = instruction[3]
                PC = main[ble_stat]
            else:
                ble_stat = ''
                PC += 1

    elif instruction[0] == 'beq':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            if Reg[reg1] == Reg[reg2]:
                beq_stat = instruction[3]
                PC = main[beq_stat]  # ??

            else:
                beq_stat = ''
                PC += 1

    elif instruction[0] == 'slli':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            reg3 = int(instruction[3])
            if type(Reg[reg2]) == str and Reg[reg2][0:2] == '0x':
                # print(hex(int(Reg[reg2], 16) << reg3))
                Reg[reg1] = hex(int(Reg[reg2], 16) << reg3)
            else:
                Reg[reg1] = Reg[reg2] << reg3
            #  print(Reg[reg1])
        PC += 1

    elif instruction[0] == 'sll':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            reg3 = int(instruction[3])
            if type(Reg[reg2]) == str and Reg[reg2][0:2] == '0x':
                # print(hex(int(Reg[reg2], 16) << reg3))
                Reg[reg1] = hex(int(Reg[reg2], 16) << reg3)
            elif type(Reg[reg3]) == str and Reg[reg3][0:2] == '0x':
                Reg[reg1] = hex(reg2 << int(Reg[reg3], 16))
            else:
                Reg[reg1] = Reg[reg2] << reg3
            #  print(Reg[reg1])
        PC += 1

    elif instruction[0] == 'j':
        if len(instruction) != 2:
            print("syntax error at line number %d", PC)
            exit()
        else:
            j_flag = instruction[1]
            PC = main[j_flag]

    elif instruction[0] == 'li':
        if len(instruction) != 3:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = int(instruction[2])
            if type(Reg[reg1]) == str and Reg[reg1][0:2] == '0x':
                Reg[reg1] = hex(int(Reg[reg2], 16))
            else:
                Reg[reg1] = reg2
        #  print(Reg)
        PC += 1

    elif instruction[0] == 'addi':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            addend = int(instruction[3])
            if type(Reg[reg2]) == str and Reg[reg2][0:2] == '0x':
                # print(hex(int(Reg[reg2], 16) + addend))
                Reg[reg1] = hex(int(Reg[reg2], 16) + addend)
            else:
                Reg[reg1] = Reg[reg2] + addend
            # print(Reg[reg1])
        PC += 1

    elif instruction[0] == 'andi':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()

        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            anded = instruction[3]
            Reg[reg1] = hex(int(Reg[reg2], 16) & int(anded, 16))
            PC += 1

    elif instruction[0] == 'and':
        if len(instruction) != 4:
            print("syntax error at line number %d", PC)
            exit()
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            reg3 = instruction[3]
            Reg[reg1] = hex(int(Reg[reg2], 16) & int(Reg[reg3], 16))
            PC += 1

    return PC


def all_instructions(file):
    all_instructions = []
    pattern = re.compile('\s*[,|\s+]\s*')
    for line in file:
        data = remove_comments(line).strip()
        if len(data) != 0:
            instruction = [x for x in pattern.split(data) if x]
            all_instructions.append(instruction)
    return all_instructions


def remove_comments(file):
    return re.sub('#.*', '', file)


def show_registers():
    i = 0
    print()
    for reg in Reg.keys():
        print(reg + " (x" + str(i) + ") " + ": " + str(Reg[reg]))
        i = i + 1
    print()


def show_memory():
    print()
    for i in range(len(data['.word'])):
        print(hex((base_address + 4 * i)) + ": " + str(data['.word'][i]))
    print()


# main program
text_address = 0x00000000
text_memory = ['' for i in range(2048)]

fileopen = open("instructions.s", "r+")
instructionslist = all_instructions(fileopen)

data_and_text = {'data': [], 'text': []}
label = {'data': []}  # list containing data section labels
# dictionary containing two lists data list and text list which contain respective instructions
data_index = 0
text_index = 0

for i in range(len(instructionslist)):
    if instructionslist[i][0] == '.data':
        data_index = i
    elif instructionslist[i][0] == '.text':
        text_index = i

for i in range(data_index + 1, text_index):
    if (len(instructionslist[i]) > 1):
        data_and_text['data'].append(instructionslist[i])
    elif (len(instructionslist[i]) == 1):
        label['data'].append(instructionslist[i])

for i in range(text_index + 1, len(instructionslist)):
    if instructionslist[i][0] != 'main:':
        data_and_text['text'].append(instructionslist[i])

data = {'.word': []}
# count = 0
# print(data_and_text['data'][0])
for ins in data_and_text['data']:
    if ins[0] == '.word':
        for i in range(1, len(ins)):
            data['.word'].append(int(ins[i]))
    elif ins[1] == '.word':
        for i in range(2, len(ins)):
            data['.word'].append(int(ins[i]))
        # count += 1

main = {}  # dictionary which contains labels as keys and corresponding numbers as values
count = 0

for ins in data_and_text['text']:
    if len(ins) == 1:  # label:
        ins[0] = ins[0][:-1]  # label
        main[ins[0]] = count  # main[label]=0  main={'label':0}
    else:
        count += 1

for ins in data_and_text['text']:
    if ins[0] in main.keys():
        data_and_text['text'].remove(ins)

index = 0
for ins in data_and_text['text']:
    text_memory[index] = ins  # storing each instruction in text segment
    print(str(index) + ":  " + str(text_memory[index]))
    # prints list of all list instructions without labels
    index += 1

print(Reg)  # prints Reg list
print(data['.word'])  # prints elements of array
print(data_and_text['data'])
print(main)  # prints labels inside text part after main
print("\nPress 1 to RUN file")
print("Press 2 to RUN step by step")
print("Press 3 to Exit")

while True:
    choice = int(input())
    count = 0
    # print(len(data_and_text['text']))
    if choice == 1:
        while PC != len(data_and_text['text']):
            #  print(PC)
            count += 1
            #   print(data_and_text['text'][PC])
            PC = perform_instructions(data_and_text['text'][PC], PC)

            if PC > len(data_and_text['text']):
                print("Sorry terminating the program due to unexpected error :(")
        show_registers()
        show_memory()
        print("Executed the file Successfully...")
        print("Total count: " + str(count))
        exit()
    elif choice == 2:
        count = 0
        while True:  # keeps on running until we stop giving some number
            print('1.Run Step by Step || 2.Show registers || 3.Show Memory || 4.Run file || 5.exit')
            option = int(input())
            if option == 1:
                if PC != len(data_and_text['text']):
                    print(PC)
                    count += 1
                    print(data_and_text['text'][PC])
                    PC = perform_instructions(data_and_text['text'][PC], PC)
                    if PC > len(data_and_text['text']):
                        exit("Sorry terminating the program due to unexpected error :(")
                    continue
                else:
                    print()
                    print("Executed the file Successfully...")
                    print(count)  # total count
                    print()
            elif option == 2:
                show_registers()
            elif option == 3:
                show_memory()
            elif option == 4:
                while PC != len(data_and_text['text']):
                    print(PC)
                    count += 1
                    #   print(data_and_text['text'][PC])
                    PC = perform_instructions(data_and_text['text'][PC], PC)
                    if PC > len(data_and_text['text']):
                        print("Sorry terminating the program due to unexpected error :(")
                print()
                print("Executed the file Successfully...")
                print("Total count: " + str(count))
                print()
            elif option == 5:
                sys.exit("Exiting from the Program...")
            else:
                print("Unexpected Error occurs, Enter again...")
    elif choice == 3:
        sys.exit("Exiting from the Program...")
    else:
        print("\nUnexpected Error occurs, Enter again...")
        print("\nPress 1 to RUN file")
        print("Press 2 to RUN step by step")
        print("Press 3 to Exit")
