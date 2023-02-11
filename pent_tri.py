import numpy as np

# Define the function to calculate the residuals
def residuals(x, sensors, distances):
    residual = np.zeros(len(sensors))
    for i in range(len(sensors)):
        residual[i] = np.sqrt((x[0] - sensors[i][0])**2 + (x[1] - sensors[i][1])**2) - distances[i]
    return np.linalg.norm(residual)
