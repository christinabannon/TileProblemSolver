def getPretty(matrix, spacing):
    prettyPuzzle = ""
    for row in matrix:
        prettyPuzzle += spacing
        columns = row
        for col in columns:
            if col < 0:
                prettyPuzzle += "[ ]"
            elif col == 0:
                prettyPuzzle += "|||"
            else:
                prettyPuzzle += "[" + str(col) + "]"
        prettyPuzzle += "\n"
    return prettyPuzzle