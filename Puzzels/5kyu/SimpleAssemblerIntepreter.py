# codewars challenge link
# https://www.codewars.com/kata/58e24788e24ddee28e000053


# todo optimize is to slow
def simple_assembler(program):
    register = dict()
    program_index = 0
    while program_index < len(program):
        tokens = program[program_index].split(" ")
        match tokens[0]:
            case "mov":
                if tokens[2] in register:
                    register[tokens[1]] = int(register[tokens[2]])
                else:
                    register[tokens[1]] = int(tokens[2])
            case "inc":
                register[tokens[1]] += 1
            case "dec":
                register[tokens[1]] -= 1
            case "jnz":
                if tokens[1] in register and register[tokens[1]] != 0:
                    program_index += int(tokens[2]) - 1
        program_index += 1
    return register


if __name__ == '__main__':
    code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
    print(simple_assembler(code.splitlines()) == {'a': 1})

    code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
    print(simple_assembler(code.splitlines()) == {'a': 409600, 'c': 409600, 'b': 409600})
    print(simple_assembler(['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2']) == {'a': 0, 'b': -20})
