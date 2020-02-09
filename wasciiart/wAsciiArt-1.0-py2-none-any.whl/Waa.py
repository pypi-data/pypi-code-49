class Waa(object):
    def __str__(self):
        return("witrdotnet ascii art")

    def getAsciiArt(self):
        return """
           _ _           _       _              _   
 __      _(_) |_ _ __ __| | ___ | |_ _ __   ___| |_ 
 \ \ /\ / / | __| '__/ _` |/ _ \| __| '_ \ / _ \ __|
  \ V  V /| | |_| | | (_| | (_) | |_| | | |  __/ |_ 
   \_/\_/ |_|\__|_|  \__,_|\___/ \__|_| |_|\___|\__|
                                                            
        """
# Testing
if __name__ == "__main__":
    waa = Waa()
    print(waa.getAsciiArt())
