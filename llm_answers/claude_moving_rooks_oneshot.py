"""
The following solution was produced by Claude 3.5 Sonnet on 10/2/2025
for the "traveling_rooks" problem.
"""
import chess
import chess.pgn

def get_squares_between(start, end):
    """Get all squares between start and end square (inclusive) for a rook move."""
    start_rank = chess.square_rank(start)
    start_file = chess.square_file(start)
    end_rank = chess.square_rank(end)
    end_file = chess.square_file(end)
    
    squares = set()
    if start_rank == end_rank:  # Horizontal move
        f1, f2 = min(start_file, end_file), max(start_file, end_file)
        for file in range(f1, f2 + 1):
            squares.add(chess.square(file, start_rank))
    else:  # Vertical move
        r1, r2 = min(start_rank, end_rank), max(start_rank, end_rank)
        for rank in range(r1, r2 + 1):
            squares.add(chess.square(start_file, rank))
    
    return squares

def track_rook_moves(game):
    """Track the distance traveled by each rook from their origin squares."""
    board = chess.Board()
    rook_distances = {}  # Maps origin square -> total distance
    rook_positions = {}  # Maps current position -> origin square
    
    # Initialize original rooks
    for square in [chess.A1, chess.H1, chess.A8, chess.H8]:
        rook_positions[square] = square
        rook_distances[square] = 0
    
    for move in game.mainline_moves():
        from_square = move.from_square
        to_square = move.to_square
        
        # Handle castling
        if board.is_castling(move):
            if to_square > from_square:  # Kingside
                rook_from = chess.square(7, chess.square_rank(from_square))
                rook_to = chess.square(5, chess.square_rank(from_square))
            else:  # Queenside
                rook_from = chess.square(0, chess.square_rank(from_square))
                rook_to = chess.square(3, chess.square_rank(from_square))
            
            # Add castling distance for the rook
            origin = rook_positions[rook_from]
            squares_traveled = get_squares_between(rook_from, rook_to)
            rook_distances[origin] += len(squares_traveled)
            rook_positions[rook_to] = origin
            del rook_positions[rook_from]
        
        # Handle regular rook moves
        elif board.piece_type_at(from_square) == chess.ROOK:
            origin = rook_positions[from_square]
            squares_traveled = get_squares_between(from_square, to_square)
            rook_distances[origin] += len(squares_traveled)
            rook_positions[to_square] = origin
            del rook_positions[from_square]
        
        # Handle pawn promotions to rook
        elif (board.piece_type_at(from_square) == chess.PAWN and 
              move.promotion == chess.ROOK):
            # Add the promotion square as a new rook origin
            rook_positions[to_square] = to_square
            rook_distances[to_square] = 0
        
        board.push(move)
    
    return rook_distances

def main(pgn_path):
    """Process the PGN file and print the origin square(s) of the rook(s) that traveled the most."""
    with open(pgn_path) as pgn_file:
        game = chess.pgn.read_game(pgn_file)
    
    rook_distances = track_rook_moves(game)
    
    if not rook_distances:
        return
    
    # Find maximum distance
    max_distance = max(rook_distances.values())
    
    # Get all rooks that traveled the maximum distance
    max_rooks = [chess.square_name(square) 
                 for square, distance in rook_distances.items() 
                 if distance == max_distance]
    
    # Sort alphabetically and join with commas
    print(','.join(sorted(max_rooks)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <pgn_file>")
        sys.exit(1)
    main(sys.argv[1])