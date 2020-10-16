def find_greatest_common_denominator(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def countBlackCells(n, m):
    gcd = find_greatest_common_denominator(n, m)
    line_cells = n + m - gcd
    line_corner_cells = (gcd - 1) * 2
    return line_cells + line_corner_cells