"""
      A
    A B C
  A B C D E
A B C D E F G
"""

for i in range(1,5):
    for j in range(i,4):
        print(" ",end=" ")
    
    for k in range((i*2)-1):
        print(chr(65 + k),end=" ")
    print()    