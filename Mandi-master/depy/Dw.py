import matplotlib.pyplot as plt
import tarfile
from astropy.utils.data import download_file
import tbdump
url = 'http://data.astropy.org/tutorials/UVES/data_UVES.tar.gz'
f = tarfile.open(download_file(url, cache=True), mode='r|*')
working_dir_path = '.'  # CHANGE TO WHEREVER YOU WANT THE DATA TO BE EXTRACTED
f.extractall(path=working_dir_path)
from glob import glob
import os

import numpy as np

from astropy.wcs import WCS
from astropy.io import fits

# os.path.join is a platform-independent way to join two directories
globpath = os.path.join(working_dir_path, 'UVES/*.fits')

print(globpath)
# glob searches through directories similar to the Unix shell
filelist = glob(globpath)

# sort alphabetically - given the way the filenames are
# this also sorts in time
filelist.sort()
sp = fits.open(filelist[0])
sp.info()
header = sp[0].header

wcs = WCS(header)
