vector1 = [1,2,3]
vector2 = [-1,0,2]
productv1 = 1
productv2 = 0
scalarProduct = 0

for valor in vector1:
    productv1 *= valor

for valor in vector2:
    productv2 *= valor

print("El producto de vector 1 es", productv1)
print("El producto de vector 2 es", productv2)

scalarProduct = productv1 + productv2
print("El producto escalar es:", scalarProduct)