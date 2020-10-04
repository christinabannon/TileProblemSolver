def getPiece(pieceNumber):
    if pieceNumber == 1:
        return [[-1,  1,  1,  1,  1],
                [ 1,  1, -1, -1, -1]]
    elif pieceNumber == 2:
        return [[-1, -1,  2,  2],
                [-1,  2,  2, -1],
                [ 2,  2, -1, -1]]
    elif pieceNumber == 3:
        return [[-1,  3,  3],
                [ 3,  3, -1],
                [-1,  3,  3]]
    elif pieceNumber == 4:
        return [[-1,  4,  4, -1],
                [ 4,  4,  4,  4]]
    else:
        return [[ 5,  5,  5,  5,  5,  5]]
