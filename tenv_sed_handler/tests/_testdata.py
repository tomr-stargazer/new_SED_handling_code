import numpy as np

valid_data_string_17 = """    14  6.813E+14  4.400E-01  2.175E-92  7.728E-56  5.265E-41
    15  5.451E+14  5.500E-01  4.433E-80  1.575E-43  8.586E-29
    16  4.684E+14  6.400E-01  7.096E-72  2.521E-35  1.181E-20
    17  3.747E+14  8.001E-01  5.704E-60  2.027E-23  7.594E-09
    18  2.998E+14  1.000E+00  2.651E-49  9.419E-13  2.824E+02
    19  2.457E+14  1.220E+00  4.013E-41  1.426E-04  3.503E+10
    20  1.839E+14  1.630E+00  5.272E-32  1.873E+05  3.445E+19"""

rows_17 = [np.fromstring(x, sep=' ') for x in valid_data_string_17.split('\n')]
expected_data_array_17 = np.vstack(rows_17)


valid_data_string_cono16 = """  3.00E+16  9.99E-03  0.00E+00  0.00E+00  0.00E+00
  2.00E+16  1.50E-02  0.00E+00  0.00E+00  0.00E+00
  1.00E+16  3.00E-02  0.00E+00  0.00E+00  0.00E+00
  8.50E+15  3.53E-02  0.00E+00  0.00E+00  0.00E+00
  5.00E+15  6.00E-02  0.00E+00  0.00E+00  0.00E+00
  4.00E+15  7.49E-02  0.00E+00  0.00E+00  0.00E+00
  2.00E+15  1.50E-01  0.00E+00  0.00E+00  0.00E+00
  1.40E+15  2.14E-01  0.00E+00  0.00E+00  0.00E+00
  1.25E+15  2.40E-01  0.00E+00  0.00E+00  0.00E+00
  1.15E+15  2.61E-01  0.00E+00  0.00E+00  0.00E+00
  1.05E+15  2.86E-01  2.48E-06  1.69E-19  6.31E+32
  9.50E+14  3.16E-01  3.03E-06  2.07E-19  6.99E+32
  8.33E+14  3.60E-01  3.81E-06  2.60E-19  7.71E+32
  6.81E+14  4.40E-01  5.39E-06  3.69E-19  8.92E+32"""

rows_cono16 = [np.fromstring(x, sep=' ') for x in valid_data_string_cono16.split('\n')]
expected_data_array_cono16 = np.vstack(rows_cono16)
