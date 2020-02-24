'''This module is for making an empty GitBuilding project.

It is used when you run `gitbuilding new`'''

def emptyconfig():
    '''This function returns and example config'''

    return '''#LandingPage this is required to build HTML
LandingPage: landing.md

# Recommended information
Authors:
    - My Name

Affiliation: My Affiliation

License: Licence Not Specified

Email: my-email@my.domain


#Uncomment below to add custom categories
#CustomCategories:
#    PrintedTool:
#        Reuse: False
#        DisplayName: Printed tools

#Uncomment below to set a custom default category
#DefaultCategory: PrintedTool

#Uncomment below to set the title for the bill of material on a page
#PageBOMTitle: '##For this step you will need'

#Uncomment below to override the project title
#Title: 'My project'

#Uncomment below to set a custom Website root for static HTML builds
#WebsiteRoot: '/path/'

#Uncomment below to disable fussy warnings
#Fussy: False

'''

def emptylanding():
    '''This function returns and example landing page'''

    return '''# Test Project

This is a great place to start making your documentation!

You should link to a couple of pages:

* [.](testpage1.md){step: True}
* [.](testpage2.md){step: True}

And you should definitely let people know about the {{BOMlink}} page.'''

def testpage(name):
    '''This function returns and example instruction page'''

    return '''[M4x10 screws]:Parts.yaml#M4x10PanSteel
# %s


{{BOM}}

## Method
This page should have some instructions for things in your project instead it just has a link for three [M4x10 screws]{Qty: 3} and another link to use [two more][M4x10 screws]{Qty: 2}.'''%name

def basicparts():
    '''This function returns and example part library'''

    return '''
M4x10PanSteel:
    Name: M4x10 Pan Head Steel
    Description: >
        This is lots of text
        about some screw?
    Specs:
        Head: Pan
        Length: 10 mm
        Material: Stainless Steel
        Pitch: 0.7
    Suppliers:
        RS:
            PartNo: 528-817
            Link: https://uk.rs-online.com/web/p/machine-screws/0528817/
        McMasterCarr:
            PartNo: 90116A207
            Link: https://www.mcmaster.com/90116A207'''