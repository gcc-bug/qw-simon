import numpy as np
import argparse

def to_binary_vector(num, length):
    """Convert an integer to a binary vector of a given length."""
    return [int(bit) for bit in format(num, f'0{length}b')]

def gaussian_elimination_mod2(matrix):
    """Perform Gaussian elimination on the matrix modulo 2."""
    rows, cols = matrix.shape
    for i in range(rows):
        # Ensure the pivot element is 1. If not, swap with a row below that has a 1 in this column
        if matrix[i, i] == 0:
            for j in range(i + 1, rows):
                if matrix[j, i] == 1:
                    matrix[[i, j]] = matrix[[j, i]]
                    break
        # Eliminate the column below the pivot
        for j in range(i + 1, rows):
            if matrix[j, i] == 1:
                matrix[j] = (matrix[j] + matrix[i]) % 2

def find_non_trivial_solution(matrix):
    """Find a non-trivial solution to the system of equations represented by the matrix."""
    rows, cols = matrix.shape
    free_variables = []

    # Identify free variables (columns with no pivots)
    for col in range(cols - 1):
        if np.count_nonzero(matrix[:, col]) == 0:
            free_variables.append(col)

    if not free_variables:
        return np.zeros(cols - 1, dtype=int)
    
    # Set the first free variable to 1 to find a non-trivial solution
    solution = np.zeros(cols - 1, dtype=int)
    solution[free_variables[0]] = 1
    
    # Back substitution to adjust dependent variables
    for i in range(rows - 1, -1, -1):
        pivot_col = np.argmax(matrix[i, :cols - 1])
        if matrix[i, pivot_col] == 1:
            solution[pivot_col] = (matrix[i, -1] - np.dot(matrix[i, :cols - 1], solution)) % 2
    
    return solution

def simons_algorithm(measurements, bit_length):
    """Main function to solve Simon's problem."""
    # Convert measurements to binary vectors
    binary_measurements = np.array([to_binary_vector(m, bit_length) for m in measurements])
    # Append a zero column (right-hand side of equations)
    augmented_matrix = np.hstack([binary_measurements, np.zeros((len(measurements), 1), dtype=int)])

    # Perform Gaussian elimination
    gaussian_elimination_mod2(augmented_matrix)
    # Find and return the non-trivial solution
    non_trivial_solution = find_non_trivial_solution(augmented_matrix)

    return non_trivial_solution

def main():
    parser = argparse.ArgumentParser(description="Simon's Algorithm")
    parser.add_argument("measurements", type=int, nargs='+', help="List of integers representing the measurements.")
    parser.add_argument("bit_length", type=int, help="Length of the bit strings.")
    args = parser.parse_args()

    print(f"输入非平凡解：{args.measurements}，应编码为{args.bit_length}位")
    result = simons_algorithm(args.measurements, args.bit_length)
    print("Non-trivial solution:", result)

if __name__ == "__main__":
    main()
