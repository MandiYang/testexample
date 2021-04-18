import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt

from astropy.io import fits
from astropy.utils.data import download_file, get_pkg_data_filename
#image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )
image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
hdu_list = fits.open(image_file)
hdu_list.info()
image_data = hdu_list[0].data
print(type(image_data))
print(image_data.shape)
hdu_list.close()
plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.show()
# To see more color maps
# http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))
