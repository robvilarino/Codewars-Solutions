'''
Kata URL: https://www.codewars.com/kata/65b9af728732e1002463ab5e
'''
def construct_move(piece, position, captured, checked_or_mate, promoted, passant, rank_or_file):
    s = f"{piece}"
    
    if rank_or_file:
        if rank_or_file.isalpha(): 
            s += f" on file {rank_or_file}"
        elif rank_or_file.isdigit():
            s += f" on rank {rank_or_file}"
    
    s+= f" moved to {position}"
    
    if captured: 
        if not passant:
            s += " and captured"
        else:
            s += ", capturing en passant"
    
    if promoted:
        s += f" and promoted to {promoted}"
    
    if checked_or_mate == "+":
        s += ", check"
    elif checked_or_mate == "#":
        s += ", checkmate"
        
    return s+"."
    
def to_words(move: str) -> str:
    # Dictionary of Pieces
    pieces = {"K": "King", "Q": "Queen", "B": "Bishop", "R": "Rook", "N": "Knight"}
    
    # Default some variables
    captured = False
    checked_or_mate = ""
    promoted = ""
    rank_or_file = ""
    
    # Handle Castling
    if move[0] == "O":
        if len(move) == 3: 
            return "A kingside castle."
        else: 
            return "A queenside castle."
        
    # Assign Piece moving
    if move[0].islower():
        piece = "Pawn"
    else:
        piece = pieces[move[0]]
        move = move[1:]
    
    # Check if it is disambiguous move (rank or file)
    # If the next char is a number 
    # or the next two chars are letters and the first is not an x
    if piece != "Pawn":
        if move[0].isdigit(): 
            rank_or_file = move[0]
            move = move[1:]
        elif move[0].isalpha() and move[1].isalpha() and move[0] != "x": 
            rank_or_file = move[0]
            move = move[1:]
        
    # Handling how Pawns capture and then other pieces
    if move[0] == "x" and piece != "Pawn":
        captured = "True"
        move = move[1:]    
    elif piece == "Pawn" and move[1] == "x":
        captured = "True"
        move = move[2:]
        
    # Next two chars should be Position
    position = move[0:2]
    move = move[2:]
    
    # Check if the move is over, if so construct output
    if not move:
        return construct_move(piece,position,captured,checked_or_mate,promoted,"",rank_or_file)
         
    # Handle promoted pieces
    if move[0] == "=":
        promoted = pieces[move[1]].lower()
        move = move[2:]
    
    # Check if the move is over, if so construct output
    if not move:
        return construct_move(piece,position,captured,checked_or_mate,promoted,"",rank_or_file)
    
    # Handle check or checkmate moves
    if move[0] == "+" or move[0] == "#": 
        checked_or_mate = move[0]
        move = move[1:]
    
    if not move:
        return construct_move(piece,position,captured,checked_or_mate,promoted,"",rank_or_file)
    else:
        return construct_move(piece,position,captured,checked_or_mate,promoted,True,rank_or_file)