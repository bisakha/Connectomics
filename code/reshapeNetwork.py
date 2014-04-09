#### Author: Bisakha Ray, Javier Orlandi and Olav Stetter.




def reshapeNetwork(network):
    y_true = []
    for i in range(len(network)):
       for j in range(len(network[0])):
          #if network[i][j] == int(1):
          if network[i][j] == int(1):  
              y_true.append(int(1))
          else:                           
             y_true.append(int(0))
    return y_true

