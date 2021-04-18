import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
#matplotlib inline
from astropy.io import ascii
import astropy.coordinates as coord
import astropy.units as u

tbl = ascii.read("simple_table.csv")
print(tbl)
print(tbl["ra"])

first_row = tbl[0] # get the first (0th) row
ra = coord.Angle(first_row["ra"], unit=u.hour) # create an Angle object
print(ra.degree) # convert to degrees
