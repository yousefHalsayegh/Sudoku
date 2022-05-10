class Brain:
    ui = None

    def __init__(self, ui):
        self.ui = ui


    def solve(self, sudoku, peers, unitlist):
        
        self.ui.drawBoard(sudoku)

        boxes = [r + c for r in 'ABCDEFGHI' for c in '123456789']
        sudoku = self.reduce_puzzle(sudoku, peers, unitlist)

        if sudoku is False:
            return False

        if all(len(sudoku[s]) == 1 for s in boxes):
            return sudoku

        n,s = min((len(sudoku[s]), s) for s in boxes if len(sudoku[s]) > 1)

        for value in sudoku[s]:
            new_sudoku = sudoku.copy()
            new_sudoku[s] = value
            attempt = self.solve(new_sudoku, peers, unitlist)
            if attempt:
                return attempt

    def reduce_puzzle(self, sudoku, peers, unitlist):

        stalled = False

        while not stalled:

            solved_values_before = len([box for box in sudoku.keys() if len(sudoku[box]) == 1])

            self.eliminate(sudoku, peers)

            self.only_choice(sudoku, unitlist)

            solved_values_after = len([box for box in sudoku.keys() if len(sudoku[box]) == 1])

            stalled = solved_values_after == solved_values_before

            if len([box for box in sudoku.keys() if len(sudoku[box]) == 0]):
                return False

        return sudoku 

    def eliminate(self, sudoku, peers):


        solved = [box for box in sudoku.keys() if len(sudoku[box]) == 1] 

        for box in solved:

            digit = sudoku[box]

            for peer in peers[box]:

                sudoku[peer] = sudoku[peer].replace(digit, "")

        return sudoku


    def only_choice(self, sudoku, unitlist):
        
        for unit in unitlist:
            
            for digit in '123456789':
                
                dplaces = [box for box in unit if digit in sudoku[box]]
                
                if len(dplaces) == 1:
                    
                    sudoku[dplaces[0]] = digit

        return sudoku