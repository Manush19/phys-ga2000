import matplotlib.pyplot as plt
import numpy as np

def gaussian(mu, sigma, x):
	"""
	Function which returns the 1D-gaussian probablility distribution:
	------------
	Parameters: 
		mu:	(float) mean value of the gaussian
		sigma: (float) standard deviation of the gaussian
		x: (1-D numpy.ndarray) x values where the pdf is required
	-----------
	Returns:
		A 1-D array of gaussian pdf values corresponding to x  
	"""
	return (1./(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/sigma)**2)
	
	
mean = 0. # mean given in the problem
stdv = 3. # standard deviation of the problem
min_range, max_range = -10., 10. # range

x = np.linspace(min_range, max_range, 300) # x values for plotting gaussian curve
gauss = gaussian(mean, stdv, x)

# CHECKING THE NORMALIZATION OF THE GAUSSIAN DISTRIBUTION
norm = np.trapz(gauss, x)
print (f"Total area under the curve = {norm:.1f}")

# PLOTTING
plt.plot(x, gauss, label=f'mean = {mean}\nstd. dev = {stdv}')
plt.xlabel('x')
plt.ylabel('p.d.f')
plt.legend(title = 'Gaussian')
plt.savefig('./gaussian.png', bbox_inches='tight', dpi=300) 
