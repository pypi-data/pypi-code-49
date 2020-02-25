import re

AAs= set('ALA,ARG,ASN,ASP,CYS,GLN,GLU,GLY,HIS,ILE,LEU,LYS,MET,PHE,PRO,SER,THR,TRP,TYR,VAL'.split(','))
atom_names = [i.strip() for i in 'C   ,  CA  ,  CB  ,  CD  ,  CD1 ,  CD2 ,  CE  ,  CE1 ,  CE2 ,  CE3 ,  CG  ,  CG1 ,  CG2 ,  CH2 ,  CZ  ,  CZ2 ,  CZ3 ,  H   ,  HA  ,  HB  ,  HC  ,  HD1 ,  HD2 ,  HE  ,  HE1 ,  HE2 ,  HE3 ,  HG  ,  HG1 ,  HH  ,  HH2 ,  HO  ,  HOC ,  HZ  ,  HZ2 ,  HZ3 ,  N   ,  ND1 ,  ND2 ,  NE  ,  NE1 ,  NE2 ,  NH1 ,  NH2 ,  NZ  ,  O   ,  OC  ,  OD1 ,  OD2 ,  OE1 ,  OE2 ,  OG  ,  OG1 ,  OH  ,  SD  ,  SG  , 1H   , 1HA  , 1HB  , 1HD  , 1HD1 , 1HD2 , 1HE  , 1HE2 , 1HG  , 1HG1 , 1HG2 , 1HH1 , 1HH2 , 1HZ  , 2H   , 2HA  , 2HB  , 2HD  , 2HD1 , 2HD2 , 2HE  , 2HE2 , 2HG  , 2HG1 , 2HG2 , 2HH1 , 2HH2 , 2HZ  , 3HB  , 3HD1 , 3HD2 , 3HE  , 3HG1 , 3HG2 , 3HZ'.split(',')]
metals = 'ZN,CA,P,MG,MN,FE,CO,NA,K'.split(',')

def atom_type(atom,resid=None):
    '''
    //simplest representation
    //1-aliphatic carbon and an alpha carbon- maybe separate later
    //2 - aromatic carbon, 3-amide nitrogen (main chain), 
    //4 - carbonyl carbon (main chain),
    //5- hydroxyl oxygen, 6-carboxyl oxygen, 7-hydroxyl aromatic, 8 - carbonyl oxygen(side chain), 
    //9 - amide nitrogen (side chain), 10-amide carbon (main chain), 11 - amide carbon (side chain)
    //12 - carboxyl carbon, 13-aromatic nitrogen (TRP), 14 - MET sulfur, 15 - CYS sulfur, 16-guanidinium carbon
    //17- aromatic nitrogen (HIS) 18-amine nitrogen (secondary), 19- amine nitrogen (primary), 20 - carbonyl oxygen(main chain)
    //21-29: ZN,CA,P,MG,MN,FE,CO,NA,K (metals)
    '''
    atom = re.match("[A-Z]+", atom).group() # remove numbers from atom definitions
    if resid is not None:
        if atom in set(['CA', 'CB']):
            return 0
        elif atom=='C':
            return 3
        elif atom=='CG':
            if resid in set(['GLN','GLU','ILE','LEU','LYS','MET','PRO','THR','VAL','ARG']):
                return 0
            elif resid in set(['PHE', 'TYR', 'TRP', 'HIS']):
                return 1
            elif resid=='ASN':
                return 10
            elif resid =='ASP':
                return 11
        elif atom =='CD':
            if resid in set(['ARG',"ILE","LEU","LYS","PRO"]):
                return 0
            elif resid=='GLN':
                return 10
            elif resid=='GLU':
                return 11
            elif resid in set(['PHE', 'TYR', 'TRP','HIS']):
                return 1
        elif atom=='CE':
            if resid in set(['HIS', 'PHE', 'TRP', 'TYR']):
                return 1
            elif resid in set(['LYS', 'MET']):
                return 0
        elif atom=='CZ':
            if resid in set(['PHE', 'TRP', 'TYR']):
                return 1
            elif resid=='ARG':
                return 15
        elif atom =='CH':
            return 1
        elif atom=='SG':
            return 14
        elif atom=='SD':
            return 13
        elif atom=='O':
            return 19
        elif atom=='OD':
            if resid=='ASN':
                return 7
            elif resid=='ASP':
                return 5
        elif atom=='OG':
            return 4
        elif atom=='OE':
            if resid=='GLN':
                return 7
            elif resid =='GLU':
                return 5
        elif atom=='OH':
            return 6
        elif atom=='N':
            return 2
        elif atom =='NE':
            if resid=='ARG':
                return 17
            elif resid=='HIS':
                return 16
            elif resid=='TRP':
                return 12
            elif resid =='GLN':
                return 8
        elif atom=='NH':
            return 18
        elif atom=='ND':
            if resid=='ASN':
                return 8
            elif resid=='HIS':
                return 16
        elif atom=='NZ':
            return 18
        else:
            print ("unidentified atom type" % atom)
            return 29
    else:
        return metals.index(atom) +20
