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

def solve():
    global sudoku, n_inputs
    solved = 1
    h_groups = []
    v_groups = []

    # making groups
    for block in range(3):
        gn = block*3    # group number (0, 3, 6)
        for line in range(3):
            ln = line*3     # line number (0, 3, 6)
            h_groups.append(sudoku[gn][ln:ln+3] + sudoku[gn+1][ln:ln+3] + sudoku[gn+2][ln:ln+3])
            v_groups.append([sudoku[block+rounds*3][line+cell*3] for rounds in range(3) for cell in range(3)])

    while n_inputs < 81 and solved > 0:
        solved = 0
        # Horizontal searching
        for row in range(9):
            missing = [n for n in range(1, 9) if n not in h_groups[row]]
            print(f'Row {row}. Missing: {missing}')
            for cell in range(9):
                if h_groups[row][cell] == ' ':
                    for m in missing:
                        if m not in v_groups[cell]:
                            print('Found', i)
                            block = (int)(row/3)*3+(int)(cell/3)
                            square = (row%3)*3+cell%3
                            sudoku[block][square] = i
                            # solved += 1
  
sudoku = [[' ' for j in range(9)] for i in range(9)]
n_inputs = 0
fill()
draw(sudoku, message='Your sudoku:')
print('Numbers:', n_inputs)
draw(sudoku, message='Answer:')
print('Numbers:', n_inputs)
solve()
