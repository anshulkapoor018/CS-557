import numpy as np

del_cost = 1
ins_cost = 1
sub_cost = 2

def calculate_minimum_edit_distance(source, target):
    n = len(source)
    m = len(target)
    med_matrix = np.zeros((n + 1, m + 1), dtype='int32')
    for i in range(1, n + 1):
        med_matrix[i][0] = med_matrix[i - 1][0] + del_cost
    for i in range(1, m + 1):
        med_matrix[0][i] = med_matrix[0][i - 1] + del_cost
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if source[i - 1] == target[j - 1]:
                med_matrix[i][j] = min([med_matrix[i - 1][j] +
                                        del_cost, med_matrix[i - 1][j - 1] + 0,
                                        med_matrix[i][j - 1] + ins_cost])
            else:
                med_matrix[i][j] = min([med_matrix[i - 1][j] +
                                        del_cost, med_matrix[i - 1][j - 1] +
                                        sub_cost, med_matrix[i][j - 1] + ins_cost])
    return med_matrix[n][m]


def main():
    """ Main function which is used as an interface """
    source = "drive"
    min_edit_distance_brief = calculate_minimum_edit_distance(source, "brief")
    min_edit_distance_divers = calculate_minimum_edit_distance(source, "divers")

    print(min_edit_distance_brief, min_edit_distance_divers)


if __name__ == '__main__':
    main()
