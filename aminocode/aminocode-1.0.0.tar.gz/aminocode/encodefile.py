#!/usr/bin/python
# -*- coding: utf-8 -*-
from re import sub,findall,search
import unidecode
from Bio import SeqIO, Seq
import sys
import codecs
from Bio.SeqRecord import SeqRecord

from .aminocode import *

def list2bioSeqRecord(header,seq):
    records = []
    for i in range(0,len(seq)):
        record = SeqRecord(Seq.Seq(seq[i]), description=header[i], id=str(i))
        records.append(record)
    records = (i for i in records)
    return records
list2fasta = list2bioSeqRecord
def writeFasta(records,out):
    fasta = list(records)
    outputFile = codecs.open(out,'w','utf-8')
    for i in fasta:
        if len(i.seq) > 0:
            outputFile.write('>'+i.description+'\n')
            seq = str(i.seq)
            seq = findall('\w{0,'+str(100)+'}',seq)
            seq = '\n'.join(seq)
            outputFile.write(seq)
    outputFile.close()

    return records

def encodefile(input_file_name,output_file_name=None,detailing='',header_format='number+originaltext',verbose=False):
    out = output_file_name
    det = detailing
    selectedEncoder = lambda x: et(x,det=det)
    # head file if necessary
    if isinstance(input_file_name, str): # if string consider filename and read
        read_file = list(SeqIO.parse(codecs.open(input_file_name,'r','utf-8'), "fasta"))
        if len(read_file) > 0:
            records = []
            for i in read_file:
                records.append (i.description)
        else:
            read_file = codecs.open(input_file_name,'r','utf-8')
            records = [line.strip() for line in read_file]
            read_file.close()
    else:
        read_file = input_file_name
        try:
            read_file[0].description #return exception if not fasta
            records = []
            for i in read_file:
                records.append (i.description)
        except:
            records = [line.strip() for line in read_file]
            
    # create header list
    count = 0
    headers = []
    for i in records:
        count += 1
        if header_format == 'number':
            headers.append(count)
        elif header_format == 'originaltext':
            i = sub('\n$','',i)
            headers.append(i)
        elif header_format == 'number+originaltext':
            i = sub('\n$','',i)
            headers.append(str(count)+' '+i)
        
    seqs = []    
    for c,i in enumerate(records):
        i = sub('\n$','',i)
        try:
            i = i.decode('utf-8')
        except:
            pass
        #print(i)
        seq = selectedEncoder(i)
        seqs.append(seq)
        if verbose and (c+1) % 10000 == 0:
            print (str(c+1)+'/'+str(count))
    if verbose:
        print (str(count)+'/'+str(count))
    records=list2bioSeqRecord(headers,seqs)
    
    if not (out is None):
        records = writeFasta(list(records),out)
    return records
ef = encodefile

def decodefile(input_file_name,output_file_name=None,detailing='',verbose=False):
    out = output_file_name
    det = detailing
    selectedEncoder = lambda x: dt(x,det=det)
    print('Decoding text...')
    
    if isinstance(input_file_name, str): # if string consider filename and read
        read_file = list(SeqIO.parse(codecs.open(input_file_name,'r','utf-8'), "fasta"))
    else:
        records = list(input_file_name)
    num_lines = len(records)
    c=0
    text = []
    for i in records:
        c+=1
        if verbose and (c+1) % 10000 == 0:
            print(str(c+1)+'/'+str(num_lines))
        text.append((selectedEncoder(str(i.seq))))
    if verbose:
        print(str(num_lines)+'/'+str(num_lines))
    if not (out is None):
        outputFile = codecs.open(out,'w','utf-8')
        for i in text:
            outputFile.write(i+'\n')
        outputFile.close()
    
    return text
            
df = decodefile