import numpy as np
import scipy as sp


def pend(y, t, b, c):
	theta, omega = y
	dydt = [omega, -b*omega - c*np.sin(theta)]
	return dydt

