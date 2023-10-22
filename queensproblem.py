import re

# Prompt the user to enter the number of queens to be placed on an 8x8 chessboard.
queen_number = int(input("Enter number of queens on the board: "))

# Initialize lists to store queen positions and the chessboard state.
queens = []
chessboard = [["-" for _ in range(8)] for _ in range(8)]

# Lambda functions for position conversion
pos_to_index = lambda pos: (ord(pos[0].upper()) - 65, 8 - int(pos[1]))
index_to_pos = lambda index: "".join([chr(index[0] + 65), str(8 - index[1])])

# Regular expression pattern for valid positions (A1 to H8).
position_regex = r"[a-hA-H][1-8]"

# Loop to input and place queens.
for i in range(queen_number):
    position = ""
    valid_position = False
    while not valid_position:
        position = input(f"Enter coordinates of Queen #{i + 1}: ")
        valid_position = re.fullmatch(position_regex, position)
        if not valid_position:
            print("-- Invalid position --")
            continue

        column, row = pos_to_index(position)

        if chessboard[row][column] == "-":
            chessboard[row][column] = "\u265B"  # Place a queen on the chessboard.
            queens.append((column, row))
        else:
            valid_position = False
            print("-- Already occupied --")
            continue

# Display the chessboard.
print("\nChessboard:")
[print(f"\t{chr(i + 65)}", end="") for i in range(8)]
print()
for i, row in enumerate(chessboard):
    print(8 - i, end="")
    for piece in row:
        print(f"\t{piece}", end="")
    print()

# Detect conflicts between queens.
conflicts = []
for queen_a in queens:
    for queen_b in queens:
        if queen_a == queen_b:
            break

        # Check if a queen is attacking another queen (same row, column, or diagonal).
        if (queen_a[0] == queen_b[0] or
            queen_a[1] == queen_b[1] or
            abs(queen_a[0] - queen_b[0]) == abs(queen_a[1] - queen_b[1])):
            conflict_set = {queen_a, queen_b}
            if conflict_set not in conflicts:
                conflicts.append(conflict_set)

# Display the outcome (valid or invalid board).
if conflicts:
    print("\n~ Invalid Board ~")
    print("The following queens are attacking each other!")
    for conflict in conflicts:
        queen_a, queen_b = list(conflict)
        print(f"\t- {index_to_pos(queen_a)} and {index_to_pos(queen_b)}")
else:
    print("\n~ Valid Board ~")
    print("All queens are safe <3")
