#!/usr/bin/env python3
###################################################################
#Script Name    :RKP.py
#Description    :Uses KMC 3 to create kmers of genomes and maps
#                them afterwards using map_kmers.sh. Acceptor and 
#                Donor are original species and hybrid is a hybrid
#                of those. Return summary with locus tags and 
#                coverage for every isotope in hybrid dir .
#Args           :-A <genome dir acceptor> -H <genome dir hybrid> -D
#                <genome dir donor> -k  <kmerlength> -at <thresholdAcceptor>
#                -dt <thresholdDonor> -g <acceptor reference genome fasta> 
#                -f < acceptor reference genome gff>
#                -o <output directory> -d -t <threads>
#Dependencies    :conda env -n  RKP kmc bowtie2 bedtools
#                r r-pheatmap r-gplots matplotlib numpy biopython
#                argparse pandas tqdm bedops
#                conda activate RKP
#Author         :Lennard Epping; Felix Hartkopf
#Email          :eppingl@rki.de; hartkopff@rki.de
###################################################################

# Import
import os
import argparse
import pandas as pd
import subprocess
from Bio import SeqIO
import numpy as np
from matplotlib import pyplot as plt
import glob
import gzip
import shutil
import logging
from tqdm import tqdm
from time import perf_counter 
import datetime

def extract_kmer_coverage(output,baseHybrid):
    # Merging coverage of all isotopes
    df = pd.DataFrame(columns=["ID"])
    for file in tqdm(os.listdir(output+"/"+baseHybrid+"/")):
        if file.endswith("locus.bed"):
            df1 = pd.read_csv(os.path.join(output,baseHybrid,file),sep="\t",header=None)
            name = file.split(".")[0]
            df1 = df1[[3,13]]
            df1.columns=["ID",name]
            df=pd.merge(df, df1, on="ID",how="outer")
            df.fillna('0.0', inplace=True)
           
    df.to_csv(os.path.join(output, baseHybrid,"mapping_result.csv"))

# Translate final fasta in amino acid sequences
def get_gene_sequence(output, baseHybrid):
    for file in tqdm(os.listdir(output+"/"+baseHybrid+"/")):
        if file.endswith("_iso_seq.fasta"):
            proteins = []
            input_file = open(os.path.join(output,baseHybrid, file), 'r')
            output_file = os.path.join(output,baseHybrid, file.replace("_iso_seq.fasta","_iso_seq_protein.fasta"))
            for cur_record in SeqIO.parse(input_file,"fasta" ) :
                 description = cur_record.description
                 protein = cur_record.translate(table=11)
                 protein.id = ""
                 protein.description = description
                 proteins.append(protein)
            SeqIO.write(proteins, output_file, "fasta")

    # Extract Genome coverage per Position
    subprocess.check_output(["for f in "+output+"/"+baseHybrid+"/"+"*_sorted.bam; do bedtools genomecov -ibam ${f} -d > ${f%.bam}_genomecov.tsv; done"], shell=True)

def plot_recombinations(output,baseHybrid,kmerlength):
# Plot Recombination Events
    for t in tqdm([50,100,200,300,400,500 ]):
        # Get files in hybrid directory
        files = os.listdir(output+"/"+baseHybrid+"/")

        # Initiate final dataframe
        finaldf = pd.DataFrame(columns=["ID"])

        for file in files:
            if file.endswith("_genomecov.tsv"):

                # Temporary genome coverage
                genomeCov = pd.read_csv(os.path.join(output,baseHybrid,file),sep="\t",header=None)
                name = file.split(".")[0]

                # All counts higher than 1 are 1
                genomeCov.loc[genomeCov[2] >= 1] = 1
                genomeCounts = genomeCov[2]
                finalCounts = []

                # count0, count1, count_total, count_start
                count_vector = [0,0,0,0]

                # Iterate through positions of genome
                for pos in genomeCounts:
                    # increase total count of bases in genome
                    count_vector[2]+=1
                    if pos == 1: # At least one kmer matched here
                        count_vector[1] += 1+count_vector[0]# count0 increase if pos not 1 too
                        count_vector[0] = 0
                        if count_vector[1] == 1:
                            count_vector[3] = count_vector[2]
                    elif count_vector[1] > 0:
                        count_vector[0] += 1
                        if count_vector[0] == t:#100:
                            if count_vector[1] > 100:
                                finalCounts.append([count_vector[3],count_vector[1]])
                            count_vector[0] = 0
                            count_vector[1] = 0
                finalCountsdf = pd.DataFrame(finalCounts)
                finalCountsdf.columns=["ID",name]
                finaldf = pd.merge(finaldf, finalCountsdf, on="ID",how="outer")

        # Write recombination events of all isolates to csv file
        finaldf.to_csv(output+"/"+baseHybrid+"/"+"Recombination_result_"+kmerlength+"_W"+str(t)+".csv")

        # Prepare data for plot
        cols = finaldf.columns[1:]
        finaldf[cols] = finaldf[cols].replace(0,np.nan)
        finaldf = finaldf.sort_values(by=['ID'])#.set_index("ID")
        finaldf[cols] = finaldf[cols].replace(np.nan,0)

        # Plot recombination events

        # Initiate figure
        fig = plt.figure(figsize=(20,10))
        axes = fig.add_axes([0.1,0.1,0.8,0.8])

        for isolate in cols:
            if isolate != "ID":
                cumulative = finaldf[isolate].cumsum()
                axes.plot(finaldf["ID"],cumulative,label=isolate)

        axes.set_title('Cumulative Sum of Recombination Events',fontsize=20)
        axes.set_xlabel("Genome Position",fontsize=16)
        axes.set_ylabel("Total Size of Recombination Events in bp ",fontsize=16)
        fig.legend(loc="lower right")
        fig.savefig(output+"/"+baseHybrid+"/"+"recombination_cov"+kmerlength+"_W"+str(t)+".pdf")


def remove_files(output,baseAcceptor,baseHybrid,baseDonor,acceptorRef):

    logging.info("Removing temporary files")
    # Specify files to be deleted
    fileList = []
    # KMC
    fileList += glob.glob(os.path.join(output,baseAcceptor,'*.kmc_suf'))
    fileList += glob.glob(os.path.join(output,baseAcceptor,'*.kmc_pre'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.kmc_suf'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.kmc_pre'))
    fileList += glob.glob(os.path.join(output,baseDonor,'*.kmc_suf'))
    fileList += glob.glob(os.path.join(output,baseDonor,'*.kmc_pre'))

    # Mapping
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.bai'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.bam'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.bed'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.sam'))

    # Blast
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.nog'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.nin'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.nsi'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.nsq'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.nhr'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.nhi'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.nhd'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.nsd'))

    # Misc
    fileList += glob.glob(os.path.join(output,baseAcceptor,'*.txt'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.txt'))
    fileList += glob.glob(os.path.join(output,baseDonor,'*.txt'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*final.fasta'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.tsv'))

    # Bedtools
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.genes.bed'))
    fileList += glob.glob(os.path.join(output,baseHybrid,'*.genes.bed'))
    fileList += glob.glob(os.path.join(output+baseHybrid,'*.genes.bed'))

    # Reference
    fileList += glob.glob(acceptorRef+'*.fai')
    fileList += glob.glob(acceptorRef+'*.bt2')

    # Iterate over the list of filepaths & remove each file.
    for filePath in fileList:
        try:
            os.remove(filePath)
        except OSError:
            print("Error while deleting file")


def gunzip_shutil(source_filepath, dest_filepath, block_size=65536):
    with gzip.open(source_filepath, 'rb') as s_file, \
            open(dest_filepath, 'wb') as d_file:
        shutil.copyfileobj(s_file, d_file, block_size)

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def main(acceptor, hybrid, donor, kmerlength, thresholdAcceptor, thresholdDonor, acceptorRef, output, acceptorRefGff, threads, debug):
    
    time_start = perf_counter()

    # Create output directory
    try:
        os.mkdir(output, mode=0o777)
        print("Directory " , output ,  " created ")
    except FileExistsError:
        print("Directory " , output ,  " already exists")

    # Logging
    logging.basicConfig(filename=os.path.join(output,'RKP.log'), filemode='a', format='%(levelname)s - %(message)s', level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("Parameters: ")
    for key,value in {"acceptor":acceptor, "hybrid":hybrid, "donor":donor, "kmerlength":kmerlength, "thresholdAcceptor":thresholdAcceptor, "thresholdDonor":thresholdDonor, "acceptorRef":acceptorRef, "output":output, "acceptorRefGff":acceptorRefGff, "threads":threads, "debug":debug}.items():
        param = ("\t"+(key+":").ljust(15)+"\t"+str(value))
        logging.info(str(param))

    #prepare arguments
    baseAcceptor = os.path.basename(os.path.normpath(acceptor))
    baseHybrid = os.path.basename(os.path.normpath(hybrid))
    baseDonor = os.path.basename(os.path.normpath(donor))
    codepath = os.path.dirname(os.path.abspath(__file__))
    logging.info("Path of source code: "+codepath)
    if acceptorRef.endswith(".gz"):
        gunzip_shutil(acceptorRef,os.path.splitext(acceptorRef)[0])
        acceptorRef = os.path.splitext(acceptorRef)[0]
    if acceptorRefGff.endswith(".gz"):
        gunzip_shutil(acceptorRefGff,os.path.splitext(acceptorRefGff)[0])
        acceptorRefGff = os.path.splitext(acceptorRefGff)[0]

    #call functions
    # Start kmer extracting (KMC) and mapping to genome (bowtie2)
    for path in execute([codepath+"/create_kmers.sh", acceptor,\
        hybrid, donor, kmerlength, thresholdAcceptor,\
        thresholdDonor, acceptorRef, acceptorRefGff, output, threads]):
        print(path, end="")
    
    logging.info("Start extracting k-mer coverage...")
    extract_kmer_coverage(output,baseHybrid)
    logging.info("Plotting heatmap...")
    res = subprocess.check_output([codepath+"/heatmap.R",os.path.join(output, baseHybrid,"mapping_result.csv"),output])
    logging.info("Writting protein fasta...")
    get_gene_sequence(output,baseHybrid)
    logging.info("Plotting recombination events...")
    plot_recombinations(output,baseHybrid,kmerlength)

    if not debug:
        remove_files(output,baseAcceptor,baseHybrid,baseDonor,acceptorRef)

    logging.info("Done! Check log file ("+os.path.join(output,'RKP.log')+") for more information.")
    time_stop = perf_counter()
    logging.info("Elapsed time during the whole RKP workflow: "+ str(datetime.timedelta(seconds=time_stop-time_start)))

    return 0

if __name__ == "__main__":
    # Read command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-A', '--acceptor', required=True)
    parser.add_argument('-H', '--hybrid', required=True)
    parser.add_argument('-D', '--donor', required=True)
    parser.add_argument('-k', '--kmerlength', required=True)
    parser.add_argument('-at', '--thresholdAcceptor', required=True)
    parser.add_argument('-dt', '--thresholdDonor', required=True)
    parser.add_argument('-g', '--acceptorRef', required=True)
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-f', '--acceptorRefGff', required=True)
    parser.add_argument('-t', '--threads', required=False, default="8")
    parser.add_argument('-d','--debug', required=False, action="store_true")
    parser.add_argument('--version', action='version',version='0.1.0')
    args = parser.parse_args()

    main(args.acceptor, args.hybrid, args.donor, args.kmerlength, args.thresholdAcceptor, args.thresholdDonor, args.acceptorRef, args.output, args.acceptorRefGff, args.threads, args.debug)