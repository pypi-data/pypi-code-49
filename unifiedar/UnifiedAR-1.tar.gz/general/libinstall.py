
import subprocess
import sys
import os

def install_libs():
    
    reqs =subprocess.check_output(['pip', 'install','--upgrade', '-q','tqdm']) #for progressbars
    from tqdm import tqdm
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    packages=[
        'numpy',
        'pandas',
        'wget',
        'ipympl',
        'intervaltree',
        'tensorflow',
        'tensorflow-plot',
        'scikit-optimize',
        'matplotlib',
        'seaborn',
        'plotly',
		'import-ipynb',
        'memory_profiler',
        'ward-metrics'
    ]
    pbar = tqdm(packages)
    for pack in pbar:
        pbar.set_description("Installing %s" % pack)
        packname=pack.split('<')[0]
        if not(pack in installed_packages):
            os.system('pip install --upgrade -q '+pack)
    pbar.set_description("Everything Installed")
    pbar.update(len(packages))

# install_libs()



def install_lab_libs():
    os.system('export NODE_OPTIONS=--max-old-space-size=4096')
    os.system('jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build')
    os.system('jupyter labextension install jupyterlab-plotly --no-build')
    os.system('jupyter labextension install plotlywidget --no-build')
    os.system('jupyter labextension install jupyter-matplotlib --no-build')
    

    os.system('jupyter lab build')
    os.system('unset NODE_OPTIONS')
    

# status=subprocess.check_output(['jupyter', 'labextension', 'check', 'plotlywidget'])
# if("enabled" in status):
#     print('Skip! labextensions are installed');
# else:
#     pass#install_lab_libs();

