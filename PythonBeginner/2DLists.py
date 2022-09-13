matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
print(matrix)
for row in matrix:
    output=''
    for number in row:
        output+=f'{number} '
    print(output)