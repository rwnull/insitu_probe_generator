# insitu_probe_generator 
## Generate HCR-3.0-style Probe Pairs for fluorescent *in situ* mRNA visualization

## [Ozpolat lab](https://bduyguozpolat.org)


### Intention of this program:

We were excited to venture into the realm of quick, easy, mutliplexable *in situ* hybridizations presented by the Hybridization Chain Reaction methodology (Choi et al. Development 2018) . We wanted a budget-friendly way of exploring gene expression, that allowed for complete control over probe design, while allowing us to also know the exact sequences of our probes to aid publication and reproducibility. As a result, we wrote this program to allow us ease of ordering probes that mesh with the published HCR system of reaction and amplification reagents.

### What you'll find here:

+ We have intentionally kept the program simple to avoid having many dependencies, however you will need to run Python in terminal or Jupyter. **If you need help with this, see the [NEW_TO_PYTHON_JUPYTER.md](https://github.com/rwnull/insitu_probe_generator/blob/master/NEW_TO_PYTHON_JUPYTER.md) guide.**
+ We are providing the code written in Python 2 and Python 3. Choose the program that matches your version of Python. 
+ Also provided is the code in Jupyter notebook format (.ipynb) (again written in Python 2 or 3).  
  *This is the easiest way to run the program.*

### What you will need to provide:

#### Some naming convention in mind for your output.
##### We like to use a format *Amplifier_Organism_GeneSymbol_ProbePairNumber* where:
  + *Amplifier* - Which hairpin amplifier these probes are compatible with (e.g. B1, B2, B3, B4)
  + *Organism* - refers to the species you are working in (we work on a few so it helps us keep things straight).
  + *GeneSymbol* - A way of identifying what gene this probe set FISHes for.
  + *ProbePairNumber* - The total number of pairs of probes this set includes (e.g. 25, 30, or 35)
  + **Example B2_PdumVasa_25** for 25 pairs of probes to *Platynereis dumerilii vasa* compatible with the B2 amplifier hairpins.

#### The reverse complement of your cDNA of interest.
  + There are many sites on the web that can do this for you. [Here](https://www.bioinformatics.org/sms/rev_comp.html) is one.
  + This program will *not* double check that you are using DNA symbols (ATCG). You can type in Homer's Iliad if you like, and you will get back probes pertaining to Nereids, but they won't really help you search for the mRNA of your organism's various Argonauts.

#### A way to create .XLSX format files
  + This could be MS Excel, Google Sheets, etc. 
  + IDT only allows .XLSX format inputs for [ordering OPools](https://www.idtdna.com/pages/products/custom-dna-rna/dna-oligos/custom-dna-oligos/opools-oligo-pools), so saving as .CSV will not work.
  + This program will spit out a copy-pastable dataframe that IDT will recognize, you just need to supply the .XLSX container. You can need to use the ["split text into columns" function](https://support.office.com/en-us/article/split-text-into-different-columns-with-the-convert-text-to-columns-wizard-30b14928-5550-41f5-97ca-7a3e9c363ed7) to separate the columns using "comma" as the delimiter. 
