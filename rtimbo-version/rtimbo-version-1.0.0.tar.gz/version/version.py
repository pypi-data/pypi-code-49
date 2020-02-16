import re

class Version:
    __errorStr = "'{}' not supported between instances of '{}' and '{}'"
    __FINAL = "z"
    
    def __init__(self, versionString):
        regex = "^v?(\d+)(?:.(\d+))?(?:.(\d+))?(?:-?(a|b|rc)(\d+)?)?$"
        m = re.match(regex, str(versionString).strip(), flags=re.IGNORECASE)
        
        if m == None:
            raise ValueError('{arg} doesn\'t match expected version regex "{regex}"'.format(arg=versionString, regex=regex))
        
        self.major =int(m.group(1))
        self.minor = int(m.group(2)) if m.group(2) != None else 0
        self.patch = int(m.group(3)) if m.group(3) != None else 0
        self.candidate = m.group(4) if m.group(4) != None else self.__FINAL # "z" so string comparison works
        self.candidate_number = int(m.group(5)) if m.group(5) != None else 0

    def __repr__(self):
        return '{cls}("{str}")'.format(cls=self.__class__.__name__, str=self.__str__())

    def __str__(self):
        return "v{major}.{minor}.{patch}{release}".format(
            major=self.major,
            minor=self.minor,
            patch=self.patch,
            release="" if self.candidate == self.__FINAL else
                    self.candidate + str(self.candidate_number))

    def __segments(self):
        return [self.major, self.minor, self.patch, self.candidate, self.candidate_number]
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            for s1, s2 in zip(self.__segments(), other.__segments()):
                if s1 < s2:
                    return True
                if s1 > s2:
                    return False
            return False
        if isinstance(other, int) or isinstance(other, float):
            return self < Version(other)
        
        raise TypeError(self.__errorStr.format("<",self.__class__, type(other)))

    def __le__(self, other):
        if isinstance(other, self.__class__):
            for s1, s2 in zip(self.__segments(), other.__segments()):
                if s1 < s2:
                    return True
                if s1 > s2:
                    return False
            return True
        if isinstance(other, int) or isinstance(other, float):
            return self <= Version(other)
        
        raise TypeError(self.__errorStr.format("<=",self.__class__, type(other)))

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            for s1, s2 in zip(self.__segments(), other.__segments()):
                if s1 < s2:
                    return False
                if s1 > s2:
                    return True
            return False
        if isinstance(other, int) or isinstance(other, float):
            return self > Version(other)
        
        raise TypeError(self.__errorStr.format(">",self.__class__, type(other)))

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            for s1, s2 in zip(self.__segments(), other.__segments()):
                if s1 < s2:
                    return False
                if s1 > s2:
                    return True
            return True
        if isinstance(other, int) or isinstance(other, float):
            return self >= Version(other)
        
        raise TypeError(self.__errorStr.format(">=",self.__class__, type(other)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            for s1, s2 in zip(self.__segments(), other.__segments()):
                if s1 < s2:
                    return False
                if s1 > s2:
                    return False
            return True
        if isinstance(other, int) or isinstance(other, float):
            return self == Version(other)
        
        raise TypeError(self.__errorStr.format("==",self.__class__, type(other)))