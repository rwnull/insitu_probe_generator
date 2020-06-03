#!/usr/bin/env python
# coding: utf-8

__author__ = "Ryan W Null, https://github.com/rwnull/insitu_probe_generator"
__copyright__ = "Copyright 2019-2020, The Ozpolat Lab (http://bduyguozpolat.org/)"
__credits__ = ["B. Duygu Ozpolat"]
__license__ = "GPL 3.0"
__version__ = "2020_0.2.0"



#_REFERENCES_

##_See Choi et al. 2018 Development for HCR3.0 methodology details
###_https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6031405/





# Step 1: Create a name for your sequence

name=str(input("What is the gene name? (ex. eGFP) "))



# Step 2: Input the reverse complement of your transcript of interest. 

## 	To create reverse complements use this tool - https://www.bioinformatics.org/sms/rev_comp.html
## 	Provided Example sequence:
### 		>eGFP Reverse complement
### 		ttacttgtacagctcgtccatgccgagagtgatcccggcggcggtcacgaactccagcaggaccatgtgatcgcgcttctcgttggggtctttgctcagggcggactgggtgctcaggtagtggttgtcgggcagcagcacggggccgtcgccgatgggggtgttctgctggtagtggtcggcgagctgcacgctgccgtcctcgatgttgtggcggatcttgaagttcaccttgatgccgttcttctgcttgtcggccatgatatagacgttgtggctgttgtagttgtactccagcttgtgccccaggatgttgccgtcctccttgaagtcgatgcccttcagctcgatgcggttcaccagggtgtcgccctcgaacttcacctcggcgcgggtcttgtagttgccgtcgtccttgaagaagatggtgcgctcctggacgtagccttcgggcatggcggacttgaagaagtcgtgctgcttcatgtggtcggggtagcggctgaagcactgcacgccgtaggtcagggtggtcacgagggtgggccagggcacgggcagcttgccggtggtgcagatgaacttcagggtcagcttgccgtaggtggcatcgccctcgccctcgccggacacgctgaacttgtggccgtttacgtcgccgtccagctcgaccaggatgggcaccaccccggtgaacagctcctcgcccttgctcaccat
###		>Aequorea victoria enhanced GFP sense cDNA | GenBank U55761.1 | ncbi.nlm.nih.gov/nuccore/1377908
###		ATGgtgagcaagggcgaggagctgttcaccggggtggtgcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgaagttcatctgcaccaccggcaagctgcccgtgccctggcccaccctcgtgaccaccctgacctacggcgtgcagtgcttcagccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccgaaggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgccgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgacttcaaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgtctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaacatcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcgacggccccgtgctgctgcccgacaaccactacctgagcacccagtccgccctgagcaaagaccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatcactctcggcatggacgagctgtacaagtaa


fullseq=str(input("Enter the REVERSE COMPLEMENT of your cDNA without spaces or returns. "))
cdna=len(fullseq)											#this will measure the length (number of bases of your input)




# Step 3: What amplifier hairpin will you use to detect probes? We've built in the probes sold by Molecular Instruments "B1-B4".


amplifier=str(input("What is the amplifier to be used with this probe set? B1,B2,B3, or B4 ").upper())
def amp(ampl): 
    if ampl == "B1":
        upspc= "aa"
        dnspc= "ta"
        up = "GAGGAGGGCAGCAAACGG"
        dn = "GAAGAGTCTTCCTTTACG"
    elif ampl == "B2":
        upspc= "aa"
        dnspc= "aa"
        up = "CCTCGTAAATCCTCATCA"
        dn = "ATCATCCAGTAAACCGCC"
    elif ampl == "B3":
        upspc= "tt"
        dnspc= "tt"
        up = "GTCCCTGCCTCTATATCT"
        dn = "CCACTCAACTTTAACCCG"
    elif ampl == "B4":
        upspc= "aa"
        dnspc= "at"
        up = "CCTCAACCTACCTCCAAC"
        dn = "TCTCACCATATTCGCTTC"
    else:
        print("Please try again")
    return([upspc,dnspc,up,dn])

test=amp(amplifier)
uspc=test[0]
dspc=test[1]
upinit=test[2]
dninit=test[3]




# Step 4: Tuning/printing output of probes. 

## How far from start of cDNA before starting to make probes?
pause=int(input("How many bases from 5' end of the Sense RNA before starting to hybridize? ex. 100 "))

## How many probe pairs desired?
count=(int(input("How many pairs of probes do you want? This will be the maximum number if mRNA will accomodate. ")))



# Output begins


print("")
print("")
print("HCR3.0 Probe Maker Output")
print("")
print("")




## A figure layout output like seen in the 2018 HCR Paper supplement

print("Figure Layout:")
print("")
print(str(amplifier+"_"+str(name)+"_"+str(count)))							# Name based on inputs
print("Pair#,1st Half of Initiator I1,Spacer,Probe,,Probe,Spacer,2nd Half of Initiator I1")	# HEADER of Output


position=cdna-pause     										# This controls how far from the 5'end of the mRNA probes begin 
pair=1
pairlib={}
idtlibu={}
idtlibd={}
while position>52: 											#52 is the cutoff for fitting an entire pair at the end of the gene. the program will cycle back over the RNA if not limited like this
    downstream=str(fullseq[position-25:position])
    upstream=str(fullseq[position-52:position-27])
    pairlib[pair]=str(str(pair)+","+str(cdna-position+25)+","+str(fullseq[position-25:position])+","+str(cdna-position)+",,"+str(cdna-position+52)+","+str(fullseq[position-52:position-27])+","+str(cdna-position+27))
    idtlibu[pair]=str(amplifier+"_"+str(name)+"_"+str(count)+","+upinit+uspc+upstream)   		# This is a library used for IDT output
    idtlibd[pair]=str(amplifier+"_"+str(name)+"_"+str(count)+","+downstream+dspc+dninit)
    position-=54      											# 54 is the number of bases covered by one probe set (25bp probe 1, 2bp spacer, 25bp probe 2, 2bp spacer). 
    print(str(pair)+","+upinit+","+uspc+","+upstream+",,"+downstream+","+dspc+","+dninit)
    if pair<count:
        pair+=1
    else:
        break



## This outputs the sequences of the probes and where they hybridize on the cDNA

print("")
print("")
print("Below are the hybridizing sequences and where they align to the cDNA:")
print("")
print("Pair#,cDNAcoord,Probe,cDNAcoord,,cDNAcoord,Probe,cDNAcoord")				# Header for Output
i=1
while i <= pair:
    print(pairlib[i])
    i+=1

print("")
print("")
print("")


## Output for IDT oPool Submission

print("Below is in IDT oPool submission_format.")
print("Copy and Paste this into an XLSX file for submission to IDT.")
print("")
print("Pool name,sequence")										#Header for output
i=1
while i <= pair:
    print(str(idtlibu[i]))
    print(str(idtlibd[i]))
    i+=1

    


## Output of the Reverse Complement used for documentation 

print("")
print("")
print("")
print("Anti-sense sequence used:")
print("")
print(">"+name)
print(fullseq)






