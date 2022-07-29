print(50+50)
print(100-10)
print("SyntaxError")
print(6**6)
print(6+6+6+6+6+6)
print("Hello World")
print("Hello World : 10")

P = 800000
R = .06
M = 10000

Rate = P * (R/12)

L = 0
while P > 0:
    P = P + Rate - M
    Rate = round(P * (R/12))
    L += 1

print(L)
