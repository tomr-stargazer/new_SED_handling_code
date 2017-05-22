"""
Gonna take a specific set of files and plot their SED information. 

There are different inclinations and opening angles.

"""

import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import astropy.constants as c

file_path = os.path.expanduser("~/Documents/Code/Nuria_SED_code/dir_object/cono")

list_of_16s = glob.glob(os.path.join(file_path,"16.*"))
list_of_angle_composites = [x.split('h')[-1] for x in list_of_16s]
list_of_angle_pairs = [x.split('.010.') for x in list_of_angle_composites]

# list_of_opening_angles, list_of_inclinations = []

# set_of_opening_angles = set(list_of_opening_angles)

print( list_of_angle_composites)
print(list_of_angle_pairs)

list_of_opening_angles = [a for (a, b) in list_of_angle_pairs]
list_of_inclinations = [b for (a, b) in list_of_angle_pairs]

set_of_opening_angles = np.sort(list(set(list_of_opening_angles)))
set_of_inclinations = np.sort(list(set(list_of_inclinations)))

fig = plt.figure(figsize=(10,7))

for x, theta in enumerate(set_of_opening_angles):

	for y, i in enumerate(set_of_inclinations):

		relevant_string_bit = 'h'+theta+'.010.'+i
		relevant_filename = [x for x in list_of_16s if relevant_string_bit in x][0]

		relevant_data = np.loadtxt(os.path.join(relevant_filename), skiprows=3)
		wavelength = relevant_data[:,1] * u.um
		luminosity = relevant_data[:,4] * u.erg * u.s**-1
		frequency = relevant_data[:,0] 

		luminosity_lsun = luminosity.to(u.Lsun)

		ax = fig.add_subplot(3,3, 1 + x + 3*y)

		# plt.plot(thing[:,1], thing[:,4]*thing[:,0])
		ax.plot(wavelength, luminosity)
		ax.loglog()
		ax.set_xlim(0.1, 1e4)
		ax.set_xlabel(r"$\lambda$ ($\mu$m)")
		ax.set_ylabel(r"$\nu L_\nu$")


plt.show()
