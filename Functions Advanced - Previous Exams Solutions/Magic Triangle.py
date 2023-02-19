def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        list_ = [1]
        counter = 0
        for j in range(1, i):
            list_.append(triangle[i - 1][counter] + triangle[i - 1][counter + 1])
            counter += 1
        list_.append(1)
        triangle.append(list_)
    return triangle