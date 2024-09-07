import matplotlib.pyplot as plt

ages=[5,12,18,22,25,27,26,30,34,38,40,42,46,45,47,49,51,56,53,67,68,64,62,70,72,74,76,77,80]
plt.hist(ages, bins=5, color='g' , edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age Ranges')
plt.ylabel('Freequency')

plt.show()
