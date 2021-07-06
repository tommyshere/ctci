# If an elemnt in an M x N matrix is 0,
# its entire row and columns are set to 0

class Solution(object):
    def zero_matrix(matrix):
        rows = len(matrix) - 1
        columns = len(matrix[0]) - 1

        # find the zeroes first and create a list of tuples with x,y coords
        zero_array = []
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    zero_array.append((i, j))
        # for a row I can just do [0 for in range(columns + 1)]
        # loop through the zero_array and replace the rows tuple[0]
        # in column we have to for loop through row and replace the column to 0
        zero_row = [0 for i in range(columns + 1)]
        for tup in zero_array:
            # replace the array with zeros
            matrix[tup[0]] = zero_row
            for x in range(rows + 1):
                matrix[x][tup[1]] = 0

        return matrix

if __name__ == "__main__":
    print(Solution.zero_matrix([[1, 1, 1, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
    print(Solution.zero_matrix([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]])
