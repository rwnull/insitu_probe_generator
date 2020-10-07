# HELP! Where do I start?! I want to make my own HCR probes but am not a programmer.

We feel you, we're not particularly gifted with programming either. Here's what you need to do to make the most of this program:

1. You will have to have Python on your machine. 
  + Python comes in a few versions: 
    1. Python 2 is an older release but because it was around for a long time many libraries have been written for it. Eventually however, it is going to be phased out and no longer supported. Starting with HCRProbeMakerv0.3.0 we also no longer will utilize Python2.
    2. Python 3 is the newer version that will continue to be developed and supported. This is what you need to have installed to be able to run HCRProbeMaker from version 0.3.0 on.
  + [Anaconda](https://docs.continuum.io/anaconda/install/) is a helpful Python environment that will let you install Python3 and R, as well as make installing add-on programs easier.
  + The Anaconda Navigator will help you install the dependencies needed to run HCRProbeMaker (Biopython, Numpy, and Pandas) under the tab "Environments".
    1. Click the "Environments" tab
    2. If no environment available, click the "New" button at the bottom.
    3. Search for the dependencies in the "Search Packages" bar, ensure that the dropdown menu nearby reads "All" or "Uninstalled".
    4. Once found, click the check box next to the library's name and follow instructions to install it.
    5. After installiing all of the dependencies (BLAST not included), return to the "Home" tab and launch the "Jupyter Notebook" application.
    6. A web page should open to your root directory, navigate to the "UserInterface_v#.#.#.ipynb" file and double click it to launch the notebook. 

2. We wrote our HCR probe maker with an interactive interface, [Jupyter](https://jupyter.org/index.html), in mind.
  + See step 1 if you don't have Python installed on your machine.
  + To get Jupyter follow this [guide.](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
  + Once installed, you can run the ".ipynb" programs, which will automatically reference the ".py" files.
