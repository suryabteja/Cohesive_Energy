from numpy import *
import matplotlib.pyplot as plt                 

################################################################################
# Load data.                                                                   #
################################################################################

a_2, pe_2 = loadtxt('Ni_BCC.dat', unpack=True)

################################################################################
# Plot.                                                                        #
################################################################################

# Start figure.
fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.80,0.80])

# Plot.

#ax.plot(a_2, pe_2, '--', c='g', lw=2, label='BCC Phase')

 

# Add details and save figure.
ax.set_xlabel(r'Lattice distance [Å]')
ax.set_ylabel(r'Potential Energy per atom [eV/atom]')
ax.legend(loc='best', frameon=False)
fig.savefig("fig_free_energy_vs_temperature.png", dpi=300)
