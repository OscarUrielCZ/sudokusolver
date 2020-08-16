def draw(sudoku, message=''):
    if message != '':
        print(message)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    print(sudoku[i*3+k][j*3+l], end=' ')
                print('|', end=' ')
            print('')
        print('-'*23)

def get_option(gridname):
    option = 0

    while option < 1 or option > 9:
        try:
            option = int(input(f'Choose a {gridname} (1-9): '))
        except ValueError:
            print(' Error: Write a number')
            option = 0
    return option

def check_option(block, square):
    global sudoku
    return sudoku[block][square] == ' '

def fill():
    global sudoku, n_inputs
    more_inputs = True

    while more_inputs:
        draw(sudoku)
        valid_square = False
        
        while not valid_square:
            print('''1 2 3\n4 5 6\n7 8 9''')
            block = get_option('block')-1
            square = get_option('square')-1
            valid_square = check_option(block, square)
        number = get_option('number')
        sudoku[block][square] = number
        n_inputs += 1

        cont = input('More inputs yet? [Y/n]: ')
        if not (cont == 'Y' or cont == 'y' or cont == ''):
            more_inputs = False

def get_groups():
    global sudoku
    h_groups = []
    v_groups = []

    for block in range(3):
        gn = block*3    # group number (0, 3, 6)
        for line in range(3):
            ln = line*3     # line number (0, 3, 6)
            h_groups.append(sudoku[gn][ln:ln+3] + sudoku[gn+1][ln:ln+3] + sudoku[gn+2][ln:ln+3])
            v_groups.append([sudoku[block+rounds*3][line+cell*3] for rounds in range(3) for cell in range(3)])

    return h_groups, v_groups

def get_posibilities(hline, vline, missing, horizontal, vertical):
    posibilities = []

    for m in missing:
        if m not in horizontal[hline] and m not in vertical[vline]:
            posibilities.append(m)

    return posibilities

def solve():
    global sudoku, n_inputs
    solved = 1
    horizontal, vertical = get_groups()

    while n_inputs < 81 and solved > 0:
        solved = 0
        for b, block in enumerate(sudoku):
            missing = [n for n in range(1, 9+1) if n not in block]
            for s, square in enumerate(block):
                if square == ' ':
                    hline = int(b/3)*3+int(s/3)
                    vline = (b%3)*3+s%3;
                    posibilities = get_posibilities(hline, vline, missing, horizontal, vertical)

                    if len(posibilities) == 1:
                        value = posibilities[0]
                        missing.remove(value)
                        sudoku[b][s] = value
                        horizontal[hline][vline] = value
                        vertical[vline][hline] = value
                        n_inputs += 1
                        solved += 1
        print('Solved:', solved)

  
sudoku = [[' ' for j in range(9)] for i in range(9)]
n_inputs = 0
fill()
draw(sudoku, message='Your sudoku:')
print('Numbers:', n_inputs)
solve()
draw(sudoku, message='Answer:')
print('Numbers:', n_inputs)
