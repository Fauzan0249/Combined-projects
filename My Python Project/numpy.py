'''Introduction and Basics

In this lab, we will use the Numpy library to overcome the "slowness" and "manual operation" issues of
standard python lists in medical data processing, and the Matplotlib library to visualize data just like in
medical monitors.

Why NumPy instead of lists?
. Lists (Pill Organizer Analogy): Great for storing items in order (e.g, patient names), but inefficient for mathematical operations.
. NumPy Arrays (Vector Power): Optimized for processing medical signals.
    . Speed: Much faster than lists (written in C) and performs  instant operations on the entire dataset without writing loops.
    
    . Precision Timing: The np.linspace(start, stop, number) command creates data points that fit perfectly into a specific time duration for medical sampling.
    
    
    . Automatic statistics: Functions like np.mean(avaerage) and np.max(peak value) analyze thousands of data points in a single line.
    
    
Data Visualization (Matplotlib)

It converts numerical data processed with NumPy into graphs that you can interpret.

   . Labels: Without Xlabel, Ylabel, and title, graphs are dangerous "mystery signals" in a medical context.
   . Grids: the plt.grid(True) command turns the graph from a single picture into a precise "measurement tool."'''



# Preparation and Example Codes
#Example A: Manual List vs Automatic NumPy
#Observe that when trying to do math with lists, the data is copied (repeated), whereas NumPy performs the actual mathematical calculation.


import numpy as np

#---1. Python List (Manual/Incorect Method)---
voltages_list = [0.5, 0.8, 1.2]
print("Normal List Multiplicaion x2:")
print(voltages_list *2)
# Output: [0.5, 0.8, 1.2, 0.5, 0.8, 1.2] (Repeats the list, does not multiply!)



#---2. MunPy Array (Correct/ Automatic Method) ---
voltages_array = np.array ([0.5, 0.8, 1.2])
print("NumPy Array Multiplication (x2):")
print(voltages_array *2)
#Output: [1.0 1.6 2.4] (Perfrorms mathemtical multiplication)



#Example B: Medical Statistics (Peak Detection)
#Find the average of data taken from a patient monitorand determine when the highest value occurred.

import numpy as np

#simulated blood pressure readings
bp_readings = np.array ([110, 125, 142, 118, 115])

average_bp = np.mean (bp_readings)     #average
max_bp = np.max(bp_readings)           #Peak Value
max_index = np.argmax(bp_readings)     #Index of the Peak  value


print(f"Average: {average_bp}")
print(f"Highest value: {max_bp}")
print(f"Index of highest value: {max_index}")



#Example C: Basic Signal Plotting
#Draw a signal professionally with its labels and gridlines

import numpy as np
import matplotlib.pyplot as plt

# Create 100 points between 0 and 10 seconds
 

time = np.linspace(0, 10, 100)
signal = np.sin(time)


plt.fiure(figsize=(8, 4))
plt.plot(time, signal, color ='blue', label = 'Respiration')


# Medical labels (mandatory)
plt.title("Patient Respiration Rythm")
plt. xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show( )   # Show the graph