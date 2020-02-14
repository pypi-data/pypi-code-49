import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="az_k8s_operations", # Replace with your own username
    version="1.1.21",
    author="1V14713",
    author_email="mathieu.gravil@gmail.com",
    description="Collection of scripts to maintains aks cluster." ,
    long_description_content_type="text/markdown",
    long_description=open('README.md', 'r').read(),
    use_2to3=True,
    url="https://aksterraformstate.z6.web.core.windows.net/az_k8s_operations/",
    packages=setuptools.find_packages(),
      install_requires=[            # I get to this in a second
          'azure-mgmt-keyvault==1.1.0',
      'msrestazure==0.6.2',
      'azure-identity==1.1.0',
      'azure-mgmt-resource==7.0.0',
      'azure-mgmt-web==0.44.0',
      'azure-mgmt-network==8.0.0',
      'azure-mgmt-sql==0.16.0', 
      'azure-mgmt-rdbms==1.9.0',
      'azure-mgmt-storage==7.0.0',
      'azure-storage-blob==2.1.0',
      'azure-storage-file==2.1.0',
      'azure-mgmt-compute==10.0.0',
      'requests>=2.22.0',
      'xlsxwriter>=1.2.1', 
      'datetime>=4.3',
      'sendgrid==6.1.0',
      'filetype==1.0.5',
      'azure-mgmt-containerservice==8.2.0',
      'azure-graphrbac==0.61.1',
      'azure-devops==5.1.0b6',
      'azure-keyvault-secrets==4.0.0',
       ],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=2.7',
)
