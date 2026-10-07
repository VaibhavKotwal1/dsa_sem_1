"""
      A
    A   C
  A       E
A B C D E F G
"""
for i in range(1, 5):
    for j in range(i, 4):
        print(" ", end=" ")

    # Prints the hollow structure
    for k in range((i * 2) - 1):
        if i == 4 or k == 0 or k == (i * 2) - 2:
            print(chr(65 + k), end=" ")
        else:
            print(" ", end=" ")  # Prints hollow spaces in the middle
            
    print()

