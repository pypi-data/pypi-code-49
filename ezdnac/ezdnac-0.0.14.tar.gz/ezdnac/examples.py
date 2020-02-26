
from ezdnac import device, apic


#####################################################################################################################
## This file is holding some examples of how to use the ezdnac.py 
##
####Written by Johan Lahti, CCIE60702, Conscia Sweden.###############################################################
#####################################################################################################################

####################################################################################################################
## The driver behind the creation of ezdnac (easy dna-c) is to make it easier to script towards its API. 
## Some abstraction is done, for example the management of authorization. The module will automatically 
## use the auth-api to athenticate and autorize and after that reuse the authToken for the rest of the script runtime
##
## ezdnac.py defines two classes, one for the DNAC itself and its parameters. 
## and one for the device/devices you want to manage. 
## The apic class is holding all functions that manages dnac-wide stuff such as authentication, topology and
## templates.
##
## The device holds all functions that is necessary to populate a device, some parts are automatically always 
## populated using the apic class such as hostname, type etc. 
##
###################################    APIC and Device    #######################################################
#################################################################################################################
## The device class also holds operational functions, such as template deployment for a given device.
## 
## First example shows how to initalize a dna-c apic, using the apic class. The init needs following inputs:
## 1. ip address of the dna-c
## 2. username
## 3. password
## -port (optional, unless specified port 443 will be used.)
## -timeout (optinal, default 5sek)
## Second example shows how to initialize an object for a specific device, 
## enter serialnumber or deviceId and apic-object. 
## 
## In the example we initialize two nodes device1 and device2.
###################################################################################################################
## Example 1: 
#dna_c = apic('10.10.100.40','admin', 'password, timeout=2')
##
## Example 2:
#device1 = device(sn='ABCDEF12345', dna_c)
#device2 = device(id='1111111-aaaa-2222-bbbb-333333333333', dna_c)
#
###################################    Device    ##################################################################
###################################################################################################################
## Now that the objects are created, you can refer to its' 
## defined attributes such as hostname and softwareType 
## 
####################################################################################################################
## Example: 
#print (device1.hostname)
#print (device1.softwareType + " ver: " + device1.softwareVersion)
#print (device2.hostname)
#print (device2.platform)
#
#####################################################################################################################
####################################################################################################################
## With the function getTopology in the device class, it will return a dictionary 
## with all links for the dnac that the device is claimed to. Note that this includes the whole
## Topology as known to the dnac.
##  
## 
####################################################################################################################
## Example: 
# all_connections = device1.getTopology()
#
####################################################################################################################
####################################################################################################################
## The function getSites gives you a dictionary of all sites. IF you specify site=sitename in the input that site 
## is returned only. Sitename should include the whole siteNameHierarchy, ex "Global/Area/sitename"
## 
####################################################################################################################
####################################################################################################################
## With the function getConnections, you will get all connections for the specified device.
##  You can use keys such as 'remotenode' or 'localif'. 
## The keys prefixed with 'remote' will always refer to the other side from the specified switches' perspecitve
##  In the example below we retreive all connections to device1
##
####################################################################################################################
## Example: 
#device_connections = device1.getConnections()
#
#
#print (" - Displaying device connections - ")
#
#for connection in device_connections:
#	print ("Device is connected to " + connection['remotenode'])
#	print ("Remote interface: " + connection['remoteif'])
#	print ("Local interface: " + connection['localif'])
#
#
###################################################################################################################
###################################################################################################################
##To deploy a template following steps is necessary:
## 1. define a dictionary containing all template variables
## 2. append the template id to the dictionary
## 3. use the function deployTemplate in the device class with the deviceId and params-dictionary as input
##
## To translate template name to template id, use the function getTemplateid in the
## apic class.
##
## Example showing the workflow. 
## 1. initialize the dnac
## 2. translate template name to template id
## 3. initialize the device to deploy the template to 
## 4. define the template input dictionary
## 5. run the deploy
##
####################################################################################################################
####################################################################################################################
## Another handy function is findNextPortchannel under the device class. It discovers
## the next configurable port-channel id for the device. Let's say id 1,4 and 8 are configured
## already, it will return the first free id which would be 2 in that case.
## 
####################################################################################################################
## Example: 
#apic_sweden = apic('ip address of dna-c','username', 'password')
#templateId = (apic_sweden.getTemplateid('template_name'))
#device1 = device('ABCDEF12345', dna_c)
#
#params = {
#"description": 'STuffz',
#"interface": 'Gi1/0/2'
#}
#
#device1.deployTemplate(templateId,dict(params))

###################################    APIC      ################################################################
#################################################################################################################
## Here comes some apic specific features. The first one written was the management of templates. 
## The functions are named pullTemplates and pushTemplates. And are very easy to use. Input parameters area
## for the pullTemplates: 
##  -  path (optional - directory where the templates shall be stored (default is local path))
##  -  project (optional, if only a specific project is to be pulled. Default is all projects)
##
####################################################################################################################
#
# #This line gets all templates from 'Day1' project and stores them in the folder 'templates'
#print (dna_c.pullTemplates(project='Day1', path='templates/'))
#
# #This line pushes all templates in the given folder to the DNA-C.
#
# print (dna_c.pushTemplates(path=')'templates/')
####################################################################################################################
## The project/template tree matches on it's name. The idea is to enable sync between more than one DNA-C, hence matchin
## on the id is not appropriate. It matches on the whole tree, meaning if the template name exists under another project
## it is still going to be seen as a unique template. 
## When pushing a template, the function will do multiple steps:
## 1. Check if the project exists.
## 2. Check if the template exists.
## If the project does not exist = create project and create template
## If the project exists but not the template = create the tempalte within the project.
## If the template exists = Update it according to the local file. 
## This enables offline editing as well as syncinc templates and storing them elsewhere like GIT.
####################################################################################################################
####################################################################################################################






