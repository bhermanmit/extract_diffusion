#!/usr/bin/env python2

import statepoint as sp
import sys

# Get file name from command line
filename = sys.argv[1]

# Process statepoint file
sph = sp.StatePoint(filename)
sph.read_results()

# Extract data
flux1 = sph.get_value(1, [('energyin',2)], 1)
flux2 = sph.get_value(1, [('energyin',1)], 2)
print flux1, flux2
