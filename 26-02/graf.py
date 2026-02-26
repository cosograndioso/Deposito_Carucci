import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
def graf(x, y, x_label, y_label, title):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.show()
    
    
    
graf([1, 2, 3, 4, 5], [10, 20, 30, 40, 50], 'X-axis', 'Y-axis', 'Sample Graph')


x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='blue', marker='o')     
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()