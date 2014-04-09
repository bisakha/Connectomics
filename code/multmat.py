def  matrixmult (A, B):
    matsum = 0
    
    for i in range(int(A.T.shape[0])):
            #for j in range(int(B.shape[1])):
               matsum = matsum + A.T[i][0]*B[0][i]
               #print matsum
    return matsum
      
