import re
Base_Address=0x10000000                #4KB 
PC=0
def perform_instructions(instruction,PC):
    if(instruction[0]=='add'):
        if(len(instruction)!=4):
            print("syntax error at line number %d",PC)
        else:
            reg0=instruction[1]
            reg1=instruction[2]
            reg2=instruction[3]
            Reg[reg0]=Reg[reg1]+Reg[reg2]
            PC=PC+1
    elif(instructions[0]=='sub'):
        if(len(instruction)!=4):
            print("syntax error at line number %d",PC)
        else:
            reg0=instruction[1]
            reg1=instruction[2]
            reg2=instruction[3]
            Reg[reg0]=Reg[reg1]-Reg[reg2]
            PC=PC+1
    elif(instruction[0]=='lw'):
        if(len(instruction)!=3):
            print("syntax error at line number %d",PC)

        else:
            reg2_getting= re.search(r"\[a-z0-9]*",instruction[2],re.MULTILINE)
            offset_getting = re.search(r"\w+",instruction[2],re.MULTILINE)
            reg1 = instruction[1]
            reg2 = reg2_getting.group(0)
            offset = int(offset_getting.group(0))
            if(int(Reg[reg2],16)-base_address>=0 and (int(Reg[reg2],16)-base_address)%4==0 and offset%4==0):
                index = int((int(Reg[reg2],16)-base_address)/4 + offset/4)
                Reg[reg1] = data['.word'][index]
            PC+=1

    elif(instruction[0]=='sw'):
        if(len(instruction)!=3):
            print("syntax error at line number %d",PC)

        else:
            reg2_getting = re.search(r"\[a-z0-9]*",instruction[2],re.MULTILINE)
            offset_getting = re.search(r"\w+",instruction[2],re.MULTILINE)
            reg1 = instruction[1]
            reg2 = reg2_getting.group(0)
            offset = int(offset_getting.group(0))

            if(int(Reg[reg2],16)>=base_address and (int(Reg[reg2],16)-base_address)%4==0 and offset%4==0):
                index = int((int(Reg[reg2],16)-base_address)/4 + offset/4)
                if(index>=len(data['.word'])):
                    count = index-len(data['.word'])
                    for i in range(count):
                        data['.word'].append(0)
                    data['.word'].append(Reg[reg1])
                else:
                    data['.word'][index] = Reg[reg1]
            PC+=1

    elif(instruction[0]=='bne'):

        if(len(instruction)!=4):
            print("syntax error at line number %d",PC)
        
        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            
        if(Reg[reg1]!=Reg[reg2]):
            bne_flag = instruction[3]   
            PC = main[bne_flag] 

        else:
            bne_flag = ''
            PC+=1

    elif(instruction[0]=='lui'):                            # [ 'lui','a0','0x10101'] upper 20bits

        if(len(instruction)!=3):
            print("syntax error at line number %d",PC)

        else:
            reg1 = instruction[1]
            Reg[reg1] = hex(int(instruction[2]+'000',16))       
            PC+=1

    elif(instruction[0]=='slt'):

        if(len(instruction)!=4):
            print("syntax error at line number %d",PC)

        else:
            reg1 = instruction[1]
            Reg[reg1] = 0
            reg2 = instruction[2]
            reg3 = instruction[3]
            if(Reg[reg2]<Reg[reg3]):
                Reg[reg1] = 1
            PC+=1

    elif(instruction[0]=='beq'):

        if(len(instruction)!=4):
            print("syntax error at line number %d",PC)

        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            if(Reg[reg1]==Reg[reg2]):
            beq_flag = instruction[3]
            PC = main[beq_flag]

            else:
                    beq_flag = ''
                    PC+=1

    elif(instruction[0]=='j'):

        if(len(instruction)!=2):
            print("syntax error at line number %d",PC)

        else:
            j_flag = instruction[1]
            PC = main[j_flag]

    elif(instruction[0]=='addi'):

        if(len(instruction)!=4):
            print("syntax error at line number %d",PC)

        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            addend = int(instruction[3])
            if(type(Reg[reg2])==str and reg[Reg2][0:2]=='0x'):
                Reg[reg1] = hex(int(Reg[reg2],16)+addend)
            else:
                Reg[reg1] = Reg[reg2] + addend
            PC+=1
    elif(instruction[0]=='andi'):

        if(len(instruction)!=4):
            print("syntax error at line number %d",PC)

        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            anded = instruction[3]
            Reg[reg1] = hex(int(Reg[reg2],16)&int(anded,16))
            PC=PC+1

    elif(instruction[0]=='and'):

        if(len(instruction)!=4):
            print("syntax error at line number %d",PC)

        else:
            reg1 = instruction[1]
            reg2 = instruction[2]
            reg3 = instruction[3]
            Reg[reg1] = hex(int(Reg[reg2],16) & int(Reg[reg3],16))
            PC = PC + 1
            
    return PC

def remove_comments(file):
    return re.sub('#.*', '', file)


def data_part(file):
    data_set = []
    pattern = re.compile('\s*[,:|\s+]\s*')
    for line in file:
        data = remove_comments(line).strip()
        if data == ".text":
            break
        elif len(data) != 0:
            if data != "start:" and data != ".data":
                data_set.append([x for x in pattern.split(data) if x])
    return data_set


def instructions(file):
    instructions_set = []
    pattern = re.compile('\s*[,:|\s+]\s*')
    flag = False
    for line in file:
        data = remove_comments(line).strip()
        if data == ".text":
            flag = True
        elif len(data) != 0 and flag:
            instruction = [x for x in pattern.split(data) if x]
            if len(instruction) > 1:
                instructions_set.append(instruction)
    return instructions_set


def all_instructions(file):
    instructions_set = []
    pattern = re.compile('\s*[,:|\s+]\s*')
    flag = False
    for line in file:
        data = remove_comments(line).strip()
        if data == ".text":
            flag = True
        elif len(data) != 0 and flag:
            instruction = [x for x in pattern.split(data) if x]
            if len(instruction) == 1:
                instructions_set.append(instruction)
    return instructions_set


# def operations(instructions):

Reg = {"zero": 0, "ra": 0, "sp": 0, "gp": 0, "tp": 0, "t0": 0, "t1": 0, "t2": 0, "s0": 0, "s1": 0,
             "a0": 0, "a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "s2": 0, "s3": 0, "s4": 0,
             "s5": 0, "s6": 0, "s7": 0, "s8": 0, "s9": 0, "s10": 0, "s11": 0, "t3": 0, "t4": 0, "t5": 0, "t6": 0}

# print(len(Registers))
# testing
fileopen = open("risc.asm", "r+")
print(instructions(fileopen))
fileopen.seek(0)
print(data_part(fileopen))
fileopen.seek(0)
print(all_instructions(fileopen))
