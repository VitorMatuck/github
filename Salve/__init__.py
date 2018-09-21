n1= float(input("digite um numero: "))
n2= float(input("digite um numero: "))
n3= float(input("digite um numero: "))

if n1>n2>n3:
    print("O maior número é",n1,"e o menor número é",n3)

if n1>n3>n2:
    print("O maior número é",n1, "e o menor número é",n2)

if n2>n1>n3:
    print("O maior número é", n2, "e o menor número é", n3)
if n2>n3>n1:
    print("O maior número é", n2, "e o menor número é", n1)
if n3>n2>n1:
    print("O maior número é", n3, "e o menor número é", n1)
if n3>n1>n2:
    print("O maior número é", n3, "e o menor número é", n1)

