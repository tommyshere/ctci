# take a perfect square matrix and rotate it 90 degrees

# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# the pattern for rotating a matrix:
# flip the diagonals
# then in one row flip the ends
# WHAT THE FUCKS?!

# Look for that pattern!

class Solution(object):
    def rotate(self, matrix):
