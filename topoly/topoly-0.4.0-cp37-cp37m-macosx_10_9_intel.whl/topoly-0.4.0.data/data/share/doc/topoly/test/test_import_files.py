import os
import urllib

from topoly.graph import Graph

INPUT_FOLDER = '/tmp'
proteins = [('6i7s', 'A'), ('1j85', 'A'), ('4wlr', 'A'), ('3bjx', 'A')]
file_types = ['cif', 'pdb', 'nxyz']

PDB_URL="http://files.rcsb.org/download/{0}.{1}"
KNOTPROT_URL="https://knotprot.cent.uw.edu.pl/chains/{0}/{2}/chain.xyz.txt"

download_urls = {'cif': PDB_URL, 'pdb': PDB_URL, 'nxyz': KNOTPROT_URL}


def download_if_not_exist(url, filename, dir=INPUT_FOLDER):
    file = os.path.join(dir, filename)
    if not os.path.isfile(file):
        f = urllib.request.urlopen(url)
        fw = open(file, "wb")
        fw.write(f.read())
        fw.close()
        f.close()
    return file


# Setup test - download input files
def setup_module():
    for prot in proteins:
        for f_type in file_types:
            download_if_not_exist(download_urls[f_type].format(prot[0], f_type, prot[1]), prot[0] + '.' + f_type)


def import_coords_for_prot(protein):
    from Bio import BiopythonWarning
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', BiopythonWarning)
        res = {}
        prev = None
        for f_type in file_types:
            file = os.path.join(INPUT_FOLDER, protein[0] + '.' + f_type)
            res[f_type] = str(Graph(file, chain=protein[1]).coordinates)
            #print(res[f_type])
            if prev:
                assert res[f_type]==prev


# Actual testing
def test_import_coords():
    for prot in proteins:
        import_coords_for_prot(prot)

setup_module()
test_import_coords()