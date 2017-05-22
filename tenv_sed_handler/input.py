"""
Initial functions (simple) to correctly read in the SED files.

"""

import numpy as np
import astropy.table
import astropy.units as u


def read_file_17_SED(filename):
    """ Reads an SED from file, for the spherically symmetric case. """

    # Currently, this requires a workaround because of poor scientific notation formatting.
    try:
        data_array = np.loadtxt(filename)
    except ValueError:
        num_lines = sum(1 for line in open(filename))

        i = 1
        while i < num_lines:
            try:
                data_array = np.loadtxt(filename, skiprows=i)
                break
            except ValueError:
                i += 1               

    return data_array


def tabulate_file_17_SED(data_array):
    table = astropy.table.Table()

    table['index'] = data_array[:,0]
    table['frequency'] = data_array[:,1] * u.Hz
    table['wavelength'] = data_array[:,2] * u.um
    table['H'] = data_array[:,3]
    table['??'] = data_array[:,4]
    table['luminosity'] = data_array[:,5] * u.erg/u.s

    return table


def read_file_cono16_SED(filename):
    """ Reads an SED from file, for the 'cono' case. """

    data = np.loadtxt(filename, skiprows=3)
    return data


def tabulate_file_cono16_SED(data_array):
    table = astropy.table.Table()

    table['frequency'] = data_array[:,0] * u.Hz
    table['wavelength'] = data_array[:,1] * u.um
    table['H'] = data_array[:,2]
    table['??'] = data_array[:,3]
    table['luminosity'] = data_array[:,4] * u.erg/u.s

    return table

