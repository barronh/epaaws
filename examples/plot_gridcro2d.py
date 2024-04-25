"""
GRIDCRO2D Terrain Height Plot
=============================

This example shows how to create a plot of terrain heigh from one day of EPA MCIP."""


# !python -m pip install git+https://github.com/barronh/epaaws.git
import epaaws

f = epaaws.mp2022.open_gridcro2d('2022-01-01')
levels = [-100, -10, 1, 100, 200, 400, 800, 1600, 3200]
qm = f['HT'].plot(levels=levels, cmap='terrain')
f.csp.cno.drawstates()
qm.figure.savefig('terrain.png')