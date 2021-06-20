x = [2,3,5,6,8]
y = [1,6,22,33,61]
x_2 = list()
x_3 = list()
x_4 = list()
x_carpi_y = list()
x_2_carpi_y = list()


for i in x:
    x_2.append(int(pow(i,2)))
    x_3.append(int(pow(i,3)))
    x_4.append(int(pow(i,4)))


print("xi : ", x, sum(x))
print("xi^2 : ", x_2, sum(x_2))
print("xi^3 : ", x_3, sum(x_3))
print("xi^4 : ", x_4, sum(x_4))

for i, j, z in zip(x, y, x_2):
    x_carpi_y.append(i*j)
    x_2_carpi_y.append(z*j)

print()
print("yi : ", y, sum(y))
print("xi.yi : ", x_carpi_y, sum(x_carpi_y))
print("xi^2.yi : ", x_2_carpi_y, sum(x_2_carpi_y))
