def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows of the triangle to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the triangle as an empty list
    triangle = []

    # Loop through each row
    for row_num in range(n):
        # Start each row with 1
        row = [1]

        if row_num > 0:
            # Get the previous row for reference
            previous_row = triangle[row_num - 1]
            # Calculate the intermediate values of the row
            for j in range(1, row_num):
                row.append(previous_row[j - 1] + previous_row[j])

            # End each row with 1
            row.append(1)

        # Add the row to the triangle
        triangle.append(row)

    return triangle
