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

from animals import *




def build_yard(dims):
    plan = np.zeros(dims)
    return plan

def build_yard2(dims):
    plan = np.zeros(dims)
    plan[:100,:] = 5
    plan[0:100,0] = 0
    plan[80:100,0:90] = 0  
    plan[0:100,89] = 0
    plan[0,0:90] = 0
    plan[100:120,0:90] = 10 
    plan[20:90,20:70] = 7
    plan[110:120,0:90] = 0
    return plan
   
def update_smells(smells, animals):
    for c in animals: 
        smells[c.pos[0], c.pos[1]] = 10
    return smells

def plot_yard(ax, p):
    ax.imshow(p, cmap = "nipy_spectral")

def plot_smells(ax, p):
    ax.imshow(p, cmap = "nipy_spectral_r")


def main():
    size = (120,90)

    yard = build_yard(size)
    smells = np.zeros(size)
    yard2 = build_yard2(size)
    animals= []
    name_list = ["Snoopy","Dawg","Doug","Big Dawg"]
    colour_list = ["Red","Blue","Cyan","Black"]
    position_list = [(15,15),(32,13),(15,28),(78,55)]
    for i in range(4):
        animals.append(Puppy(name_list[i], colour_list[i],position_list[i]))
    
    toys= []
    toy_name_list = ["Ball", "Frisbee", "Bone", "Squeaky Toy"]
    toy_colour_list = ["Green", "Orange", "Brown", "Pink"]
    toy_position_list = [(20, 20), (30, 10), (25, 25), (78,55)]

    for i in range(4):
        toys.append(Toy(toy_name_list[i], toy_colour_list[i], toy_position_list[i]))

    name_list = ["Alex","Joel","Einstein","Bro"]
    colour_list = ["brown","brown","brown","brown"]
    role_list=["owner","stranger","owner","stranger"]
    position_list = [(18,18),(30,10),(17,27),(80,60)]
    for i in range(4):
        animals.append(Human(name_list[i],role_list[i], colour_list[i],position_list[i]))     

    
    name_list = ["Rockie","Micky","Turkey","Flocky"]
    colour_list = ["lightgreen","aqua","crimson","fuchsia"]
    position_list = [(15,20),(32,8),(15,27),(33,9)]
    for i in range(4):
        animals.append(Squirrel(name_list[i], colour_list[i],position_list[i]))   

    plt.ion()
    fig, axs = plt.subplots(1,2,figsize=(15,10))

    plot_yard(axs[1], yard)
    for j in range(10):
        for i in animals:
            i.step_change(smells, animals, toys)  
        axs[0].set_title(f"Task 4 Simulation: {j+1}")
        axs[1].set_title(f"Smells: {j+1}")
        plot_yard(axs[0], yard2)
        update_smells(smells, animals)
        plot_smells(axs[1], smells)

        for t in toys:
            t.plot_me(axs[0], size)
        for a in animals:
            a.plot_me(axs[0], size)
        fig.savefig(f"Step {j+1}.png")
        if j>5 : 
            print("Night time")
        else: 
            print("Daytime")
        fig.canvas.draw()
        fig.canvas.flush_events()
        axs[0].clear()
        print(f"Step {j}")
        time.sleep(1)

if __name__ == "__main__":
    main()
