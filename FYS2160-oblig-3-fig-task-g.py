import numpy as np
import matplotlib.pyplot as plt

def n_over_N(T, deltaEps=1.):
	k = 8.6173324e-5 #eV/K (Boltzmanns constant) 
	return np.exp(-deltaEps/(k*T))

def C_v_over_N(T, deltaEps=1.):
	k = 8.6173324e-5 #eV/K (Boltzmanns constant)
	return deltaEps**2/(k*T**2)*n_over_N(T, deltaEps)

deltaEps = 1.0 # eV

T = np.linspace(0, 1000, 10000)
plt.plot(T, n_over_N(T)*1e5)
plt.xlabel('Temperature $T$ / K')
plt.ylabel('Concentration of vacancies $n/N \cdot 10^5$')
plt.savefig('FYS2160-oblig-3-fig-conc-n-T.pdf')


plt.figure(1)
plt.plot(T, C_v_over_N(T))
plt.show(1)