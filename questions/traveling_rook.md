# Goal
print the origin square of the rook traveled the most over the board during the game.

# Definitions
 * Each rook move travel along the start square, the end square and all the squares in between.
 * The distance traveled by a rook is the number of squares it traveled in every move in the game.
 * Castling is considered a rook move. For example, white kingside castling is a 3-square move for the h1 rook.
 * The origin square of a rook is the square where the rook started the game. For non-promoted rooks, it is h1, a1, h8 or a8.
 * Promoted rooks are considered as a new rook, with the origin square being the promotion square.

# Output format
SAN notation of the origin square. In case several rooks traveled the same distance, print comma-separated list of the origin squares, sorted alphabetically, without spaces.
