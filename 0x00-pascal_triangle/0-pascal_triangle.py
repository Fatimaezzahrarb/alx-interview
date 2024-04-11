#!/usr/bin/python3
""" Creates a function that returns a lits of lists """


def pascal_triangle(n):
    """ creates pascal triangle
    n:
        number of rows
    return:
        Pascal triangle """
    new_pascal = []

    """ Assuming n is an integer """
    if n <= 0:
        return new_pascal

    for i in range(n):
        row_index = [1]
        if new_pascal:
            final_row = new_pascal[-1]
            row_index.extend([sum(pair) for pair in
                              zip(final_row, final_row[1:])])
            row_index.append(1)
        new_pascal.append(row_index)
    return (new_pascal)
