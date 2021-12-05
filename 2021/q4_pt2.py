draw_numbers = None
boards = []


class Board:
    def __init__(self, board_array, length_row, length_col):
        self.board_array = board_array
        self.length_row = length_row
        self.length_col = length_col
        self.tracker = [[0] * length_row, [0] * length_col]
        self.board_dict = self.board_dict(board_array)

    def board_dict(self, board_array):
        new_board_dict = {}

        for i in range(0, len(board_array)):
            for j in range(0, len(board_array[i])):
                cell = {board_array[i][j]: [i, j, False]}
                new_board_dict.update(cell)

        return new_board_dict

    def check_cell(self, draw_num):
        cell = self.board_dict.get(draw_num)
        if cell:
            # Update cell
            self.board_dict.update({draw_num: [cell[0], cell[1], True]})
            # Update tracker if cell exists
            self.update_tracker(cell[0], cell[1])

    def get_unmarked_cells(self):
        unmarked_list = []
        for cell in self.board_dict:
            cell_val = self.board_dict.get(cell)
            if not cell_val[2]:
                unmarked_list.append(cell)

        test_list = [int(n) for n in unmarked_list]
        return sum(test_list)

    def update_tracker(self, row, col):
        # Update row
        self.tracker[0][row] += 1

        # Update col
        self.tracker[1][col] += 1

    def check_winner(self):
        for i in range(0, len(self.tracker)):
            for j in range(0, len(self.tracker[i])):
                if self.tracker[i][j] == self.length_row:
                    return i, j

        return None


with open("q4_input") as file:
    data = []
    for i, line in enumerate(file.readlines()):
        line = line.strip().rstrip()
        line_arr = line.strip().replace("  ", " ").split(" ")
        if i == 0:
            draw_numbers = line.strip().rstrip().split(",")
        elif i > 1:
            data.append(line_arr)

    board = []
    for i, line in enumerate(data):
        if i == len(data) - 1:
            board.append(line)
            boards.append(board)
            break

        if len(line) == 1:
            boards.append(board)
            board = []
        else:
            board.append(line)

boards_obj = []

for board_arr in boards:
    board_obj = Board(board_arr, len(board_arr[0]), len(board_arr))
    boards_obj.append(board_obj)


def start_game(boards_obj):
    winners = []
    winning_num = []
    for n in draw_numbers:
        for i in range(0, len(boards_obj)):
            board_obj = boards_obj[i]
            board_obj.check_cell(n)
            winner = board_obj.check_winner()
            if winner:
                if i not in winners:
                    winners.append(i)
                    winning_num.append(n)

                if len(winners) == len(boards_obj):
                    return winners, winning_num


winners, winning_num = start_game(boards_obj)
winning_board = boards[winners[-1]]
winnning_board_obj = boards_obj[winners[-1]]

last_draw = winning_num[-1]
print(int(last_draw) * winnning_board_obj.get_unmarked_cells())
