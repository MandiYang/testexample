import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
from astropy.io import fits
from astropy.utils.data import download_file, get_pkg_data_filename
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
#image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
hdu_list = fits.open(image_file)
hdu_list.info()
image_data = hdu_list[0].data
type(image_data)
image_data.shape
hdu_list.close()
plt.imshow(image_data, cmap='gray')
plt.colorbar()
# To see more color maps
# http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
'Min:', np.min(image_data)
'Max:', np.max(image_data)
'Mean:', np.mean(image_data)
'Stdev:', np.std(image_data)
