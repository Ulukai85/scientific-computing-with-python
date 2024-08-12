# Course Project: Build an arithmetic formatter

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dividers = []
    sums = []

    for term in problems:
        first, operator, second = term.split()

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        if not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        length = max(len(first), len(second)) + 2
        first_line.append(first.rjust(length ))
        second_line.append(operator + second.rjust(length - 1))
        dividers.append("-" * (length ))

        if show_answers:
            sums.append(str(eval(term)).rjust(length))

    first_line = '    '.join(first_line)
    second_line = '    '.join(second_line)
    third_line = '    '.join(dividers)


    if show_answers:
        fourth_line = '    '.join(sums)
        return '\n'.join([first_line, second_line, third_line, fourth_line])
    return '\n'.join([first_line, second_line, third_line])

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
