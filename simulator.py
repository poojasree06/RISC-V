import re


def remove_comments(file):
    return re.sub('#.*', '', file)


def data_part(file):
    data_set = []
    pattern = re.compile('\s*[,|\s+]\s*')
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
    pattern = re.compile('\s*[,|\s+]\s*')
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


def labels(file):
    labels_set = []
    pattern = re.compile('\s*[,|\s+]\s*')
    flag = False
    for line in file:
        data = remove_comments(line).strip()
        if data == ".text":
            flag = True
        elif len(data) != 0 and flag:
            instruction = [x for x in pattern.split(data) if x]
            if len(instruction) == 1:
                label = []
                #      print(instruction)
                while len(instruction) != 1:
                    label.append(instruction)
                labels_set.append(label)
    return labels_set


Registers = {"zero": 0, "ra": 0, "sp": 0, "gp": 0, "tp": 0, "t0": 0, "t1": 0, "t2": 0, "s0": 0, "s1": 0,
             "a0": 0, "a1": 0, "a2": 0, "a3": 0, "a4": 0, "a5": 0, "a6": 0, "a7": 0, "s2": 0, "s3": 0, "s4": 0,
             "s5": 0, "s6": 0, "s7": 0, "s8": 0, "s9": 0, "s10": 0, "s11": 0, "t3": 0, "t4": 0, "t5": 0, "t6": 0}

# print(len(Registers))
# testing
fileopen = open("risc.asm", "r+")
print(instructions(fileopen))
fileopen.seek(0)
print(data_part(fileopen))
fileopen.seek(0)
print(labels(fileopen))
