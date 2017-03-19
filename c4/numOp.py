##
a = 3.0 % .7
b = 3.0 // .7
c = 3.0 - b * .7

a == c

a = 7 % 3
b = 7 // 3
c = 7 - b * 3

a == c

## chained operator

x = 2
y = 3
z = 4

x < y < z # is equivalent to:
x < y and y < z

x < y > z # is equivalent to:
x < y and y > z

## operation on sequences

a = [1, 2, 3]

n = 2

a * 2

s = "god"
n = 3
s * n
n * s

a, b, c = s # value unpack
a

a = [1,2,3]
sum(a, 4) # 4 is the initial value

## shalow copies

a = [3, 4, 5]

b = [a]
