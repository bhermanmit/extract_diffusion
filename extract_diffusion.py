#!/usr/bin/env python2

import statepoint as sp
import sys

# Get file name from command line
filename = sys.argv[1]

# Process statepoint file
sph = sp.StatePoint(filename)
sph.read_results()

# Extract data
n = sph.current_batch - sph.n_inactive
flux1 = sph.get_value(0, [('energyin', 1)], 0)[0]/float(n)
flux2 = sph.get_value(0, [('energyin', 0)], 0)[0]/float(n)
totalrr1 = sph.get_value(0, [('energyin', 1)], 1)[0]/float(n)
totalrr2 = sph.get_value(0, [('energyin', 0)], 1)[0]/float(n)
p1scattrr1 = sph.get_value(0, [('energyin', 1)], 2)[0]/float(n)
p1scattrr2 = sph.get_value(0, [('energyin', 0)], 2)[0]/float(n)
scattrr11 = sph.get_value(1, [('energyin', 1), ('energyout', 1)], 0)[0]/float(n)
scattrr12 = sph.get_value(1, [('energyin', 1), ('energyout', 0)], 0)[0]/float(n)
scattrr21 = sph.get_value(1, [('energyin', 0), ('energyout', 1)], 0)[0]/float(n)
scattrr22 = sph.get_value(1, [('energyin', 0), ('energyout', 0)], 0)[0]/float(n)
nufissrr11 = sph.get_value(1, [('energyin', 1), ('energyout', 1)], 1)[0]/float(n)
nufissrr12 = sph.get_value(1, [('energyin', 1), ('energyout', 0)], 1)[0]/float(n)
nufissrr21 = sph.get_value(1, [('energyin', 0), ('energyout', 1)], 1)[0]/float(n)
nufissrr22 = sph.get_value(1, [('energyin', 0), ('energyout', 0)], 1)[0]/float(n)

# Compute xs
totalxs1 = totalrr1/flux1
totalxs2 = totalrr2/flux2
p1scattxs1 = p1scattrr1/flux1
p1scattxs2 = p1scattrr2/flux2
scattxs11 = scattrr11/flux1
scattxs12 = scattrr12/flux1
scattxs21 = scattrr21/flux2
scattxs22 = scattrr22/flux2
nufissxs11 = nufissrr11/flux1
nufissxs12 = nufissrr12/flux1
nufissxs21 = nufissrr21/flux2
nufissxs22 = nufissrr22/flux2

# Compute negative absorption xs
absxs1 = totalxs1 - scattxs11 - scattxs12
absxs2 = totalxs2 - scattxs22 - scattxs21

# Compute effective downscatter xs
effscattxs12 = scattxs12 - scattxs21*flux2/flux1


# Nu fission xs
nufissxs1 = nufissxs11 + nufissxs12
nufissxs2 = nufissxs22 + nufissxs21

# Diffusion coefficient
diff1 = 1.0/(3.0*(totalxs1 - p1scattxs1))
diff2 = 1.0/(3.0*(totalxs2 - p1scattxs2))

# Print out results
print "Thermal Absorption XS: {0}".format(absxs2)
print "Fast Absorption XS: {0}".format(absxs1)
print "Thermal Nu-Fission XS: {0}".format(nufissxs2)
print "Fast Nu-Fission XS: {0}".format(nufissxs1)
print "Effective Downscatter XS: {0}".format(effscattxs12)
print "Thermal Diffusion Coefficient: {0}".format(diff1)
print "Fast Diffusion Coefficient: {0}".format(diff2)
