import matplotlib.pyplot as plt

angle = [2.02, 2.25, 3.00, 3.55, 3.67, 4.00, 4.67, 4.89, 5.31, 5.39, 5.53, 5.711, 6.09] 
sigbm = [10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]

plt.scatter(sigbm, angle)
plt.xlabel("Sigbm")
plt.ylabel("Angle in degrees")
plt.show()
