import requests

def isempty(urllist):
    if len(urllist) == 0:
        return True
    else:
        return False

class retjoke:
    def __init__(self,category=list(),flags=list(),type=list(),searchstring=""):
        self.category=category
        self.flags=flags
        self.type=type
        self.searchstring=searchstring
    def getjoke(self):
        for i in ["racist","sexist","religious"]:
            if i not in self.flags:
                self.flags.append(i) #adding flags two avoid offensive jokes.
        urlstring = "https://sv443.net/jokeapi/v2/joke"
        flagstring=""
        typp="akaka"
        if isempty(self.category):
            urlstring=urlstring+"/Any"
        else:
            catstring="/"+self.category[0]
            for categ in self.category:
                if self.category.index(categ)!=0:
                    catstring=catstring+","+categ
            urlstring=urlstring+catstring
        if isempty(self.flags)==False:
            flagstring="?blacklistFlags="+self.flags[0]
            for flag in self.flags:
                if self.flags.index(flag)!=0:
                    flagstring=flagstring+","+flag
            urlstring=urlstring+flagstring
        if len(self.type)!=0 and len(self.type)!=2:
            typp="akaka" #flag
            if flagstring!="":
                urlstring=urlstring+"&type="+self.type[0]
            else:
                urlstring=urlstring+"?type="+self.type[0]
            
        if self.searchstring!="":
            if flagstring=="" and typp=="":
                urlstring=urlstring+"?contains="+self.searchstring
            else:
                urlstring=urlstring+"&contains="+self.searchstring
        print(urlstring)
        try:
            jr=requests.get(urlstring)
            jokereq=jr.json()
            print(jr.status_code)
            if jokereq['error']==False:
                if jokereq['type'] == "single":
                    return [jokereq['joke'],"null",jokereq]
                elif jokereq['type'] == "twopart":
                    return [jokereq['setup'],jokereq['delivery'],jokereq]
            else:
                return ["Error!",jokereq['message'],"Please try again!"]
        except Exception as e:
            return ["Error",str(e) +" "+jr.status_code ,"Url might be invalid"]


strst = "\n___________________\n\n\nCategories : Miscellaneous, Programming, Dark \n Black List: nsfw, religious, political, racist, sexist \nTypes :single, twopart\n you can add the seacrh string too\n\n\n"
strst2="a=jk.retjoke(category=[],flags=[],type=[],searchstring="") #create object a ,racist ,sexist and religious jokes are filtered out by default please check the source at : https://github.com/aksty/Jokepy\n"
strst3="a.getjoke() returns a list joke,second part(if the joke as two parts,otherwise null),json from url(dictionary) if everything works \notherwise returns list with error messages\n\n_____________________\n"

info=strst+strst2+strst3