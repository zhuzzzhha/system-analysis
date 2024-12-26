import json
import numpy as np

def fill_matrix(matrix):
    ranks = {}
    for index in range(len(matrix)):
        if isinstance(matrix[index], list):
            for elem in matrix[index]:
                ranks[elem] = index
        else:
            ranks[matrix[index]] = index
    
    rank_matrix = []
    for i in range(1,len(ranks) + 1):
        row = []
        for key, name in ranks.items():
            if ranks[key] >= ranks[i]:
                row.append(1)
            else:
                row.append(0)
        rank_matrix.append(row)

    return rank_matrix

def calc_K(matrix_a, matrix_b):
    matrix_a, matrix_b = np.array(matrix_a), np.array(matrix_b)
    Y_AB = matrix_a * matrix_b
    Y_AB_t = matrix_a.transpose() * matrix_b.transpose()
    K = np.logical_or(Y_AB, Y_AB_t)
    print(K)



def main(A, B):
    Y_a = fill_matrix(A)
    Y_b = fill_matrix(B)

    calc_K(Y_a, Y_b)

A = [1,[2,3],4,[5,6,7],8,9,10]
B = [[1,2],[3,4,5,],6,7,9,[8,10]]
main(A, B)


