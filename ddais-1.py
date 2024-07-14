import matplotlib.pyplot as plt
arr_1 = []
arr_2 = []
n = int(input("Enter how many colomns that are required :"))
for i in range(n):
    arr_1.append(input("Enter input :"))
m = int(input("Enter how many rows that are required :"))
for i in range(m):
    arr_2.append(input("Enter input :"))
plt.bar(arr_1,arr_2,color = 'magenta')
plt.show()