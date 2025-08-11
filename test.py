origin_matrix = [[1,2,3], [4,5,6], [7,8,9]]
reverse_matrix = list(map(list,zip(*origin_matrix)))
rotate_90_clockwise_matrix = list(zip(*origin_matrix[::-1]))
print(rotate_90_clockwise_matrix)