#VCD CODE ASSIGMENT - ORAL, Talat Cagil - s2210787021

#Import argument parser, math, matplotlib libraties
#copy code
#source: https://docs.python.org/3/library/argparse.html
#source: https://docs.python.org/3/library/math.html
#source: https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py
import argparse
import math
import matplotlib.pyplot as plt
#end copy

#Name of the file:"vcd_oral"
#Step_1: Save the code in local to use argparser
#Step_2: Run the code with desired inputs in console. (Please find the example command code below) 
#runfile('vcd_oral', '--initial_velocity_kmh 50 --mass 1100 --road_type concrete --weather dry --angle 0')

# Creation of a dictionary to store the road coefficient values
road_coefficients = {
    ('concrete', 'dry'): 0.5,
    ('concrete', 'wet'): 0.35,
    ('ice', 'dry'): 0.15,
    ('ice', 'wet'): 0.08,
    ('water', 'aquaplaning'): 0.05,
    ('gravel', 'dry'): 0.35,
    ('sand', 'dry'): 0.3
}

#Set up argparser   
parser = argparse.ArgumentParser()
parser.add_argument('--initial_velocity_kmh', type=float, required=True, help='Initial velocity in km/s')
parser.add_argument('--mass', type=float, required=True, help='Mass of the vehicle in kg')
parser.add_argument('--road_type', type=str, required=True, help='Type of road surface')
parser.add_argument('--weather', type=str, required=True, help='Current weather conditions')
parser.add_argument('--angle', type=float, required=True, help='Angle of the incline (positive for uphill, negative for downhill)')
args = parser.parse_args()

#Define argparser
initial_velocity_kmh = args.initial_velocity_kmh
mass = args.mass
road_type = args.road_type
weather = args.weather
angle = args.angle

#Retrieve the road coefficient value from the dictionary based on the road_type and weather variables
road_coefficient = road_coefficients[(road_type, weather)]

#Define Gravity
g = 9.81  # m/s^2
#Convert the km/h to m/h
initial_velocity = initial_velocity_kmh / 3.6

#Convert the angle to radians
alpha = math.radians(angle)

#Calculation of deceleration
deceleration = road_coefficient * g * math.cos(alpha) + g * math.sin(alpha)

#Create empty lists to store the time and braking distance values
time = [0]
distance = [0]

velocity = [initial_velocity]

#Calculate the braking distance and time at each time step
dt= 0.1 #time step in seconds
while velocity[-1] > 0: # Run the simulation until the vehicle stops
    time.append(time[-1] + dt)
    distance.append(distance[-1] + velocity[-1]*dt)
    velocity.append(max(velocity[-1]-deceleration*dt,0))

#Plot the braking distance over time
plt.plot(time, distance, label="Distance Travelled")
plt.plot(time, velocity, label="Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Braking distance [m], Velocity [m/s]")
plt.legend()
plt.show()

#Print the total braking distance
print("Total distance travelled until vehicle comes to stop:",distance[-1], "[m]")