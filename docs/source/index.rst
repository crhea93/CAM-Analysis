Welcome to Cognitive Affective Map Analysis Package's documentation!
====================================================================

The primary use of this repository is to clean and analyse CAM data downloaded from the Valence software.

Data exported from Valence will come as a zip file containing the node/link list and information in the form of
two files: *_blocks.csv and *_links.csv

The code presented here executes three primary functions:
 - Clean the CAM Data
    - To clean the data, update the Clean_CAMS.py file inputs and run 'python Clean_CAMS.py'
 - Construct CAM Images
    - To construct CAM Images, update Data-to-Plot.py file inputs and run 'python Data-to-Plot.py'
 - Run CAM Statistics (summary and individual)
    - To run statistics, update Summary-Stats.py file inputs and run 'python Summary-Stats.py'




.. toctree::
   :maxdepth: 2
   :caption: Contents:

   cleaning
   stats


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
