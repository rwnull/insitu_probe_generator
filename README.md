# [Ozpolat lab](https://bduyguozpolat.org/research)
[![DOI](https://zenodo.org/badge/265590174.svg)](https://zenodo.org/badge/latestdoi/265590174)

Welcome!

## insitu_probe_generator 
Generate HCR-3.0-style Probe Pairs for fluorescent *in situ* mRNA visualization

### Intention of this program:

We were excited to venture into the realm of quick, easy, mutliplexable *in situ* hybridizations presented by the Hybridization Chain Reaction methodology (Choi et al. Development 2018) . We wanted a budget-friendly way of exploring gene expression that allowed for complete control over probe design, while allowing us to also know the exact sequences of our probes to aid publication and reproducibility. As a result, we wrote this program to allow us ease of ordering probes that mesh with the published HCR system of reaction and amplification reagents.

### What you'll find here:

+ We have intentionally kept the program simple to avoid having many dependencies, however you will need to run Python in terminal or Jupyter. **If you need help with this, see the [NEW_TO_PYTHON_JUPYTER.md](https://github.com/rwnull/insitu_probe_generator/blob/master/NEW_TO_PYTHON_JUPYTER.md) guide.**
+ We are providing the code written in Python 3. 
+ While the maker depends upon some Python3 code, the UserInterface.ipynb notebook provided hides the code away so you can focus on making your probes, not on Python.


### What you will need to provide:

#### Some naming convention in mind for your output.
##### By default the output format of the script is *Amplifier_GeneName_ProbePairNumber_5'Delay* where:
  + *Amplifier* - Which hairpin amplifier these probes are compatible with (e.g. B1, B2, B3, B4)
  + *GeneName* - is a user-specified name that contains information useful to the researcher. We like to use an species and gene symbol such as *Pdu_vasa*, but you can use any code you like.
  + *ProbePairNumber* - The total number of pairs of probes this set includes (e.g. 25, 30, or 35)
  + Example **B2_PdumVasa_PP25_DLA_0** for 25 pairs of probes to *Platynereis dumerilii vasa*, starting with no delay, and compatible with the B2 amplifier hairpins.

#### The sense strand of your RNA of interest, in its DNA cognate form (T rather than U).
  + It is up to the user what is included, for example UTRs, introns, or just the coding region.
  + This program will *not* double check that you are using DNA symbols (ATCG). You can type in Homer's Iliad if you like, and you will get back probes pertaining to Nereids, but they won't really help you search for the mRNA of your organism's various Argonauts.

#### A way to create .XLSX format files
  + This could be MS Excel, Google Sheets, etc. 
  + IDT only allows .XLSX format inputs for [ordering OPools](https://www.idtdna.com/pages/products/custom-dna-rna/dna-oligos/custom-dna-oligos/opools-oligo-pools), so saving as .CSV will not work.
  + This program will spit out a copy-pastable dataframe that IDT will recognize, you just need to supply the .XLSX container. You can need to use the ["split text into columns" function](https://support.office.com/en-us/article/split-text-into-different-columns-with-the-convert-text-to-columns-wizard-30b14928-5550-41f5-97ca-7a3e9c363ed7) to separate the columns using "comma" as the delimiter. 


### Running Jupyter Notebook
  + Start Anaconda.
  + Select the Environment you have installed the dependencies on.
  + Launch Jupyter Notebook application from the Anaconda Navigator Home launch page.
  + A browser window will open showing your root directory.
  + Navigate to the unzipped HCRProbeMaker folder, and double click the "UserInterface_v#.#.#.ipynb" file.
  + A new browser page will open.
  + Click within the first cell and run the code by holding "Shift" and pressing "Return".
  + A series of prompts will appear that will guide you through the process to making your probes.


### Description of HCRProbeMaker Inputs and Options
#### Required
  + "name" -> prompt: "What is the gene name?"
    + This is where the user will input the distinguishing name of the probe set. ex. Pdu_vasa -or- RWN001
  + "fullseq" -> prompt: "Enter the sense sequence of your cDNA without spaces or returns."
    + This is where you will input the sense strand sequence of your cDNA
  + "amplifier" -> prompt: "What is the amplifier to be used with this probe set? B1,B2,B3,B4,B5,B7,B9,B10,B11,B13,B14,B15,or B17 "
    + This is where you determine what amplifier hairpin will be used to visualize the probes. 
    + The input requires you have the letter 'b' but is not case sensitive. ex. "b1" -or- "B7" both will work fine, but "7" or "B20" will raise an error.
    + B1-B5 were described by HMT Choi et al. in their [2014 ACS Nano paper](https://pubs.acs.org/doi/full/10.1021/nn405717p)
    + B7,B9,B10,B11,B13,B14,B15, and B17 were described by Y Wang et al. in their [2020 BioRxiv preprint](https://www.biorxiv.org/content/10.1101/274456v3)
  + "pause" -> prompt: "How many bases from 5' end of the Sense RNA before starting to hybridize? ex. 100 "
    + If you want to skip the first 'N' bases of your sequence, or to create a "phase-shift" control, you can use this input to define how many bases you want to skip before making probes.
  + "polyAT/polyCG" -> prompt: "What is the max acceptable length for (polyA or polyT)/(polyC or polyG) homopolymers? "
    + Since the specific portion of the probes are a mere 25bp, some care should be taken to avoid low-complexity sequences that may lead to off-target binding.
    + These two functions set the upper limit of homopolymers you are comfortable with in the probe. 
    + Potential probes with more than the limit will be skipped, so the larger the number entered the **less** strenuous the filter is.
    + Ex. For polyAT = 5, if sequence contains "AAAAA" or "TTTTT" it will be kept, if sequence includes "AAAAAA" or "TTTTTT" it will be skipped.
    + At this point, the algorithm will not descriminate on other low complexity sequences. For instance, "ATATATATATATAT" will be kept. Manually curating the final sequences or adjusting the 5' Delay function can help with this situation. 




#### Optional
**"Do you want to choose program options?"**
  + "choose1" -> prompt: "Do you want to be able to select between potential longest probe sets? (Choosing 'n' defaults to the first longest set of probes.) Y or N "
    + In default settings the algorithm will try to maximize the number of probes that fit in a cDNA, but often there is some wiggle room. This function allows you to see and choose from many potential probe sets. 
    + If "Y" set for this function, a series of 2 column matrices will appear with numbers indicating the position along the original cDNA where the probe pair will span.
    + Above each matrix a number will appear - you enter this number in the dialog box that appears under the last of the matrices to signal your choice. 
    + Leaving the box blank will default to the first (0th) matrix.
  + "BlastProbes" -> prompt: "Would you like BLAST potential probes against a FASTA file?  Y or N "
    + This option instructs the algorithm to make a FASTA file of the potential probe pairs, then call BLASTn with that FASTA file as a query.
    + A hard-coded value has been set in the algorithm to parse probes into 3 categories:
      + 1) Good - Those with high match across the length of the probe pair
      + 2) Unreported - Those for which <50% of the probe pair binds to the cDNA. A decision made assuming that there will be no amplification from 1/2 of the probe.
      + 3) Problematic - Those probe pairs that have >50% coverage of a cDNA and with a middle of the road e-value.
  + If BlastProbes option is chosen a list of further dialog boxes will appear
    + "db" -> prompt: "Where is the FASTA file you would like to BLAST against? " 
      + This is where you define the location of the subject FASTA file. IE your transcriptome/cDNA library.
    + "show" -> prompt: "Do you want to display detailed BLAST outputs? Y or N "
      + "show" will allow you to see the detailed BLASTn output ([in output format 6](https://sites.google.com/site/wiki4metagenomics/tools/blast/blastn-output-format-6)).
    + "dropout" -> prompt: "Do you want to eliminate probes that appear in low quaility BLAST outputs? Y or N "
      + If you want to eliminate probe pairs that fall into the "Problematic" category, set this option to 'Y' and they will not appear in your final output.
  + "report" -> prompt: "Do you want to display chosen parameters in output? Y or N "
    + If you want a record for future experiments of the options/parameters you used during the running of the script, you can turn this function on and it will appear at the end of the run.
  + "maxprobe" -> prompt: "Do you want to limit the number of probes made?  Y or N "
    + If you want to set a limit on the number of probe pairs that are output this function will allow you to do so.
    + This is useful if you are trying to reduce costs, the default setting is to make 33 probe pairs: the max number of probe pairs allowed by IDT's lowest cost tier.
    + In the end if your desired number of probe pairs is greater than what is capable of being made, the algorithm will just output the max number it could make.
    + The algorithm will also space the probe pairs across the full length of the cDNA to maximize coverage of the cDNA.
    + If maxprobe option is chosen one more dialog box will appear
      + "numbr" -> prompt: "Enter a particular number of probes made. The default max is 33.  Enter integer -or- leave empty for default 33 pairs."
      + "numbr" sets the upper limit number of probe pairs made by the program. 
      + Leaving the box empty, entering 0, or entering 33 will all output a maximum of 33 probe pairs.


### Outputs of the Algorithm
The program will return several outputs that will help with ordering, figure construction, and visualization of the probe pairs.
  + First and foremost, IDT OPool submission format
    + This will appear with the heading "Pool name, Sequence" and follow with a list of each member of the probe set preceeded by a single identifier representing the OPool label.
    + Just copy/paste the region from the header to the end of the sequences into an ".xlsx" document and use the "separate data based on comma separator" function.
    + If ordering more than one probe set (i.e. B1_PduVasa, B2_PduActin, B3_RWN001, B3_Loxodonta_Hox4A) all sets can be input to a single document, the uploader will separate them by the "Pool name" into separate tubes.
    + Conversely, if you want to just order 1 tube premultiplexed, just make sure you change the "Pool name" field to be the same across all of the probes in your mix (i.e. "B1_PduVasaB2_PduActinB3_RWN001B3_Loxodonta_Hox4A")
  + Secondly, an output to easily make supplemental figures of your probe mixes is provided, modeled on the supplemental figures of HMT Choi 2018.
    + The header of this output is "Figure Layout of Probe Sequences:"
    + This can be copy/pasted into an .xlsx and separated into columns using the "separate data into columns on space" function.
  + The third and fourth outputs provide location data for each half of a probe pair in relation to the input sequence.
    + The third output shows the probes's base locations numerically.
    + The fourth output spits back a representation of the cDNA where all of the half-pair probe sequences's binding sites are shown along the 5'->3' of the sense strand cDNA. Non-bound regions are converted to 'n'.


## Citation
  If you use this program to create probe pairs, please cite this paper in your publication.

  ```
  Kuehn, E., Clausen, D. S., Null, R. W., Metzger, B. M., Willis, A. D., & Özpolat, B. D. (2022). 
  Segment number threshold determines juvenile onset of germline cluster expansion in Platynereis dumerilii. 
  Journal of Experimental Zoology Part B: Molecular and Developmental Evolution, 338, 225– 240. 
  ```
  Kindly, consider including the work that this was built upon as well.
  ```
  Choi HMT, Schwarzkopf M, Fornace ME, Acharya A, Artavanis G, Stegmaier J, Cunha A, Pierce NA. 
  Third-generation in situ hybridization chain reaction: multiplexed, quantitative, sensitive, versatile, robust. 
  Development. 2018 Jun 26;145(12):dev165753. doi: 10.1242/dev.165753. PMID: 29945988; PMCID: PMC6031405.
  ```
  ```
  Multiplexed in situ protein imaging using DNA-barcoded antibodies with extended hybridization chain reactions.
  Yu Wang, Yitian Zeng, Sinem K. Saka, Wenxin Xie, Isabel Goldaracena, Richie E. Kohman, Peng Yin, George M. Church
  bioRxiv 274456; doi: https://doi.org/10.1101/274456
  ```
  ```
  Tsuneoka Y, Funato H. 
  Modified in situ Hybridization Chain Reaction Using Short Hairpin DNAs. 
  Front Mol Neurosci. 2020 May 12;13:75. doi: 10.3389/fnmol.2020.00075. PMID: 32477063; PMCID: PMC7235299.
  ```
