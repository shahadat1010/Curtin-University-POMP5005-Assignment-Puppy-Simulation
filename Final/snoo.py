"""
task4.py - base simulation for the FOP PracTest3, Sem 1 2024

Written by : Md. Aaqib Chowdhury
Student ID : 22046293

Usage:

Versions:
    - initial version supplied 15/4/24
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import time

from animals import *  # Importing the custom classes and functions from the animals module

# Function to create an empty yard plan
def build_yard(dims):
    plan = np.zeros(dims)
    return plan

# Function to create a yard plan with specific features
def build_yard2(dims):
    plan = np.zeros(dims)
    plan[:100,:] = 5  # General yard area
    plan[0:100,0] = 0  # Pathway
    plan[80:100,0:90] = 0  # Another pathway
    plan[0:100,89] = 0  # Pathway boundary
    plan[0,0:90] = 0  # Pathway boundary
    plan[100:120,0:90] = 10  # Different area of the yard
    plan[20:90,20:70] = 7  # Special yard area
    plan[110:120,0:90] = 0  # Pathway boundary
    return plan

# Function to update the smells in the yard based on the positions of the animals
def update_smells(smells, animals):
    for c in animals: 
        smells[c.pos[0], c.pos[1]] = 10  # Each animal emits a smell at its position
    return smells

# Function to plot the yard on the given axis
def plot_yard(ax, p):
    ax.imshow(p, cmap="nipy_spectral")  # Use a specific color map for visualization

# Function to plot the smells on the given axis
def plot_smells(ax, p):
    ax.imshow(p, cmap="nipy_spectral")  # Use the same color map for smells

# Main function to run the simulation
def main():
    size = (120, 90)  # Define the size of the yard

    yard = build_yard(size)  # Create an empty yard
    smells = np.zeros(size)  # Initialize smells array with zeros
    yard2 = build_yard2(size)  # Create a yard with specific features
    animals = []  # Initialize an empty list for animals

    # Lists of names, colors, and positions for creating puppies
    name_list = ["Snoopy", "Dawg", "Doug", "Big Dawg"]
    colour_list = ["Red", "Blue", "Cyan", "Black"]
    position_list = [(15, 15), (32, 13), (15, 28), (78, 55)]
    for i in range(4):
        animals.append(Puppy(name_list[i], colour_list[i], position_list[i]))  # Add puppies to the animals list

    toys = []  # Initialize an empty list for toys

    # Lists of names, colors, and positions for creating toys
    toy_name_list = ["Ball", "Frisbee", "Bone", "Squeaky Toy"]
    toy_colour_list = ["Green", "Orange", "Brown", "Pink"]
    toy_position_list = [(20, 20), (30, 10), (25, 25), (78, 55)]
    for i in range(4):
        toys.append(Toy(toy_name_list[i], toy_colour_list[i], toy_position_list[i]))  # Add toys to the toys list

    # Lists of names, roles, colors, and positions for creating humans
    name_list = ["Alex", "Joel", "Einstein", "Bro"]
    colour_list = ["brown", "brown", "brown", "brown"]
    role_list = ["owner", "stranger", "owner", "stranger"]
    position_list = [(18, 18), (30, 10), (17, 27), (80, 60)]
    for i in range(4):
        animals.append(Human(name_list[i], role_list[i], colour_list[i], position_list[i]))  # Add humans to the animals list

    # Lists of names, colors, and positions for creating squirrels
    name_list = ["Rockie", "Micky", "Turkey", "Flocky"]
    colour_list = ["lightgreen", "aqua", "crimson", "fuchsia"]
    position_list = [(15, 20), (32, 8), (15, 27), (33, 9)]
    for i in range(4):
        animals.append(Squirrel(name_list[i], colour_list[i], position_list[i]))  # Add squirrels to the animals list

    plt.ion()  # Turn on interactive plotting
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))  # Create a figure with two subplots

    plot_yard(axs[1], yard)  # Plot the empty yard in the second subplot

    for j in range(10):
        for i in animals:
            i.step_change(smells, animals, toys)  # Update each animal's state
        axs[0].set_title(f"Task 4 Simulation: {j+1}")  # Set title for the first subplot
        axs[1].set_title(f"Smells: {j+1}")  # Set title for the second subplot
        plot_yard(axs[0], yard2)  # Plot the detailed yard in the first subplot
        update_smells(smells, animals)  # Update the smells array
        plot_smells(axs[1], smells)  # Plot the smells in the second subplot

        for t in toys:
            t.plot_me(axs[0], size)  # Plot each toy in the first subplot
        for a in animals:
            a.plot_me(axs[0], size)  # Plot each animal in the first subplot
        fig.savefig(f"Step {j+1}.png")  # Save the figure as a PNG file
        if j > 5:
            print("Night time")
        else:
            print("Daytime")
        fig.canvas.draw()  # Draw the canvas
        fig.canvas.flush_events()  # Flush the events
        axs[0].clear()  # Clear the first subplot
        print(f"Step {j}")
        time.sleep(1)  # Pause for 1 second

if __name__ == "__main__":
    main()
