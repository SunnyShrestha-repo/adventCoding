#Part 1
'''
def readInput(filename):
    with open(filename, 'r') as file:
        file_input = file.read().rstrip()
        input = [int(i) for i in file_input.split(',')]
        return input

def opcode(num):
    end = 99
    i = 0
    while num[i] != 99:
        pos = i
        pos1 = pos+1
        first_num = num[pos1]
        pos2 = pos+2
        second_num = num[pos2]
        savepos = pos+3
        save_at = num[savepos]
        # print('opcode:{}, first pos:{}, second pos:{}, save at: {}'.format(num[pos],first_num, second_num,save_at))
        if int(num[pos]) == 1:
            num[save_at] = num[first_num] + num[second_num]
        elif int(num[pos]) == 2:
            num[save_at] = num[first_num] * num[second_num]
        else:
            print('trouble bubble hit!')
        i += 4
    return num




value= readInput("day2input.txt")
print(opcode(value))
#3166704
'''

#Part 2
import random

def readInput(filename):
    with open(filename, 'r') as file:
        file_input = file.read().rstrip()
        input = [int(i) for i in file_input.split(',')]
        return input

def update_input(num_list):
    r1 = random.randint(0,99)
    r2 = random.randint(0,99)
    num_list[1] = r1
    num_list[2] = r2
    return num_list


def opcode(num):
    end = 99
    i = 0
    while num[i] != 99:
        pos = i
        pos1 = pos+1
        first_num = num[pos1]
        pos2 = pos+2
        second_num = num[pos2]
        savepos = pos+3
        save_at = num[savepos]
        # print('opcode:{}, first pos:{}, second pos:{}, save at: {}'.format(num[pos],first_num, second_num,save_at))
        if int(num[pos]) == 1:
            num[save_at] = num[first_num] + num[second_num]
        elif int(num[pos]) == 2:
            num[save_at] = num[first_num] * num[second_num]
        else:
            print('trouble bubble hit!')
        i += 4
    return num

def run_until(num_list):
    result = opcode(num_list)
    while result != 19690720:
        update_input(num_list)
        noun = num_list[1]
        verb = num_list[2]
        # result = opcode(num_list)
        print(noun)
        print(verb)



values = readInput("advent2b.txt")
print(run_until(values))
