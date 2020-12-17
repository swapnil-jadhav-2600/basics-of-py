# LIST COMPRESSION CODE
mat = [[1,2,3],
       [4,5,6],
       [7,8,9],
       [8,7,9]]
print(mat)
transpd = []
for i in range(len(mat[0])):
    transpd_row = []
    for row in mat:
        transpd_row.append(row[i])
    transpd.append(transpd_row)
print("Transpose of the matrix  is ",transpd)

# METHOD 2 (LIST COMPRESSION)
trans_mat = [[row[i] for row in mat] for i  in range(len(mat[0]))]
print("Transpose of the matrix  is ",trans_mat)



