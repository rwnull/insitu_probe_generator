# insitu_probe_generator
## Generate HCR-style Probe Pairs for fluorescent in situ mRNA visualization

### What you'll find here:

+ We have intentionally kept the program simple to avoid having many dependencies, however you will need to run Python in terminal or Jupyter. **If you need help with this, see the [NEW_TO_PYTHON_JUPYTER.md](https://github.com/rwnull/insitu_probe_generator/blob/master/NEW_TO_PYTHON_JUPYTER.md) guide.**
+ We are providing the code written in Python 2 and Python 3. Choose the program that matches your version of Python. 
+ Also provided is the code in Jupyter notebook format (.ipynb) (again written in Python 2 or 3).  
  *This is the easiest way to run the program.*

### What you will need to provide:

#### Some naming convention in mind for your output.
##### We like to use a format *Organism_GeneSymbol_ProbePairNumber_Amplifier* where:
  + *Organism* - refers to the species you are working in (we work on a few so it helps us keep things straight).
  + *GeneSymbol* - A way of identifying what gene this probe set FISHes for.
  + *ProbePairNumber* - The total number of pairs of probes this set includes (e.g. 25, 30, or 35)
  + *Amplifier* - Which hairpin amplifier these probes are compatible with (e.g. B1, B2, B3, B4)
  + **Example PdumVasa_25_B2** for *Platynereis dumerilii vasa* 25 probe pairs compatible with the HCR B2 amplifier hairpins.

#### The reverse complement of your cDNA of interest.
  + There are many sites on the web that can do this for you. [Here](https://www.bioinformatics.org/sms/rev_comp.html) is one.
  + This program will not double check that you are using DNA symbols (ATCG). So if you put in U's you'll get U's out. If you use amino acid symbols, you'll get amino acid symbols back.

#### A way to create .XLSX format files
  + This could be MS Excel, Google Sheets, etc. 
  + IDT only allows .XLSX format inputs for [ordering OPools](https://www.idtdna.com/pages/products/custom-dna-rna/dna-oligos/custom-dna-oligos/opools-oligo-pools), so saving as .CSV will not work.
  + This program will spit out a copy-pastable dataframe that IDT will recognize, you just need to supply the .XLSX container.
