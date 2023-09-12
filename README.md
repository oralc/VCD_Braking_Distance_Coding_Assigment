# VCD_Assigment - ORAL Cagil / 2210787021<br />

**Time-based Simulation of Braking Distance**<br />

_Spyder - (Python 3.7)_<br />

**How to Run:**<br />
Step_1: Please, save the code locally to use argparser<br />
Step_2: Run the code with desired inputs in the console. (Please find the example command code below)<br />
E.g: runfile('vcd_code.py', '--initial_velocity_kmh 50 --mass 1100 --road_type concrete --weather dry --angle 0')<br /><br />

**Input Data:**<br />
  angle: Positive for uphill || Negative for downhill)<br />
  road_type: concrete, ice, water, gravel, sand<br />
  weather: dry, wet, aquaplaning<br />
  initial_velocity_kmh: initial velocity in km/h<br />
  mass: mass of the vehicle<br /><br /><br />

**Algoritmh**:<br />
  The code calculates the distance traveled and the decrease in velocity in the time step until the vehicle comes to stop with a while loop.<br />
  Then, it plots the velocity and distance as a time-based simulation.<br /><br /><br />
  
