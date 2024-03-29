#!/usr/bin/env python

def execute_opcode(intcode,pointer):
    if intcode[pointer] == 1:
        intcode[intcode[pointer + 3]] = int(intcode[intcode[pointer + 1]]) + int(intcode[intcode[pointer + 2]])
        status = True
    elif intcode[pointer] == 2:
        intcode[intcode[pointer +3 ]] = int(intcode[intcode[pointer + 1]]) * int(intcode[intcode[pointer + 2]])
        status = True
    else:
        status = False
    pointer = pointer + 4
    return intcode,pointer,status

input = open("input", "r")
intcode = input.read().split(",")
intcode = [ int(x) for x in intcode ]
intcode[1] = 12
intcode[2] = 2
status = True
pointer = 0
while status:
    intcode,pointer,status = execute_opcode(intcode, pointer)

print(intcode[0])
