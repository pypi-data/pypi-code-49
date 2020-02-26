import matplotlib.pyplot as plt

# squares = [1,4,9,16,25]
# plt.plot(squares,linewidth=5)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of value', fontsize=14)
plt.tick_params(axis='both',labelsize=14)

# plt.show()
plt.scatter([1,2,3,4,5],[1,4,9,16,25], s=200);
# plt.show()

yvalues = [x**2 for x in range(1,6)]
print(yvalues)

# plt.axis([0,6,0,50])
# plt.show()