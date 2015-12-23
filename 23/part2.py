#!/usr/bin/python

class Computer():
    
    def __init__(self):
        self.program = []
        self.registers = {"a": 0, "b": 0}
        self.program_counter = 0

    def run_program(self):
        try: 
            while True:
                self.instructions[self.program[self.program_counter][0]](self, self.program[self.program_counter][1])
                self.program_counter += 1
        except IndexError:
            pass

    def load_program(self, program_string):
        for line in program_string.split("\n"):
            if line == "":
                continue

            line = line.replace(",","")
            self.program.append([line.split(" ")[0].strip(), list([arg.strip() for arg in line.split(" ")[1:]])])
            
    def halve_register(self, args):
        self.registers[args[0]] /= 2

    def triple_register(self, args):
        self.registers[args[0]] *= 3

    def increment_register(self, args):
        self.registers[args[0]] += 1

    def jump_offset(self, args):
        self.program_counter += int(args[0]) - 1

    def jump_if_even(self, args):
        if self.registers[args[0]] % 2 == 0:
            self.program_counter += int(args[1]) - 1

    def jump_if_one(self, args):
        if self.registers[args[0]]  == 1:
            self.program_counter += int(args[1]) - 1

    instructions = {"hlf": halve_register,
                    "tpl": triple_register,
                    "inc": increment_register,
                    "jmp": jump_offset,
                    "jie": jump_if_even,
                    "jio": jump_if_one}


def run_program(input_string):
    
    program = []

    for line in input_string.split("\n"):
        if line == "":
            continue
        
        
        line = line.replace(",","")
        program.append([line.split(" ")[0].strip(), [arg.strip() for arg in line.split(" ")[1:]]])
    



if __name__=="__main__":
    
    input_string = open("input.txt").read()
    
    comp = Computer()
    comp.registers["a"] = 1
    comp.load_program(input_string)
    comp.run_program()
    print comp.registers["b"]
