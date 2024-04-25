.. epaaws documentation master file, created by
   sphinx-quickstart on Thu Apr 25 10:01:17 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to epaaws's documentation!
==================================

`epaaws` is a library of functions to facilitate analysis of EPA's data on
AWS S3 buckets thru Amazon's Registry of Open Data.[1] At present, this only
includes the epa-2022-modeling-platform (see module mp2022). For more
information, see the  `documentation pages <https://barronh.github.io/epaaws>`_.

Citations:
1. https://registry.opendata.aws/epa-2022-modeling-platform/

Install for Python3
-------------------

.. code-block:: sh

    python -m pip epaaws

Example
-------

Example of how to plot the terrain height from a GRIDCRO2D file.

.. code-block:: python

    import epaaws

    f = epaaws.mp2022.open_gridcro2d('2022-01-01')
    levels = [-100, -10, 1, 100, 200, 400, 800, 1600, 3200]
    f['HT'].plot(levels=levels, cmap='terrain')
    f.csp.cno.drawstates()


Issues
------

If you're having any problems, open an issue on github.

https://github.com/barronh/epaaws/issues


Quick Links
-----------

* :doc:`auto_examples/index`
* :doc:`api/epaaws`


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Table of Contents

   self
   auto_examples/index
   api/epaaws
   api/modules