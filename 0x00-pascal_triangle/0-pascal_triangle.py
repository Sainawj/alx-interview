def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row from the second to the nth row
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Calculate the values between the first and last 1's
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End each row with 1
        row.append(1)
        # Append the row to the triangle
        triangle.append(row)

    return triangle
