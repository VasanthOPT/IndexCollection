def indexSet(x):
  n=len(x)
  IndexCollect=[]
  for j in range(n):
    a_j=x[j]
    IndexCollect.append(j)
  print(IndexCollect)
Alphabets=['A', 'B', 'A', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
indexSet(Alphabets)
# in this list Alphabets 'A' occurs three times in the place 0, 2 and 10 but the function forms the index correctly
#standard ouput
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    
  
