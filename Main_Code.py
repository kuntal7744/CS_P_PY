# Simple Text-Based Chess Game in Python

# Initialize an empty 8x8 chessboard
chessboard = [[' ' for _ in range(8)] for _ in range(8)]

# Set up the initial pieces (you can customize this)
chessboard[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
chessboard[1] = ['P'] * 8
chessboard[6] = ['p'] * 8
chessboard[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']

# Display the chessboard
for row in chessboard:
    print(' '.join(row))

# Example move: Move pawn from e2 to e4
chessboard[4][4] = chessboard[6][4]
chessboard[6][4] = ' '

# Display the updated chessboard
print("\nAfter moving pawn from e2 to e4:")
for row in chessboard:
    print(' '.join(row))
