def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Sum of the two numbers above
        row.append(1)  # End each row with 1
        triangle.append(row)
    
    return triangle

# Test the function
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))

# Additional test cases
print_triangle(pascal_triangle(0))  # Expected output: []
print_triangle(pascal_triangle(1))  # Expected output: [1]
print_triangle(pascal_triangle(2))  # Expected output: [1], [1, 1]
print_triangle(pascal_triangle(3))  # Expected output: [1], [1, 1], [1, 2, 1]
print_triangle(pascal_triangle(4))  # Expected output: [1], [1, 1], [1, 2, 1], [1, 3, 3, 1]
print_triangle(pascal_triangle(5))  # Expected output: [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]
