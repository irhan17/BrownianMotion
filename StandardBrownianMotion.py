#Name: Irhan Iftikar
#Date: January 2025
#Description: Simulation of a standard Brownian motion
#Source: https://www.quantstart.com/articles/brownian-motion-simulation-with-python/

#Imports Matplotlib and Numpy for visualization and quantitative computations
import matplotlib.pyplot as plt
import numpy as np

#Generates a random seed value
rng = np.random.default_rng()

#Defines an arbitrarily chosen number of paths and number of time steps per path
paths = 100
points = 1000

#For a standard Brownian motion, drift (mu) is zero and volatility (sigma) is one
mu, sigma = 0, 1

#Draws samples from a normal distribution and stores them in a matrix where number of rows = paths and number of columns = points
Matrix = rng.normal(mu, sigma, (paths, points))

#Defines a time interval with equal step sizes
interval = [0.0, 1.0]
dt = (interval[1] - interval[0]) / (points - 1)

#Creates a linear space axis that takes the interval and creates equally spaced points
t_axis = np.linspace(interval[0], interval[1], points)

#Implements a recursion formula that sets the next path values for each point
W = np.zeros((paths, points))
for idx in range(points - 1):
    real_idx = idx + 1
    W[:, real_idx] = W[:, real_idx - 1] + np.sqrt(dt) * Matrix[:, idx]

#Plots the graph 
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
for path in range(paths):
    ax.plot(t_axis, W[path, :])
ax.set_title("Standard Brownian Motion - Irhan Iftikar")
ax.set_xlabel("Time")
ax.set_ylabel("Asset Value")
plt.show()