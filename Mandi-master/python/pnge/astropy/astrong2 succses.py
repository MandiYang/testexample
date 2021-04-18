import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.modeling import models, fitting
from astropy.modeling.models import custom_model
from astropy.modeling import Fittable1DModel, Parameter
from astroquery.sdss import SDSS

spectrum = SDSS.get_spectra(plate=1349, fiberID=216, mjd=52797)[0]
spectrum[1].columns
flux = spectrum[1].data['flux']
lam = 10**(spectrum[1].data['loglam'])
#Units of the flux
units_flux = spectrum[0].header['bunit']
print(units_flux)

#Units of the wavelegth

units_wavelength_full = spectrum[0].header['WAT1_001']
print(units_wavelength_full)
units_wavelength = units_wavelength_full[36:]
print(units_wavelength)
plt.plot(lam, flux, color='k')
plt.xlim(6300,6700)
plt.axvline(x=6563, linestyle='--')
plt.xlabel('Wavelength ({})'.format(units_wavelength))
plt.ylabel('Flux ({})'.format(units_flux))
plt.show()
compound_model = models.Gaussian1D(1, 6563, 10) + models.Polynomial1D(degree=1)
fitter = fitting.LevMarLSQFitter()
compound_fit = fitter(compound_model, lam, flux)
plt.figure(figsize=(8,5))
plt.plot(lam, flux, color='k')
plt.plot(lam, compound_fit(lam), color='darkorange')
plt.xlim(6300,6700)
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Flux ({})'.format(units_flux))
plt.show()
