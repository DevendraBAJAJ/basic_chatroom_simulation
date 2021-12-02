class Challenge_2:
   def findNum(self, n):
      input = n
      zeros = 0
      ones = 0

      while input and not input & 1:
         zeros += 1
         input >>= 1

      while input & 1:
         ones += 1
         input >>= 1
      right = ones + zeros
      n |= 1 << right
      n &= ~((1 << right) - 1)
      n |= (1 << ones - 1) - 1
      return n, bin(n)[2:].zfill(4)

inst = Challenge_2()
val = input("Please enter positive integer:\n")
print("You entered: ", (val ,bin(int(val))[2:].zfill(4)))
print("Output: " ,inst.findNum(int(val)))