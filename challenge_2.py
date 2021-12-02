class Challenge_2:
   def findNum(self, n):
      input = n
      zeros = 0
      ones = 0

      #count trailing 0s
      while input and not input & 1: #while input is not 0 and input is even
         zeros += 1
         input >>= 1                 #test next bit

      #count trailing 1s
      while input & 1:   #while input is odd
         ones += 1
         input >>= 1     #test next bit
      right = ones + zeros
      n |= 1 << right
      n &= ~((1 << right) - 1)
      n |= (1 << ones - 1) - 1
      return n, bin(n)[2:].zfill(4)

inst = Challenge_2()
val = input("Please enter positive integer:\n")
print("You entered: ", (val ,bin(int(val))[2:].zfill(4)))
print(inst.findNum(int(val)))