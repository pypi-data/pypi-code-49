#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from builtins import range
import numpy as np
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import sys, math, re, os
import unitCellTools

# 3D plotting 
#from mpl_toolkits import mplot3d

#------------- REGULAR EXPRESSION
regexprCRYST1=re.compile(r"^CRYST1")
regexprATOM2=re.compile(r"(ATOM  |HETATM)([\d\.\s]{5})(\s)(.{4})(.{1})(.{3})(\s)(.{1})(.{4})(.{1})(.{3})([.\d\s\-]{8})([.\d\s\-]{8})([.\d\s\-]{8})(.{6})(.{6})(\s{10})(.{2}).*") 
reHKL= re.compile(r"([\-\d\s]{4})([\-\d\s]{4})([\-\d\s]{4}) ([\-\.\d\s]{8})([\-\.\d\s]{8})([\-\.\d\s]{8})([\-\.\d\s]{8})")
reAmplitude=re.compile(r"([\-\d])+\.(\d+)")

#------------- CONSTANTS
NELECTRONS={ 'H':1, 'HE':2, 'LI':3, 'BE':4, 'B':5, 'C':6, 'N':7, 'O':8, 'F':9, 'NE':10, 'NA':11, 'MG':12, 'AL':13, 'SI':14, 'P':15, 'S':16, 'CL':17, 'AR':18, 'K':19, 'CA':20, 'SC':21, 'TI':22, 'V':23, 'CR':24, 'MN':25, 'FE':26, 'CO':27, 'NI':28, 'CU':29, 'ZN':30, 'GA':31, 'GE':32, 'AS':33, 'SE':34, 'BR':35, 'KR':36, 'RB':37, 'SR':38, 'Y':39, 'ZR':40, 'NB':41, 'MO':42, 'TC':43, 'RU':44, 'RH':45, 'PD':46, 'AG':47, 'CD':48, 'IN':49, 'SN':50, 'SB':51, 'TE':52, 'I':53, 'XE':54, 'CS':55, 'BA':56, 'LA':57, 'CE':58, 'PR':59, 'ND':60, 'PM':61, 'SM':62, 'EU':63, 'GD':64, 'TB':65, 'DY':66, 'HO':67, 'ER':68, 'TM':69, 'YB':70, 'LU':71, 'HF':72, 'TA':73, 'W':74, 'RE':75, 'OS':76, 'IR':77, 'PT':78, 'AU':79, 'HG':80, 'TL':81, 'PB':82, 'BI':83, 'PO':84, 'AT':85, 'RN':86, 'FR':87, 'RA':88, 'AC':89, 'TH':90, 'PA':91, 'U':92, 'NP':93, 'PU':94, 'AM':95, 'CM':96, 'BK':97, 'CF':98, 'ES':99, 'FM':100, 'MD':101, 'NO':102, 'LR':103, 'RF':104, 'DB':105, 'SG':106, 'BH':107, 'HS':108, 'MT':109, 'UUN':110, 'UUU':111, 'UUB':112, 'UUT':113, 'UUQ':114, 'UUP':115, 'UUH':116, 'UUS':117, 'UUO':118,}
RESO_CUTOFF=2.0
GRID_DIVIDE= 4   # how many times we divide the resolution to get the grid spacing
NTERMS=4
CUBEDIM=2

#----------------------------------------------
PDBLINE_C= "ATOM      1  C   ALA A   1      15.570  14.283  40.555  1.00  7.75           C"
PDBLINE_O= "ATOM      1  O   ALA A   1      15.570  14.283  40.555  1.00  7.75           O"

#------------- Form factor tables
chemGaussian={
  'H':    {
    'radius':0.31,
    'nelectrons':1,
    'a1':0.489918,
    'b1':20.6593,
    'a2':0.262003,
    'b2':7.74039,
    'a3':0.196767,
    'b3':49.5519,
    'a4':0.049879,
    'b4':2.20159,
    'c':0.001305,
    },
  'ZN':    {
    'radius':1.22,
    'nelectrons':30,
    'a1':14.0743,
    'b1':3.2655,
    'a2':7.0318,
    'b2':0.2333,
    'a3':5.1652,
    'b3':10.3163,
    'a4':2.41,
    'b4':58.7097,
    'c':1.3041,
    },
  'HE':    {
    'radius':0.28,
    'nelectrons':2,
    'a1':0.8734,
    'b1':9.1037,
    'a2':0.6309,
    'b2':3.3568,
    'a3':0.3112,
    'b3':22.9276,
    'a4':0.178,
    'b4':0.9821,
    'c':0.0064,
    },
  'CU':    {
    'radius':1.32,
    'nelectrons':29,
    'a1':13.338,
    'b1':3.5828,
    'a2':7.1676,
    'b2':0.247,
    'a3':5.6158,
    'b3':11.3966,
    'a4':1.6735,
    'b4':64.8126,
    'c':1.191,
    },
  'F':    {
    'radius':0.57,
    'nelectrons':9,
    'a1':3.5392,
    'b1':10.2825,
    'a2':2.6412,
    'b2':4.2944,
    'a3':1.517,
    'b3':0.2615,
    'a4':1.0243,
    'b4':26.1476,
    'c':0.2776,
    },
  'O':    {
    'radius':0.66,
    'nelectrons':8,
    'a1':3.0485,
    'b1':13.2771,
    'a2':2.2868,
    'b2':5.7011,
    'a3':1.5463,
    'b3':0.3239,
    'a4':0.867,
    'b4':32.9089,
    'c':0.2508,
    },
  'NE':    {
    'radius':0.58,
    'nelectrons':10,
    'a1':3.9553,
    'b1':8.4042,
    'a2':3.1125,
    'b2':3.4262,
    'a3':1.4546,
    'b3':0.2306,
    'a4':1.1251,
    'b4':21.7184,
    'c':0.3515,
    },
  'N':    {
    'radius':0.71,
    'nelectrons':7,
    'a1':12.2126,
    'b1':0.0057,
    'a2':3.1322,
    'b2':9.8933,
    'a3':2.0125,
    'b3':28.9975,
    'a4':1.1663,
    'b4':0.5826,
    'c':-11.529,
    },
  'HG':    {
    'radius':1.32,
    'nelectrons':80,
    'a1':20.6809,
    'b1':0.545,
    'a2':19.0417,
    'b2':8.4484,
    'a3':21.6575,
    'b3':1.5729,
    'a4':5.9676,
    'b4':38.3246,
    'c':12.6089,
    },
  'CD':    {
    'radius':1.44,
    'nelectrons':48,
    'a1':19.2214,
    'b1':0.5946,
    'a2':17.6444,
    'b2':6.9089,
    'a3':4.461,
    'b3':24.7008,
    'a4':1.6029,
    'b4':87.4825,
    'c':5.0694,
    },
  'NI':    {
    'radius':1.24,
    'nelectrons':28,
    'a1':12.8376,
    'b1':3.8785,
    'a2':7.292,
    'b2':0.2565,
    'a3':4.4438,
    'b3':12.1763,
    'a4':2.38,
    'b4':66.3421,
    'c':1.0341,
    },
  'PD':    {
    'radius':1.39,
    'nelectrons':46,
    'a1':19.3319,
    'b1':0.698655,
    'a2':15.5017,
    'b2':7.98929,
    'a3':5.29537,
    'b3':25.2052,
    'a4':0.605844,
    'b4':76.8986,
    'c':5.26593,
    },
  'AU':    {
    'radius':1.36,
    'nelectrons':79,
    'a1':16.8819,
    'b1':0.4611,
    'a2':18.5913,
    'b2':8.6216,
    'a3':25.5582,
    'b3':1.4826,
    'a4':5.86,
    'b4':36.3956,
    'c':12.0658,
    },
  'C':    {
    'radius':0.74,
    'nelectrons':6,
    'a1':2.31,
    'b1':20.8439,
    'a2':1.02,
    'b2':10.2075,
    'a3':1.5886,
    'b3':0.5687,
    'a4':0.865,
    'b4':51.6512,
    'c':0.2156,
    },
  'AG':    {
    'radius':1.45,
    'nelectrons':47,
    'a1':19.2808,
    'b1':0.6446,
    'a2':16.6885,
    'b2':7.4726,
    'a3':4.8045,
    'b3':24.6605,
    'a4':1.0463,
    'b4':99.8156,
    'c':5.179,
    },
  'MG':    {
    'radius':1.39,
    'nelectrons':25,
    'a1':5.4204,
    'b1':2.8275,
    'a2':2.1735,
    'b2':79.2611,
    'a3':1.2269,
    'b3':0.3808,
    'a4':2.3073,
    'b4':7.1937,
    'c':0.8584,
    },
  'CL':    {
    'radius':1.02,
    'nelectrons':17,
    'a1':11.4604,
    'b1':0.0104,
    'a2':7.1964,
    'b2':1.1662,
    'a3':6.2556,
    'b3':18.5194,
    'a4':1.6455,
    'b4':47.7784,
    'c':-9.5574,
    },
  'PT':    {
    'radius':1.36,
    'nelectrons':78,
    'a1':27.0059,
    'b1':1.51293,
    'a2':17.7639,
    'b2':8.81174,
    'a3':15.7131,
    'b3':0.424593,
    'a4':5.7837,
    'b4':38.6103,
    'c':11.6883,
    },
  'P':    {
    'radius':1.07,
    'nelectrons':15,
    'a1':6.4345,
    'b1':1.9067,
    'a2':4.1791,
    'b2':27.157,
    'a3':1.78,
    'b3':0.526,
    'a4':1.4908,
    'b4':68.1645,
    'c':1.1149,
    },
  'S':    {
    'radius':1.05,
    'nelectrons':16,
    'a1':6.9053,
    'b1':1.4679,
    'a2':5.2034,
    'b2':22.2151,
    'a3':1.4379,
    'b3':0.2536,
    'a4':1.5863,
    'b4':56.172,
    'c':0.8669,
    },
  'LI':    {
    'radius':1.28,
    'nelectrons':3,
    'a1':1.1282,
    'b1':3.9546,
    'a2':0.7508,
    'b2':1.0524,
    'a3':0.6175,
    'b3':85.3905,
    'a4':0.4653,
    'b4':168.261,
    'c':0.0377,
    },
  'AS':    {
    'radius':1.19,
    'nelectrons':33,
    'a1':16.6723,
    'b1':2.6345,
    'a2':6.0701,
    'b2':0.2647,
    'a3':3.4313,
    'b3':12.9479,
    'a4':4.2779,
    'b4':47.7972,
    'c':2.531,
    },
  'BR':    {
    'radius':1.20,
    'nelectrons':35,
    'a1':17.1789,
    'b1':2.1723,
    'a2':5.2358,
    'b2':16.5796,
    'a3':5.6377,
    'b3':0.2609,
    'a4':3.9851,
    'b4':41.4328,
    'c':2.9557,
    },
  'U':    {
    'radius':1.96,
    'nelectrons':92,
    'a1':36.0228,
    'b1':0.5293,
    'a2':23.4128,
    'b2':3.3253,
    'a3':14.9491,
    'b3':16.0927,
    'a4':4.188,
    'b4':100.613,
    'c':13.3966,
    },
  'GA':    {
    'radius':1.22,
    'nelectrons':31,
    'a1':15.2354,
    'b1':3.0669,
    'a2':6.7006,
    'b2':0.2412,
    'a3':4.3591,
    'b3':10.7805,
    'a4':2.9623,
    'b4':61.4135,
    'c':1.7189,
    },
  'AR':    {
    'radius':1.06,
    'nelectrons':18,
    'a1':7.4845,
    'b1':0.9072,
    'a2':6.7723,
    'b2':14.8407,
    'a3':0.6539,
    'b3':43.8983,
    'a4':1.6442,
    'b4':33.3929,
    'c':1.4445,
    },
  'SE':    {
    'radius':1.20,
    'nelectrons':34,
    'a1':17.0006,
    'b1':2.4098,
    'a2':5.8196,
    'b2':0.2726,
    'a3':3.9731,
    'b3':15.2372,
    'a4':4.3543,
    'b4':43.8163,
    'c':2.8409,
    },
  'IN':    {
    'radius':1.42,
    'nelectrons':49,
    'a1':19.1624,
    'b1':0.5476,
    'a2':18.5596,
    'b2':6.3776,
    'a3':4.2948,
    'b3':25.8499,
    'a4':2.0396,
    'b4':92.8029,
    'c':4.9391,
    },
  'TL':    {
    'radius':1.45,
    'nelectrons':81,
    'a1':27.5446,
    'b1':0.65515,
    'a2':19.1584,
    'b2':8.70751,
    'a3':15.538,
    'b3':1.96347,
    'a4':5.52593,
    'b4':45.8149,
    'c':13.1746,
    },
  'I':    {
    'radius':1.39,
    'nelectrons':53,
    'a1':20.1472,
    'b1':4.347,
    'a2':18.9949,
    'b2':0.3814,
    'a3':7.5138,
    'b3':27.766,
    'a4':2.2735,
    'b4':66.8776,
    'c':4.0712,
    },
  'KR':    {
    'radius':1.16,
    'nelectrons':36,
    'a1':17.3555,
    'b1':1.9384,
    'a2':6.7286,
    'b2':16.5623,
    'a3':5.5493,
    'b3':0.2261,
    'a4':3.5375,
    'b4':39.3972,
    'c':2.825,
    },
  'PB':    {
    'radius':1.46,
    'nelectrons':82,
    'a1':31.0617,
    'b1':0.6902,
    'a2':13.0637,
    'b2':2.3576,
    'a3':18.442,
    'b3':8.618,
    'a4':5.9696,
    'b4':47.2579,
    'c':13.4118,
    },
  'TE':    {
    'radius':1.38,
    'nelectrons':52,
    'a1':19.9644,
    'b1':4.81742,
    'a2':19.0138,
    'b2':0.420885,
    'a3':6.14487,
    'b3':28.5284,
    'a4':2.5239,
    'b4':70.8403,
    'c':4.352,
    },
  'SI':    {
    'radius':1.11,
    'nelectrons':14,
    'a1':6.2915,
    'b1':2.4386,
    'a2':3.0353,
    'b2':32.3337,
    'a3':1.9891,
    'b3':0.6785,
    'a4':1.541,
    'b4':81.6937,
    'c':1.1407,
    },
  'XE':    {
    'radius':1.40,
    'nelectrons':54,
    'a1':20.2933,
    'b1':3.9282,
    'a2':19.0298,
    'b2':0.344,
    'a3':8.9767,
    'b3':26.4659,
    'a4':1.99,
    'b4':64.2658,
    'c':3.7118,
    },
  'SN':    {
    'radius':1.39,
    'nelectrons':50,
    'a1':19.1889,
    'b1':5.8303,
    'a2':19.1005,
    'b2':0.5031,
    'a3':4.4585,
    'b3':26.8909,
    'a4':2.4663,
    'b4':83.9571,
    'c':4.7821,
    },
  'NA':    {
    'radius':1.66,
    'nelectrons':11,
    'a1':4.7626,
    'b1':3.285,
    'a2':3.1736,
    'b2':8.8422,
    'a3':1.2674,
    'b3':0.3136,
    'a4':1.1128,
    'b4':129.424,
    'c':0.676,
    },
  'K':    {
    'radius':2.03,
    'nelectrons':19,
    'a1':8.2186,
    'b1':12.7949,
    'a2':7.4398,
    'b2':0.7748,
    'a3':1.0519,
    'b3':213.187,
    'a4':0.8659,
    'b4':41.6841,
    'c':1.4228,
    },
  'CA':    {
    'radius':1.76,
    'nelectrons':20,
    'a1':8.6266,
    'b1':10.4421,
    'a2':7.3873,
    'b2':0.6599,
    'a3':1.5899,
    'b3':85.7484,
    'a4':1.0211,
    'b4':178.437,
    'c':1.3751,
    },

}

#------------- FUNCTIONS
def gaussianTerm(a, b, bfact, r):
    # calculate a Gaussian eletron density term (from Agarwal, 1978)
    return a*np.power((4*np.pi / (b + bfact)), 1.5) * np.exp(-4*np.power(np.pi*r,2) / (b + bfact))


def gaussianApprox(nterms, elem, Bfact, r):

    result =0
    n=0
    i=0

    nterms = 4 if nterms>4 else nterms
    indices=('a1', 'b1', 'a2', 'b2', 'a3', 'b3', 'a4', 'b4')
    terms=[chemGaussian[elem][k] for k in indices]


    # Calculate the first term whatever is happening
    for n in range(1,nterms+1):
        i=n*2-2
        result += gaussianTerm(terms[i], terms[i+1], Bfact, r)
        #print("SHERLOCK term {} = {}".format(n, result))
    return result


def indexFromFrac(fracCoordarray, nx, ny, nz):
    """ Returns in which voxel (1D), a fractional coordinate belongs, for each of an array of fractional coordinates"""

    dim=(nx, ny, nz)
    outtab=[]
    for i,fracCoord in enumerate(fracCoordarray):
        tmp= fracCoord* (dim[i]-1)
        if tmp%1.0 >= 0.5:
            tmp +=1
        outtab.append(int(tmp)%dim[i])
    
    return outtab

#PDB-oriented functions

def extract_cryst_card_pdb(pdbfilePath):  #modified from Claudia's alixe library

    for line in open(pdbfilePath):
        m = regexprCRYST1.match(line) # E.G. CRYST1   30.279   91.989   32.864  90.00 112.60  90.00 P 1 21 1      2
        if m:

            unitCellParam=line
            a=float(line[6:15])
            b=float(line[15:24])
            c=float(line[24:33])
            alpha=float(line[33:40])
            beta= float(line[40:47])
            gamma=float(line[47:54])
            spacegroup=line[55:66].strip()
            symbol=1
            try:
                symbol=line[66:70].strip()
            except:
                pass
            out=(a,b,c,alpha,beta,gamma,spacegroup,symbol)

            return out   #returns [a,b,c,alpha,beta,gamma,spacegroup,symbol]
    return None


def extractCoordinatesFromPDB(pathToPDBfile=None, regularExprAtom=regexprATOM2):
    """Extracts coordinates from a pdb file and outputs them in a numpy n x 4 array"""

    PDBorthCoord=np.empty((0,3),float)   #empty array to store the coordinates the first PDB
    nelec_tab=[]  # Will now contain a tuple ('element', Bfactor)
    if pathToPDBfile is not None and os.path.exists(pathToPDBfile):
        natom=0
        unitCellParam=[0,0,0,0,0,0]
        sgnumber = 1
        with open(pathToPDBfile,'r') as f:

            gotCryst = False
            for line in f:
               
                m = regularExprAtom.match(line)

                if not gotCryst:
                    mcryst = regexprCRYST1.match(line) # E.G. CRYST1   30.279   91.989   32.864  90.00 112.60  90.00 P 1 21 1      2
                    if mcryst:
                        a=float(line[6:15])
                        b=float(line[15:24])
                        c=float(line[24:33])
                        alpha=float(line[33:40])
                        beta= float(line[40:47])
                        gamma=float(line[47:54])
                        spacegroup=line[55:66].strip()
                        symbol=1
                        try:
                            symbol=line[66:70].strip()
                        except:
                            pass
                        unitCellParam=(a,b,c,alpha,beta,gamma,spacegroup,symbol)
                        sgnumber = unitCellTools.get_space_group_number_from_symbol(spacegroup)
                        gotCryst  =True
                        print("Unit cell parameters: {} {} {} {} {} {}".format(a,b,c,alpha,beta,gamma))
                        print("Space group {} (number {})".format(spacegroup, sgnumber))
                        print("----------------------")

                elif m:
                    natom+=1

                    #atom coordinates

                    x=float(m.group(12))
                    y=float(m.group(13))
                    z=float(m.group(14))
                    bfact=float(m.group(16))
                    elem=m.group(18).strip().upper()
               
                    # Add lines to the current coordinates
                    PDBorthCoord=np.append(PDBorthCoord,np.array([[x,y,z]]),axis=0)

                    # If the element is not is NELECTRONS, add a density of 1 
                    # if elem in NELECTRONS:
                    #     nelec_tab.append(NELECTRONS[elem])
                    # else:
                    #     nelec_tab.append(1)

                    if elem in chemGaussian.keys():
                        nelec_tab.append((elem,bfact))
                    else:
                        nelec_tab.append(('O', 20))

        print("----- %s atom coordinates recorded from %s.-----\n"%(natom,pathToPDBfile))
        return natom, PDBorthCoord, nelec_tab, unitCellParam, sgnumber             # returns a 1) the number of atoms, 2) a n x 3 numpy array of orthogonal coordinates and 3) the corresponding electron density at these points
    else:
        print("Problem with your extracting coordinates from PDB file %s, the file does not exist or is not accessible"%pathToPDBfile)
        return None, None, None, None, None

def fracCoord2electronDensity(orthCoord=None, elem_tab = None, unitCellParam=[50,50,50,90,90,90], resolution = RESO_CUTOFF, sgnumber =1, writePDB=False, cubeDim=CUBEDIM):
    """ Outputs a numpy 3D array representing the electron density in the unit cell, takes into account space group symmetry operations"""

    gridSpacing = resolution / GRID_DIVIDE

    if orthCoord is not None and elem_tab is not None:

        # Converts input orthogonal coordinates to Fractional coordinates
        deOmat = unitCellTools.deOmat(*unitCellParam[:6])
        omat = unitCellTools.Omat(*unitCellParam[:6])
        Gmat = unitCellTools.Gmat(*unitCellParam[:6])
        symopDic = unitCellTools.get_symops_from_sg_dictionary(sgnumber)
        fracCoord = unitCellTools.ortho2Frac(deOmat,coordMat=orthCoord, belowOne=True)

        # Fill the unit cell with electron density values (0 if no atom, otherwise the corresponding electron density)
        # First, initialize the Numpy array

        nx = int(float(unitCellParam[0]) / gridSpacing) 
        ny = int(float(unitCellParam[1]) / gridSpacing)
        nz = int(float(unitCellParam[2]) / gridSpacing)

        print("Grid spacing along a: {} pt, b: {} pt, c: {} pt".format(nx, ny, nz))

        unitCellArray = np.zeros((nz,nx,ny), dtype=float)     # nsec, nrow, ncol order
        tmpCoordVec=np.zeros(3, dtype=float)
        # Fill up unitCellArray with Density when a voxel corresponds to an atomic position
        nvox=0
        if writePDB:
            pdbfile= open("frac2ed.pdb",'w')
            sgsymbol=unitCellTools.get_full_symbol_from_sg_number(sgnumber)
            cryst1= unitCellTools.writeCRYSTCARDintoPDB(*unitCellParam,sgsymbol=sgsymbol)
            pdbfile.write(cryst1)

        print("Converting PDB coordinates into Gaussian-approximated electron density")
        for operation in symopDic.values():
            # fill up the electron density at all symmetry-equivalent positions

            fracCoordSym = unitCellTools.rotoTranslateFracCoord(fracCoord,operation, belowOne=True)
            for i in range(len(fracCoordSym)):
                nvox += 1
                a = fracCoordSym[i,0]
                b = fracCoordSym[i,1] 
                c = fracCoordSym[i,2]

                a, b, c = indexFromFrac((a,b,c), nx, ny, nz)    # Voxel coordinates of unitCellArray
                #print("-----------")
                #print("a {}, b {}, c{}".format(a,b,c))

                # Electron density at point i
                element= elem_tab[i][0]
                bfact= elem_tab[i][1]
                #print("bfact {}".format(bfact))
                unitCellArray[c, a, b] += gaussianApprox(nterms=NTERMS, elem=element, Bfact=bfact, r=0)
                #print("ED",unitCellArray[a, b, c])

                ################################## Now electron density around point i (Gaussian approximation)
                for shiftz in range(-cubeDim, cubeDim+1):
                
                    for shifty in range(-cubeDim, cubeDim+1):
                    
                        for shiftx in range(-cubeDim, cubeDim+1):
                        
                            a2= a+shiftx
                            b2= b+shifty
                            c2= c+shiftz

                            if not (shiftz == 0 and shifty == 0 and shiftx == 0):
                            
                                # calculate the electron density in the voxels immediatly around the atom's centre
                                #(sum of Gaussians approx)
                                # r is approximated to one voxeldim between neigbouring atoms
                                #print("a2, b2, c2", a2,b2,c2)
                                tmpCoordVec[0]= float(a2) /nx ;
                                tmpCoordVec[1]= float(b2) /ny ;
                                tmpCoordVec[2]= float(c2) /nz ;


                                #print("VEC")
                                #print(fracCoordSym[i,:], tmpCoordVec)
                                distance =unitCellTools.distanceFrac(Gmat,fracCoord1=fracCoordSym[i,:],fracCoord2=tmpCoordVec)
                                #print('distance',distance)
                                unitCellArray[c2%nz, a2%nx, b2%ny] += gaussianApprox(nterms=NTERMS, elem=element, Bfact=bfact, r=distance)
                                #print("    ED around {}".format(unitCellArray[a2%nx, b2%ny, c2%nz]))
                                nvox+=1
                                ################################## CCCCCCC

                if writePDB:
                    orthCoordSym = unitCellTools.frac2Ortho(omat,np.array([[float(a)/nx, float(b)/ny, float(c)/nz]]))
                    line=unitCellTools.replaceATOMrec(inputLine=PDBLINE_C, replaceDic={"serial": nvox, 'x':orthCoordSym[0][0], 'y': orthCoordSym[0][1], 'z':orthCoordSym[0][2] })
                    pdbfile.write(line+"\n")

        print("Done!")
        print("number of voxels assigned : {}".format(nvox))
        if writePDB:
            print("PDB file from fracCoord2electronDensity written as frac2ed.pdb")
            pdbfile.close()
        return unitCellArray #, xdata, ydata, zdata, colors

    else:
        return None

def FT_map2SF(edMap=None,writePHS =False, unitCellParam=None, resolution=RESO_CUTOFF):
    """Fourier transforms a map to a structure factor list, optionally writes a phs file"""
    if edMap is not None:
        #SF=np.fft.fftshift(np.fft.fftn(edMap))
        SF=np.fft.rfftn(np.flip(edMap))
        amplitudes  = np.abs(SF)
        phases = np.angle(SF, deg=True)%360
 
        Gstar = unitCellTools.Gstar(*unitCellParam[:6])
       
        nl= amplitudes.shape[0]
        nh= amplitudes.shape[1]
        nk= amplitudes.shape[2]

        if writePHS:
            with open('map2sf.phs','w') as f:
                for l in range(0, nl):
                    for h in range(0, nh):
                        for k in range(0, nk):
                            currentL= l if l< (1 +nl/2) else -(nl-l)
                            currentH= h if h< (1+ nh/2) else -(nh-h)
                            resol= unitCellTools.resolution(currentH,k,currentL,GstarMatrix=Gstar)
                            #print("h: {}, k: {}, l: {}, resolution: {}".format(currentH,currentK,l, resol))
                            if resol >=resolution or ((l, h, k) == (0,0,0)):
                                indices=(l, h, k)
                                # Note, if the amplitude is too big, reduce the number of figures after comma
                                if len(str(int(amplitudes[indices])))>5:
                                    print("SHERLOCK: \'{}\'".format(str(amplitudes[indices])))
                                    f.write("{:4d}{:4d}{:4d} {:8.1f}{:8.4f}{:8.1f}{:8.2f}\n".format(currentH, k, currentL, amplitudes[indices], 1.0, phases[indices], np.sqrt(amplitudes[indices])))

                                else:
                                    f.write("{:4d}{:4d}{:4d} {:8.2f}{:8.4f}{:8.1f}{:8.2f}\n".format(currentH, k, currentL, amplitudes[indices], 1.0, phases[indices], np.sqrt(amplitudes[indices])))

                print("PHS file from map2sf file written as map2sf.phs (cut at {}A resolution)".format(resolution))
                return SF, os.path.join(os.getcwd(), 'map2sf.phs' )
        return SF

def PHS_2_SFarray(phsFilePath=None, unitCellParam=None, resolution=RESO_CUTOFF):
    """ Parses a PHS file to create a 3d array of structure factors HKL"""

    if phsFilePath is not None and os.path.exists(phsFilePath) and unitCellParam is not None:

        gridSpacing = resolution / GRID_DIVIDE
        nx = int(float(unitCellParam[0]) / gridSpacing) 
        ny = int(float(unitCellParam[1]) / gridSpacing)
        nz = int(float(unitCellParam[2]) / gridSpacing)

        hmax, kmax, lmax = 0, 0, 0

        print("Grid spacing along a: {} pt, b: {} pt, c: {} pt".format(nx, ny, nz))

        hklDic={}
        fomDic={}

        # Retrieving the structure factors from the PHS file:
        with open(phsFilePath, 'r') as f:
            found=False
            nref=0
            for line in f:
                found=True
                m= reHKL.match(line)
                if m:
                    h= int(m.group(1))
                    k= int(m.group(2))
                    l= int(m.group(3))
                    amplitude= float(m.group(4))
                    fom=float(m.group(5))
                    phase = float(m.group(6))
                    sf = amplitude * np.exp(1j*np.radians(phase))
                    nref+=1

                    hmax = h if h>hmax else hmax
                    kmax = k if k>kmax else kmax
                    lmax = l if l>lmax else lmax

                    try:
                        if h>=nx or k>=ny or l>=nz: 
                            print("h: {}, k: {}, l: {}, A: {}, phi: {} fom: {}".format(h,k,l,amplitude, phase,fom))

                        hklDic[(l,h,k)] = sf
                        fomDic[(l,h,k)] = fom
                    except Exception as e:
                        print("problem with indices {}{}{}".format(h,k,l))
                        print(e)

        if found:
            HKLarray = np.zeros((nz, nx, int(1+ny/2.0)), dtype=complex)
            for (hkl_tuple, sf) in hklDic.items():
                l,h,k= hkl_tuple
                l = 2*lmax+2+l if l<0 else l
                h = 2*hmax+2+h if h<0 else h
                k = 2*kmax+2+k if k<0 else k

                HKLarray[l,h,k] = sf   # store the structure factor if the indices exist

            print("PHS_2_SFarray: hmax+1: {}, kmax+1: {}, lmax+1: {}".format(hmax+1,kmax+1,lmax+1))
            print("{} reflections parsed from {}".format(nref, phsFilePath))

            return HKLarray, (nz,nx,ny), fomDic
        else:
            print("PHS_2_SFarray: No reflections found in phs file {}".format(phsFilePath))
            return None, None, None

    else:
        print("ERROR PHS_2_SFarray, file {} cannot be opened!".format(phsFilePath))
        return None, None, None

def FT_SF2electronDens(SFarray=None, writeMAP=False,unitCellParam=None,sgnumber=1, shape=(50,50,50)):
    """Fourier transforms a structure factor file to an electron density map, optionally writes a (Binary map) """ 
    if SFarray is not None:
        electronDensity = np.fft.irfftn(SFarray) #, s=shape)
        print("shape of HKL input:", SFarray.shape)
        print("shape of electron density from SF:", electronDensity.shape)

        # Note it has to be inverted because of the python FT conventions
        electronDensity = np.flip(electronDensity)

        nsec, nrow, ncol = electronDensity.shape

        omat = unitCellTools.Omat(*unitCellParam[:6])


        # test: Write a PDB file out of this density
        if writeMAP:

            pdbfile= open("sf2ed.pdb",'w')
            sgsymbol=unitCellTools.get_full_symbol_from_sg_number(sgnumber)

            cryst1= unitCellTools.writeCRYSTCARDintoPDB(*unitCellParam[:6],sgsymbol=sgsymbol)
            pdbfile.write(cryst1)
            nvox=0
            edMEAN = np.mean(electronDensity)
            edSTD = np.std(electronDensity)
            threshold= edMEAN + 1.5*edSTD

            for z in range(nsec):
                for y in range(ncol):
                    for x in range(nrow):

                        if electronDensity[z,x,y] >= threshold: 
                            nvox +=1
                            xfrac, yfrac, zfrac = (1.0+x) /nrow, (1.0*y)/ncol, (1.0*z) /nsec
                            orthCoordSym = unitCellTools.frac2Ortho(omat,np.array([[xfrac, yfrac, zfrac]]))
                            line=unitCellTools.replaceATOMrec(inputLine=PDBLINE_O, replaceDic={"serial": nvox, 'x':orthCoordSym[0][0], 'y': orthCoordSym[0][1], 'z':orthCoordSym[0][2] })
                            pdbfile.write(line+"\n")
                        
            print("MAP (PDB file) from FT_SF2electronDens written as sf2ed.pdb")
            pdbfile.close()

        return electronDensity

def wMPD(SFarray1, SFarray2, all=True, fomDic=None, noweight=True):
    """ 
    Compute the mean phase difference between phases extracted from arrays of structure factors, make the weights later
    SFarray1 will come from a PDB file while SFarray2 from a PHS file
    """
    print("\n----> MPD calculation")
    print("shape of structure factor array 1: {}".format(SFarray1.shape))
    print("shape of structure factor array 2: {}".format(SFarray2.shape))
    commonshape= [min(x,y) for x,y in zip(SFarray1.shape,SFarray2.shape)]
    print("Common shape: {}\n".format(commonshape))
    SFarray1 = SFarray1[:commonshape[0], :commonshape[1],:commonshape[2]]
    SFarray2 = SFarray2[:commonshape[0], :commonshape[1],:commonshape[2]]

    phaseSet1 = np.angle(SFarray1, deg=True)%360
    phaseSet2 = np.angle(SFarray2, deg=True)%360

    if fomDic is None:
        weights= np.abs(SFarray2)                     # Amplitudes of the PHS file used as weights
    else:
        weights=np.zeros(commonshape,dtype=float)
        for l in range(commonshape[0]):
            for h in range(commonshape[1]):
                for k in range(commonshape[2]):
                    if (h,k,l) in fomDic:
                        try:
                            weights[l,h,k] = fomDic[(l,h,k)]
                        except:
                            pass


    if noweight:
        weights[:,:,:]=1

    del(SFarray1)
    del(SFarray2)

    #print(phaseSet2 - phaseSet1)

    if all:
        return np.absolute(np.sum(np.multiply((phaseSet1 - phaseSet2), weights))  / np.sum(weights))

    else:
        deltaPhiSum=0
        weightSum=0
        for l in range(commonshape[0]):
            for h in range(commonshape[1]):
                for k in range(commonshape[2]):
                    if weights[l,h,k] != 0:
                        deltaPhiSum += (phaseSet1[l,h,k] - phaseSet2[l,h,k]) * weights[l,h,k]
                        weightSum += weights[l,h,k]

        return np.absolute(deltaPhiSum / weightSum)


def map2mapCC(electronDens1, electronDens2, all=True):
    """ 
    Calculate the correlation coefficient between 2 maps, given as voxel 3d arrays
    if all is False, it will only consider voxels which have a density greater than 1 sigma in absolute value
    all True uses Numpy (faster)
    """

    # The formula for the Pearson CC is E[ (X-mean(X)) (Y-mean(Y))] / (sigmaX*sigmaY)

   # print(zip(electronDens1.shape,electronDens2.shape))
    #Only keep the common parts of the two eletron densities
    print("\n----> CC map / model calculation")
    print("shape of electron density 1: {}".format(electronDens1.shape))
    print("shape of electron density 2: {}".format(electronDens2.shape))
    commonshape= [min(x,y) for x,y in zip(electronDens1.shape,electronDens2.shape)]
    electronDens1 = electronDens1[:commonshape[0], :commonshape[1],:commonshape[2]]
    electronDens2 = electronDens2[:commonshape[0], :commonshape[1],:commonshape[2]]

    print("Common shape: {}\n".format(commonshape))
    # substract the mean
    electronDens1 -= np.mean(electronDens1)
    electronDens2 -= np.mean(electronDens2)

    if all:
        if electronDens1.shape == electronDens2.shape:
            return np.mean(np.multiply(electronDens1, electronDens2)) / ((np.std(electronDens1) * np.std(electronDens2)))

        else:
            print("Shapes are not equal: {} and {}".format(electronDens1.shape, electronDens2.shape))
            return None
    else:
        # compare only voxels who have a standardized density superior to 1
        #divide by std:
        electronDens1 /= np.std(electronDens1)
        electronDens2 /= np.std(electronDens2)
        liste1=[]
        liste2=[]
        for i in range(commonshape[0]):
            for j in range(commonshape[1]):
                for k in range(commonshape[2]):
                    if np.absolute(electronDens1[i,j,k])>=1 and np.absolute(electronDens2[i,j,k])>1:
                        liste1.append(electronDens1[i,j,k])
                        liste2.append(electronDens2[i,j,k])
        #print(liste1)
        #print("---\n\n\n")
        #print(liste2)
        liste1 = np.array(liste1)
        liste2 = np.array(liste2)
        liste1 -= np.mean(liste1)
        liste2 -= np.mean(liste2)
        return np.mean(np.multiply(liste1, liste2)) / (np.std(liste1) * (np.std(liste2)))

    
#------------ FUNCTIONS TO TEST WHETHER EVERYTHING WORKS

def edFromPDB(path_to_pdb):

    path_to_pdb = os.path.abspath(os.path.normpath(path_to_pdb))

    if os.path.exists(path_to_pdb):
    # Extract info from the input PDB file
        natom, orthCoord, elem_tab, unitCellParam, sgnumber = extractCoordinatesFromPDB(path_to_pdb)
    if not natom :
        print("NO CRYSTCARD FOUND, QUITTING NOW!")
        sys.exit(1)

    # Create the corresponding electron density array
    return fracCoord2electronDensity(orthCoord=orthCoord, elem_tab = elem_tab, unitCellParam=unitCellParam[:6], resolution = RESO_CUTOFF, sgnumber= sgnumber, writePDB=False)
    


def phsfromPDB(path_to_pdb, ed_PDB=None):

    path_to_pdb = os.path.abspath(os.path.normpath(path_to_pdb))

    if os.path.exists(path_to_pdb):
        # Extract info from the input PDB file
        natom, orthCoord, elem_tab, unitCellParam, sgnumber = extractCoordinatesFromPDB(path_to_pdb)
        if not natom :
            print("NO CRYSTCARD FOUND, QUITTING NOW!")
            sys.exit(1)

        # Create the corresponding electron density array
        if ed_PDB is None:
            electronDensPDB = fracCoord2electronDensity(orthCoord=orthCoord, elem_tab = elem_tab, unitCellParam=unitCellParam[:6], resolution = RESO_CUTOFF, sgnumber= sgnumber, writePDB=False)
        else:
            electronDensPDB = ed_PDB

        # Then turn it into a SFarray
        SFarray , PHSfile= SFarrayPDB= FT_map2SF(edMap=electronDensPDB,writePHS = True, unitCellParam=unitCellParam[:6], resolution=RESO_CUTOFF)

        print("PHS file written as {}".format(PHSfile))

        return SFarray, PHSfile

    else:
        print("Please enter a valid PDB file!")

def PDBandPHSmapCC(path_to_pdb, path_to_phs=None, ed_PDB=None, ed_PHS=None):


    # Extract info from the input PDB file
    natom, orthCoord, elem_tab, unitCellParam, sgnumber = extractCoordinatesFromPDB(path_to_pdb)
    if not natom :
        print("NO CRYSTCARD FOUND, QUITTING NOW!")
        sys.exit(1)

    # Create the corresponding electron density array
    if ed_PDB is None:
        electronDensPDB = fracCoord2electronDensity(orthCoord=orthCoord, elem_tab = elem_tab, unitCellParam=unitCellParam[:6], resolution = RESO_CUTOFF, sgnumber= sgnumber, writePDB=False)
    else:
        electronDensPDB = ed_PDB


    if ed_PHS is None and path_to_phs is not None:
        # Transforming the PHS file to SF
        SFarrayPHS, shape, fomDic = PHS_2_SFarray(phsFilePath=path_to_phs, unitCellParam=unitCellParam[:6], resolution=RESO_CUTOFF)

        # And then to electron density
        electronDensPHS = FT_SF2electronDens(SFarray=SFarrayPHS, writeMAP=True,unitCellParam=unitCellParam[:6],sgnumber=sgnumber,shape=shape)
        del(SFarrayPHS)
    else:
        electronDensPHS = ed_PHS

    # Finally, calculating the CC between the two densities
    cc =  map2mapCC(electronDensPDB, electronDensPHS, all=True)

    print("CC is {}".format(cc))

    return cc



def PDBandPHSwMPD(path_to_pdb=None, path_to_phs=None, sfarray_pdb=None, sfarrayTuple_phs=None):


    # Extract info from the input PDB file
    natom, orthCoord, elem_tab, unitCellParam, sgnumber = extractCoordinatesFromPDB(path_to_pdb)
    if not natom :
        print("NO CRYSTCARD FOUND, QUITTING NOW!")
        sys.exit(1)

    # Create the corresponding electron density array
    if sfarray_pdb is None:
        electronDensPDB = fracCoord2electronDensity(orthCoord=orthCoord, elem_tab = elem_tab, unitCellParam=unitCellParam[:6], resolution = RESO_CUTOFF, sgnumber= sgnumber, writePDB=False)
        
        # Then turn it into a SFarray and pick the PHS file
        SFarray_from_PDB, _ = FT_map2SF(edMap=electronDensPDB,writePHS = True, unitCellParam=unitCellParam[:6], resolution=RESO_CUTOFF)
        del(electronDensPDB)
    else:
        SFarray_from_PDB = sfarray_pdb


    # Now get the SF array from the PHS file
    if sfarrayTuple_phs is None:
        SFarrayPHS, shape, fomDic = PHS_2_SFarray(phsFilePath=path_to_phs, unitCellParam=unitCellParam[:6], resolution=RESO_CUTOFF)
    else:
        SFarrayPHS, shape, fomDic = sfarrayTuple_phs

    print("SF array from PHS shape: {}".format(shape))

    # Calculating the wMPD between the two PHS files
    mpd = wMPD(SFarrayPDB, SFarrayPHS, fomDic=fomDic)

    # print("MPD id {}".format(mpd))

    return mpd



#---------------------- MAIN PROGRAM
if __name__ == '__main__':

    if len(sys.argv)>1 and os.path.exists(sys.argv[1]):
        PDBfile=sys.argv[1]

        # First, create a PHS file from the PDB file, that we will comnpare with the PDB
        print("CREATING ED FROM PDB")
        ed_from_pdb= edFromPDB(PDBfile)

        # Now create a PHS file from the same PDB without recalculating the electron density
        print("CREATING PHS FROM PDB")
        _, PHSfile = phsfromPDB(PDBfile, ed_PDB=ed_from_pdb)


        # Now compare the original PDB with the Generated PHS in terms of MAPcc
        print("COMPARING VALUES")
        PDBandPHSmapCC(path_to_pdb=PDBfile , path_to_phs=PHSfile, ed_PDB=ed_from_pdb)

    else:
        print("Please enter a PDB file and a PHS file to compare")

