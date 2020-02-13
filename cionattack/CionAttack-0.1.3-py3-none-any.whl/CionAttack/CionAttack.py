import tkinter, pandas, random, turtle
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

class Earth(tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        tkinter.Canvas.__init__(self, *args, **kwargs)
        self.tag_bind('CLICK_AREA', '<Button>', self.onClickArea)
        self.rectangle = []
        self.Colors = []
        self.ListInList = []
        self.Tmp = []
        self.Selected = {}

    def rgb(self, x, y, z):
        return "#%02x%02x%02x" % (x, y, z)

    def Set(self, ListInList, Track=[], width=25, height=10):

        self.ListInList = ListInList

        self.Colors = ['#0408f1', '#20f303', '#f53603', '#000000', '#deaf27', '#f4ff03', '#03aa8f', '#eb7b4a',
                       '#42efe3',
                       '#bfb9c9', '#5027c1', '#b44340', '#e151ae', '#c78993', '#c0ed1f', '#f37777', '#730f45',
                       '#cb9821',
                       '#d3f5c0', '#cd48a8', '#f701c0', '#5772ad', '#4f9e14', '#589dba', '#34db7e', '#217aff',
                       '#792791',
                       '#d95787', '#7b030e', '#2a3e33', '#52a37c', '#deaf27']

        for i in range(len(ListInList)):
            y = 0
            for j in range(len(ListInList[i])):
                x1 = j * width
                y1 = i * height
                x2 = x1 + width
                y2 = y1 + height

                Colors = self.Colors
                if Track:
                    if [y, i] in Track:
                        Colors = self.Colors[::-1]
                self.rectangle.append(
                    [self.create_rectangle(x1, y1, x2, y2, fill=Colors[ListInList[i][j]], tags=['CLICK_AREA', i, j]), i,
                     y])
                y += 1

        self.update()

    def onClickArea(self, event):
        a = event.widget.find_closest(event.x, event.y)
        if a[0] in self.Tmp:
            del self.Selected[self.rectangle[a[0] - 1][2]][self.rectangle[a[0] - 1][1]]
            self.Tmp.remove(a[0])
            Colors = self.Colors
        else:
            Colors = self.Colors[::-1]
            self.Tmp.append(a[0])

            if not self.rectangle[a[0] - 1][2] in self.Selected:
                self.Selected[self.rectangle[a[0] - 1][2]] = {}

            if not self.rectangle[a[0] - 1][1] in self.Selected[self.rectangle[a[0] - 1][2]]:
                self.Selected[self.rectangle[a[0] - 1][2]][self.rectangle[a[0] - 1][1]] = \
                self.ListInList[self.rectangle[a[0] - 1][1]][self.rectangle[a[0] - 1][2]]

        self.itemconfig(self.rectangle[a[0] - 1][0],
                        fill=Colors[self.ListInList[self.rectangle[a[0] - 1][1]][self.rectangle[a[0] - 1][2]]])


class List():
    def Space_Bar(self,List):
        tmp,b = [], None
        for n in List:
            if not b == None:
                tmp.append(len(range(n < b and n or b,n < b and b or n)))
            b = n
        return tmp

    def expression(self,List1,List2,Command):
        expression = 0
        for l2 in List2:
            Set = None
            for command in Command:
                if command == '>':
                    if l2 < 0 and min(List1) < 0 and min(List1) > l2:
                        Set = True
                    elif l2 >= 0 and max(List1) >= 0 and max(List1) < l2:
                        Set = True
                elif command == '<':
                    if l2 <= 0 and min(List1) <= 0 and min(List1)   < l2:
                        Set = True
                    elif l2 >= 0 and max(List1) >= 0 and max(List1) > l2:
                        Set = True
            if Set:
                expression += 1
        return expression

    def Count(self, List):
        c, d = [List.count(x) for x in List], {}
        for t in List:
            if not c[List.index(t)] in d:
                d[c[List.index(t)]] = []
            not t in d[c[List.index(t)]] and d[c[List.index(t)]].append(t)
        return d

    def Part(self, List, Part):
        l = []
        while True:
            l.append(List[:Part])
            List = List[Part:]
            if not List:
                return l

    def Start_at(self, ListOrDict, Sop=None, Start=None, End=None):
        if type(ListOrDict) == dict:
            List = ListOrDict.keys()
        else:
            List = ListOrDict
        List_, index = [], None

        for n in range(100):
            for d in List:
                if d == (d < 0 and n - n - n or n):
                    List_.append(d)

        if Start and End:
            for n in range(Start, End):
                if n in List_:
                    return List_[List_.index(n):] + List_[:List_.index(n)]

        if Start and Sop:
            for n in range(Sop, Start):
                if n in List_:
                    return List_[List_.index(n):] + List_[:List_.index(n)]

        if type(ListOrDict) == dict:
            Dict = {}
            for n in List_:
                for Key, Values in ListOrDict.items():
                    if n == Key:
                        Dict[n] = Values
            return Dict
        return List_

    def PartListInList(self, ListInList):
        KeyValues, index, Max = {}, 0, 0
        for l in ListInList:
            if len(l) > Max:
                Max = len(l)

        for n in range(Max):
            c = []
            for l in ListInList:
                try:
                    c.append(l[n])
                except:
                    pass
            if not index in KeyValues:
                KeyValues[index] = []
            KeyValues[index] += c
            index += 1
        return KeyValues

    def TryInTry(self, ListInList):
        TryInTry = []
        for l in ListInList:
            List, Back, Down, Index, TryN, Start = [], None, None, 0, 0, 0
            for i in l:
                if i == Back or Back == None:
                    TryN += 1
                else:
                    List.append((Back, Start, TryN == 0 and 1 or TryN))
                    Down, TryN, Start = True, 1, Index

                Back = i
                Index += 1

            not Down and List.append((i, Start, TryN == 0 and 1 or TryN))
            TryInTry.append(List)
        return TryInTry

    def IndexLopPart(self, ListInList, Part):
        for List in ListInList:
            tmp = []
            Index = List.copy()

            for q in range(len(List)):
                for i in range(len(List)):
                    if len(List) > i + 1:
                        a, b = List[i], List[i + 1]
                        List[i + 1], List[i] = a, b
                        index = 0
                        while True:
                            List = List[1:] + [List[0]]
                            for n in range(len(List)):
                                if len(List[n:n + Part]) == Part:
                                    d, index_ = {}, 0
                                    for i in range(n, n + Part):
                                        d[Index.index(List[n:n + Part][index_])] = List[n:n + Part][index_]
                                        index_ += 1
                                    if not d in tmp:
                                        tmp.append(d)
                                        yield d

                            index += 1
                            if index == len(List) + 1:
                                break

    def NextPart(self, ListInList, Part):
        tmp = []
        for List in ListInList:
            index = 0
            while True:
                List = List[1:] + [List[0]]
                for n in range(len(List)):
                    if len(List[n:n + Part]) == Part:
                        d, index_ = {}, 0
                        for i in range(n, n + Part):
                            d[i] = List[n:n + Part][index_]
                            index_ += 1
                        if not d in tmp:
                            tmp.append(d)
                            yield d

                index += 1
                if index == len(List) + 1:
                    break

    def Track(self, ListInList, List):
        Track = []
        for q in range(len(max(ListInList))):
            Dict = {}
            for i in range(len(ListInList)):
                try:
                    if not i in Dict:
                        Dict[i] = {}
                    Dict[i] = {'q': ListInList[i][q], 'xy': [q, i]}
                except:
                    pass

            for m in List:
                Set, l = True, []
                for k, v in m.items():
                    l.append(Dict[k]['xy'])
                    if not v == Dict[k]['q']:
                        Set = None

                if Set and not l in Track:
                    Track += l
        return Track

    def Spees(self, ListInList, List):
        spess, start, index, o, p = [], 0, 0, None, None
        for s in ListInList:
            Set = None
            for q in List:
                if not False in [x in s for x in q]:
                    if o == None:
                        o = index
                    elif not o == None:
                        p = index
                    Set = True
            if Set:
                start += 1
            else:
                spess.append(start)
                start = 0
            index += 1
        return {'Spees': spess, 'StartEnd': [o, p]}

    def IfSpees(self, PartList, ListInList, IfSpees=[], Start=[], End=[], InCount=[{}], Count={}):
        ListTrackAdd, ListTrackLen, ListTrackIndex = [], [], []
        for Part in PartList:
            Spees = self.Spees(ListInList=ListInList, List=[Part.values()])
            l = True
            if IfSpees:
                if not (not None in [Spees['StartEnd'][0], Spees['StartEnd'][1]] and (
                        Spees['StartEnd'][1] - Spees['StartEnd'][0] in IfSpees)):
                    l = None

            if Start and End:
                if not None in [Spees['StartEnd'][0], Spees['StartEnd'][1]]:
                    if not (Spees['StartEnd'][0] in Start and Spees['StartEnd'][1] in End):
                        l = None
                else:
                    l = None

            if Count:
                for Dict in Count:
                    Set = True
                    for k, v in Dict.items():
                        SpeesSpees = Spees['Spees']
                        if 'XY' in v:
                            SpeesSpees = Spees['Spees'][v['XY'][0]:v['XY'][1]]

                        if not SpeesSpees.count(k) in v['Count']:
                            Set = None
                    if Set:
                        break
                l = l and Set
            if InCount:
                for Dict in InCount:
                    Set = True
                    for k, v in Dict.items():
                        if not Spees['Spees'][k] == v:
                            Set = None
                    if Set:
                        break
                if not Set:
                    l = None

            if (IfSpees or InCount or (Start and End)) and l:
                ListTrackAdd.append(Part)
                ListTrackIndex.append((Spees['StartEnd'][0], Spees['StartEnd'][1]))
                if type(Spees['StartEnd'][0]) == int and type(Spees['StartEnd'][1]) == int:
                    ListTrackLen.append(Spees['StartEnd'][1] - Spees['StartEnd'][0])
                else:
                    ListTrackLen.append(None)

        return {'ListTrackAdd': ListTrackAdd, 'ListTrackLen': ListTrackLen, 'ListTrackIndex': ListTrackIndex}


class Addrees():
    def __init__(self):
        self.Addrees = {'db': {}}

    def ArrangingAddrees(self, List, Index):
        l = [Values[Index] for Values in List]
        for Tap in range(min(l), max(l) + 1):
            for Addrees in List:
                if Addrees[Index] == Tap:
                    yield Addrees

    def CreateAddrees(self, ListNumTap,Try=1,Range=True, Arranging=None):
        Tap_, Exec, Index = 0, 'def Create():\n', 0
        for l in ListNumTap:
            if Range:
                for n in range(l[0]):
                    Exec  += '{tap}for i{n} in range({Start},{end}):\n'.format(tap='\t' * (Index + 1), n=Index, Start=Tap_,end=Tap_ + l[1])
                    Tap_  += l[1]
                    Index += 1
            else:
                for n in range(l[0]):
                    Exec += '{tap}for i{n} in {List}:\n'.format(tap='\t' * (Index + 1), n=Index,List=l[1])
                    Index += 1

        Exec += '{tap}for i in range({Try}):{tap}\tyield {List}\n'.format(Try=Try,tap='\t' * (Index + 1),List=str(['i' + str(x) for x in range(Index)]).replace("'", ''))
        exec(Exec)
        if not Arranging == None:
            return self.ArrangingAddrees(List=list(locals()['Create']()), Index=Arranging)
        else:
            return locals()['Create']()

    def Part(self, List, Part):
        for l in List:
            index = 0
            while True:
                d = {}
                for i in range(index, index + Part):
                    if len(l) > i:
                        d[i] = l[i]
                if len(d) == Part:
                    yield d

                l = l[1:] + [l[0]]
                if index == len(l):
                    break
                index += 1

    def AddreesIndex(self, ListNumTap):
        l = {}
        for Addrees in self.CreateAddrees(ListNumTap=ListNumTap):
            for i in Addrees:
                if not Addrees.index(i) in l:
                    l[Addrees.index(i)] = []
                not i in l[Addrees.index(i)] and l[Addrees.index(i)].append(i)
        return l

    def AddreesToZero(self, Addrees, ListNumTap, In=None):
        Tap_, Index = 0, 0

        if In:
            Addrees_ = {}
        else:
            Addrees_ = []

        for List in ListNumTap:
            for n in range(List[0]):
                if In:
                    if Index in Addrees:
                        if type(Addrees[Index]) == int:
                            Addrees_[Index] = Addrees[Index] - Tap_
                else:
                    if type(Addrees[Index]) == int:
                        Addrees_.append(Addrees[Index] - Tap_)

                Tap_, Index = Tap_ + List[1], Index + 1
        return Addrees_

    def ZeroToAddrees(self, Addrees, ListNumTap, In=None):
        Tap_, Index = 0, 0
        if In:
            Addrees_ = {}
        else:
            Addrees_ = []

        for List in ListNumTap:
            for n in range(List[0]):
                if In:
                    if Index in Addrees:
                        if type(Addrees[Index]) == int:
                            Addrees_[Index] = Tap_ + Addrees[Index]
                else:
                    if type(Addrees[Index]) == int:
                        Addrees_.append(Tap_ + Addrees[Index])

                Tap_, Index = Tap_ + List[1], Index + 1
        return Addrees_


class Data():
    def __init__(self):
        self.Data = {'db': {}, 'Class': {'Addrees': Addrees(), 'List': List()}}

    def Create(self, Name):
        if not Name in self.Data['db']:
            self.Data['db'][Name] = {'db': {}, 'AddreesToMap': {'BackZero': []}}

    def Name(self):
        return list(self.Data['db'].keys())

    def Delete(self, Name, Values):
        for Key_, Values_ in self.Data['db'][Name]['db'].items():
            for Delete in Values:
                if Delete in Values_:
                    del Values_[Delete]

    def DataAndAddrees(self, Name):
        s = {'Addrees': [], 'Data': []}
        for Key, Values in self.Data['db'][Name]['db'].items():
            for a in ['Addrees', 'Data']:
                if a in Values:
                    s[a].append(Values[a])
        return s

    def Copy(self,Name,ClassDataShow):
        self.Create(Name=Name)
        for Key,Values in ClassDataShow.items():
            self.Data['db'][Name]['db'][len(self.Data['db'][Name]['db'])] = Values.copy()

    def SetMap(self, Name):
        Num = {}
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Addrees' in Values:
                Num = not Num and [{'n': 1} for i in range(len(Values['Addrees']))] or Num

                Values['Zero'] = {}
                for Tap in Values['Addrees']:
                    if 'b' in Num[Values['Addrees'].index(Tap)] and Num[Values['Addrees'].index(Tap)]['b'] == Tap:
                        Num[Values['Addrees'].index(Tap)]['n'] += 1
                    else:
                        Num[Values['Addrees'].index(Tap)]['n'] = 1
                    if Values['Addrees'].index(Tap) == len(Values['Addrees']) - 1:
                        Values['Zero'][Values['Addrees'].index(Tap)] = Key
                    else:
                        Values['Zero'][Values['Addrees'].index(Tap)] = Num[Values['Addrees'].index(Tap)]['n']
                    Num[Values['Addrees'].index(Tap)]['b'] = Tap

    def SetBar(self, Name):
        Bar = {}

        for Key, Values in self.Tap(Name=Name, Index=True, Count=True).items():
            Revese, Start = None, 0
            for k in set(Values):
                if Revese == None:
                    Revese = True
                    Bar[k] = [x for x in range(Start + 1, Values.count(k) + Start + 1)]
                    Max = max(Bar[k])
                else:
                    Bar[k] = [-x for x in range(Start + 1, Values.count(k) + Start + 1)]
                    Start += min(Bar[k]) - min(Bar[k]) - min(Bar[k]) > Max and min(Bar[k]) - min(Bar[k]) - min(Bar[k]) or Max
                    Revese = None

        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Addrees' in Values:
                if not 'Bar' in Values:
                    Values['Bar'] = {}

                for Tap in Values['Addrees']:
                    if Bar[Tap]:
                        Values['Bar'][Tap] = Bar[Tap][0]
                        Bar[Tap]           = Bar[Tap][1:]

    def DataToMap(self, Name, Data):
        Zero, Map = [], []
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Zero' in Values and 'Data' in Values and Values['Data']:
                if Data in Values['Data']:
                    Zero.append(Values['Zero'])
                    for Key_, Values_ in self.Data['db'][Name]['db'].items():
                        if 'Zero' in Values_:
                            Values_['Map'] = {}
                            for k, v in Values_['Zero'].items():
                                Values_['Map'][k] = Values['Zero'][k] - v

        if self.Data['db'][Name]['AddreesToMap']['BackZero']:
            for Zero_ in Zero:
                for Zero__ in self.Data['db'][Name]['AddreesToMap']['BackZero']:
                    Map.append({})
                    for Key, Values in Zero_.items():
                        Map[-1][Key] = Zero__[Key] - Zero_[Key]

        self.Data['db'][Name]['AddreesToMap']['BackZero'] = Zero

        return {'Map': Map, 'Zero': Zero}

    def AddreesToMap(self, Name, Addrees):
        Zero, Map = [], []
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Zero' in Values and 'Addrees' in Values and Values['Addrees']:
                if not False in [x in Values['Addrees'] for x in Addrees]:
                    Zero.append(Values['Zero'])
                    for Key_, Values_ in self.Data['db'][Name]['db'].items():
                        if 'Zero' in Values_:
                            Values_['Map'] = {}
                            for k, v in Values_['Zero'].items():
                                Values_['Map'][k] = Values['Zero'][k] - v

        if self.Data['db'][Name]['AddreesToMap']['BackZero']:
            for Zero_ in Zero:
                for Zero__ in self.Data['db'][Name]['AddreesToMap']['BackZero']:
                    Map.append({})
                    for Key, Values in Zero_.items():
                        Map[-1][Key] = Zero__[Key] - Zero_[Key]

        self.Data['db'][Name]['AddreesToMap']['BackZero'] = Zero

        return {'Map': Map, 'Zero': Zero}

    def AddreesToBar(self, Name, Addrees):
        Bar = {}
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Bar' in Values and 'Addrees' in Values and Values['Bar'] and Values['Addrees']:
                if not False in [x in Values['Addrees'] for x in Addrees]:
                    for Tap in Addrees:
                        Bar[Tap] = Values['Bar'][Tap]
        return [Bar]
    def DataToBar(self, Name, Data):
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Bar' in Values and 'Data' in Values and Values['Bar'] and Values['Data']:
                if Data in Values['Data'] or Data == None:
                    return [Values['Bar']]

        return []

    def SetDataAndAddrees(self,Name,List,Mode='For',Try=0):
        self.Create(Name=Name)
        Num = 0
        if Mode == 'While':
            while True:
                for Key, Values in self.Data['db'][Name]['db'].items():
                    DataAndAddrees = List[0]
                    List           = List[1:]

                    for v in ['Data','Addrees']:
                        if not v in Values:
                            Values[v] = []

                    Values['Data']        += DataAndAddrees[0]
                    if len(DataAndAddrees) > 1:
                        Values['Addrees'] += DataAndAddrees[1]
                    Num            += 1
                    if not List:
                        break
                if not List:
                    break

        elif Mode == 'For':
            for DataAndAddrees in List:
                for t in range(Try + 1):
                    index = len(self.Data['db'][Name]['db'])
                    self.Data['db'][Name]['db'][index] = {}
                    self.Data['db'][Name]['db'][index]['Data'] = DataAndAddrees[0]
                    if len(DataAndAddrees) > 1:
                        self.Data['db'][Name]['db'][index]['Addrees'] = DataAndAddrees[1]

                    Num                                    += 1
        return Num


    def SetData(self, Name, List, Mode='For',Try=0):
        self.Create(Name=Name)
        Num = 0
        if Mode == 'While':
            while True:
                for Key, Values in self.Data['db'][Name]['db'].items():
                    Data = List[0]
                    List = List[1:]

                    if not 'Data' in Values:
                        Values['Data'] = []

                    Values['Data'] += Data
                    Num            += 1
                    if not List:
                        break
                if not List:
                    break

        elif Mode == 'For':
            for Data in List:
                for t in range(Try + 1):
                    self.Data['db'][Name]['db'][len(self.Data['db'][Name]['db'])]  = {'Data': Data}
                    Num                                                           += 1
        return Num

    def SetAddrees(self, Name, List, Mode='For',Try=0):
        self.Create(Name=Name)
        Num = 0
        if Mode == 'While':
            while True:
                for Key, Values in self.Data['db'][Name]['db'].items():
                    Addrees = List[0]
                    List    = List[1:]

                    if not 'Addrees' in Values:
                        Values['Addrees'] = []

                    Values['Addrees'] += Addrees
                    Num               += 1

                    if not List:
                        break
                if not List:
                    break

        elif Mode == 'For':
            for Addrees in List:
                for t in range(Try + 1):
                    self.Data['db'][Name]['db'][len(self.Data['db'][Name]['db'])] = {'Addrees': Addrees}
                    Num += 1

        self.SetMap(Name=Name)
        self.SetBar(Name=Name)
        return Num

    def ManualSetAddress(self, Name, List=[
        [('st', [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]), ('nd', [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]),
         ('rd', [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34])],
        [('to1', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), ('to2', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),
         ('to3', [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])],
        [('Red', [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]),
         ('Black', [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35])],
        [('Even', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]),
         ('Odd', [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35])],
        [('1-18', range(1, 19)), ('19-36', range(19, 37))]]):
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Data' in Values:
                Addrees = []
                for List_ in List:
                    for n in range(len(List_)):
                        if True in [Data in List_[n][1] for Data in Values['Data']]:
                            Addrees.append(List_[n][0])
                if Addrees:
                    Values['Addrees'] = Addrees

        self.SetBar(Name=Name)
        self.SetMap(Name=Name)

    def UnSetAddrees(self, Name):
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Addrees' in Values:
                del Values['Addrees']

    def UnSetData(self, Name):
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Data' in Values:
                del Values['Data']

    def AddreesToData(self, Name, Addrees,Index=None):
        Data = []
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Data' in Values and 'Addrees' in Values and Values['Data'] and Values['Addrees']:
                if Index:
                    if not False in [Addrees[x] == Values['Addrees'][x] for x in range(len(Addrees))]:
                        Data.append(Values['Data'])
                else:
                    if not False in [x in Values['Addrees'] for x in Addrees]:
                        Data.append(Values['Data'])
        return Data

    def DataToAddrees(self, Name, Data):
        Addrees = []

        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Data' in Values and 'Addrees' in Values and Values['Data'] and Values['Addrees']:
                if Data in Values['Data'] or Data == None:
                    Addrees.append(Values['Addrees'])
        return Addrees

    def Tap(self, Name, Index=None, Count=None):
        Tap, Tmp = {}, []

        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Addrees' in Values:
                for t in range(len(Values['Addrees'])):
                    if not t in Tap:
                        Tap[t] = []
                    if Count:
                        Tap[t].append(Values['Addrees'][t])
                    elif not Values['Addrees'][t] in Tap[t]:
                        Tap[t].append(Values['Addrees'][t])

        if Index:
            return Tap
        else:
            return self.Data['Class']['List'].Start_at(ListOrDict=[t for l in Tap.values() for t in l])

    def ManualSetAddress(self, Name, List=[
        [('st', [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]), ('nd', [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]),('rd', [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34])],
        [('to1', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), ('to2', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),('to3', [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])],
        [('Red', [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]),
         ('Black', [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35])],
        [('Even', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]),
         ('Odd', [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35])],
        [('1-18', range(1, 19)), ('19-36', range(19, 37))]]):
        for Key, Values in self.Data['db'][Name]['db'].items():
            if 'Data' in Values:
                Addrees = []
                for List_ in List:
                    for n in range(len(List_)):
                        if True in [Data in List_[n][1] for Data in Values['Data']]:
                            Addrees.append(List_[n][0])
                if Addrees:
                    Values['Addrees'] = Addrees

        self.SetBar(Name=Name)
        self.SetMap(Name=Name)

    def Show(self,Name):
        return self.Data['db'][Name]['db']
class Space():
    def __init__(self):
        self.Space = {'db': {}}

    def Create(self, Name=0, Start=0, Stop=36, X=4, Y=10, Separate=5, Non=5):
        self.Space['db'][Name] = {'db': {}, 'arg': {'Start': Start, 'Stop': Stop, 'x': X, 'y': Y, 'Separate': Separate,
                                                    'Non': Non}, 'Separate': {'Num': 0}, 'Non': {'Num': 0}}
        Index = 0
        for x in range(X):
            self.Space['db'][Name]['db'][len(self.Space['db'][Name]['db'])] = {'Index': Index,
                                                                               'Data': [random.randint(Start, Stop) for
                                                                                        y in range(Y)], 'Space': [0],
                                                                               'Sleep': [0], 'Non': 0, 'Separate': 0}
            Index += 1

    def Move(self, Name, In, To):
        if Name in self.Space['db']:
            self.Space['db'][Name]['db'][In]['Data'], self.Space['db'][Name]['db'][To]['Data'] = \
            self.Space['db'][Name]['db'][To]['Data'], self.Space['db'][Name]['db'][In]['Data']

    def Separate(self, Name, Num, Index=None):
        if Name in self.Space['db']:
            for Key, Values in self.Space['db'][Name]['db'].items():
                if Index == None or Values['Index'] in Index:
                    Values['Separate'] += 1
                    if Values['Separate'] >= Num:
                        Values['Separate'], Values['Space'] = 0, Values['Space'][-100:] + [0]

    def Non(self, Name, Num, Index=None):
        if Name in self.Space['db']:
            for Key, Values in self.Space['db'][Name]['db'].items():
                if Index == None or Values['Index'] in Index:
                    Values['Non'] += 1
                    if Values['Non'] >= Num:
                        Values['Non'], Values['Data'] = 0, [random.randint(self.Space['db'][Name]['arg']['Start'],
                                                                           self.Space['db'][Name]['arg']['Stop']) for y
                                                            in range(self.Space['db'][Name]['arg']['y'])]

    def Set(self, Name, Data, Index=None):
        if Name in self.Space['db']:
            for Key, Values in self.Space['db'][Name]['db'].items():
                if (Index == None or Values['Index'] in Index):
                    if True in [d in Values['Data'] for d in Data]:
                        Values['Space'][-1] += 1
                        Values['Sleep'] = Values['Sleep'][-100:] + [0]
                    else:
                        Values['Sleep'][-1] += 1

            self.Separate(Name=Name, Num=self.Space['db'][Name]['arg']['Separate'])
            self.Non(Name=Name, Num=self.Space['db'][Name]['arg']['Non'])

    def Show(self, Name):
        if Name in self.Space['db']:
            return self.Space['db'][Name]['db']
        return {}


class Coherence():
    def __init__(self):
        self.Coherence = {'db': {}, 'Class': {'List': List(), 'Addrees': Addrees()}}

    def Name(self):
        return list(self.Coherence['db'].keys())

    def Space_BarToData(self, Name, Space_Bar):
        List = []
        if Name in self.Coherence['db']:
            for Key, Values in self.Coherence['db'][Name]['db'].items():
                for s in Values['Space_Bar']:
                    if s in Space_Bar:
                        List.append(Values['Data'])
        return List

    def Create(self, Name, List, Space_Bar=None):
        self.Coherence['db'][Name] = {'db': {}, 'Set': {'SleepMax': 0, 'History': []}}

        n = 0
        for Data in List:
            if Space_Bar == None:
                Bar = n
            else:
                if Space_Bar:
                    Bar = Space_Bar[0]
                    Space_Bar = Space_Bar[1:]
                else:
                    Bar = None
            self.Coherence['db'][Name]['db'][len(self.Coherence['db'][Name]['db'])] = {'Bar': Bar, 'Index': n,
                                                                                       'Move': 0, 'Static': 0,
                                                                                       'Count': 0, 'Space_Bar': 0,
                                                                                       'Sleep': [0], 'Data': Data,
                                                                                       'ClassData': {}}

            n += 1

    def SetData(self, Name, List,Try=0):
        if Nane in self.Coherence['db']:
            for Key, Values in self.Coherence['db'][Name]['db'].items():
                if List:
                    Values['Data'] = List[0]
                    List = List[1:]
                else:
                    if 'Data' in Values:
                        del Values['Data']

    def Show(self, Name):
        return self.Coherence['db'][Name]['db']

    def AddClassData(self, Name, Class, ClassName):
        for Key, Values in self.Coherence['db'][Name]['db'].items():
            if Values['Data']:
                DataToAddrees = Class.DataToAddrees(Name=ClassName, Data=Values['Data'][0])
                if DataToAddrees:
                    Values['ClassData'][ClassName] = {'Addrees': DataToAddrees,
                                                      'Bar': Class.AddreesToBar(Name=ClassName,
                                                                                Addrees=DataToAddrees[0])}

    def Line(self, Name, ValuesView=['Tap', 'Data', 'Part']):
        Line, Is, Index, Bar = [], [], 0, 0
        if ValuesView:
            for ne in range(self.Coherence['db'][Name]['Set']['SleepMax'] + 1):
                for Key, Values in self.Coherence['db'][Name]['db'].items():
                    if Values['Sleep'][-1] == 0:
                        Values['Static'] = 0
                        Values['Move'] = 0
                        Values['Count'] += 1

                        Bar = Values['Bar']
                        Is += Values['Data']

                    if Values['Sleep'][-1] == ne:
                        if Values['Index'] == Index:
                            Values['Static'] += 1
                        else:
                            Values['Move'] += 1

                        Values['Index'] = Index
                        Index += 1
                        KeyValues = {}
                        for Key in ValuesView:
                            KeyValues[Key] = None
                        for i in ValuesView:
                            if i in Values:
                                KeyValues[i] = Values[i]
                        Line.append(KeyValues)

        Space_Bar_In = {'+': {}, '-': {}}
        for Key, Values in self.Coherence['db'][Name]['db'].items():
            k = Values['Space_Bar'] < 0 and '-' or '+'
            Space_Bar_In[k][Values['Space_Bar']] = Values['Bar']

        return {'Line': Line, 'History': self.Coherence['db'][Name]['Set']['History'], 'Space_Bar_In': Space_Bar_In,
                'Bar': Bar, 'Is': Is}

    def Set(self, Name, Data, ValuesViewLine=['Move', 'Static', 'Data', 'Count', 'ClassData']):
        if Name in self.Coherence['db']:
            Bar, History = [], []

            self.Coherence['db'][Name]['Set']['SleepMax'] = 0
            for Key, Values in self.Coherence['db'][Name]['db'].items():
                index = 0
                for d in Data:
                    if d in Values['Data']:
                        Values['Sleep'] = Values['Sleep'][-100:] + [0]
                        Values['Move'] = 0
                        Values['Static'] = 0
                        Bar.append(Values['Bar'])
                        History.append(Values.copy())
                    else:
                        Values['Sleep'][-1] += 1
                        if Values['Sleep'][-1] > self.Coherence['db'][Name]['Set']['SleepMax']:
                            self.Coherence['db'][Name]['Set']['SleepMax'] = Values['Sleep'][-1]
                    index += 1

            if Bar:
                for Key, Values in self.Coherence['db'][Name]['db'].items():
                    Values['Space_Bar'] = Bar[-1] - Values['Bar']

            self.Coherence['db'][Name]['Set']['History'] = self.Coherence['db'][Name]['Set']['History'][-100:] + History

            return {'History': self.Coherence['db'][Name]['Set']['History'],
                    'Line': self.Line(Name=Name, ValuesView=ValuesViewLine)}


class Director():
    def __init__(self):
        self.Director = {'db': {},
                         'Class': {'Data': Data(), 'Space': Space(), 'Coherence': Coherence(), 'Addrees': Addrees(),
                                   'List': List()}}

    def Name(self, pid=None):
        l = []
        for Key, Values in self.Director['db'].items():
            if pid:
                if 'pid' in Values and Values['pid']:
                    not Values['pid'] in l and l.append(Values['pid'])
            else:
                l.append(Key)
        return l

    def CreateClassData(self,Name,ClassDataShow,ListNumTap):
        self.Director['db'][Name] = {'pid': None, 'P': {'db': {}, 'Max': {}},'Set': {'Class': {'Data': {0:{'Bar': [], 'Map': [], 'Zero': [],'Data':[],'Addrees':[]},1:{'Bar': [], 'Map': [], 'Zero': [],'Data':[],'Addrees':[]}}}},'Line': {'Part': [], 'Data': {'AddreesToZero_y': [], 'ZeroToAddrees_x': [],'ZeroToAddrees_x_Tap': []}, 'Track': {}},'arg': {'ClassData': {'ListNumTap':ListNumTap,'Try':0,'Track':0}, 'ClassCoherence': {},'ClassSpace': {}}}

        self.Director['Class']['Data'].Create(Name=(Name, 0))
        self.Director['Class']['Data'].Create(Name=(Name, 1))
        self.Director['Class']['Data'].Create(Name=(Name, 2))

        self.Director['Class']['Data'].Copy(Name=(Name, 0), ClassDataShow=ClassDataShow)
        DataAndAddrees = self.Director['Class']['Data'].DataAndAddrees(Name=(Name, 0))
        self.Director['Class']['Coherence'].Create(Name=(Name, 0), List=DataAndAddrees['Data'],Space_Bar=list(range(len(DataAndAddrees['Data']))))
        self.Director['Class']['Coherence'].AddClassData(Name=(Name, 0), Class=self.Director['Class']['Data'],ClassName=(Name, 0))

    def Create(self, Name, argClassData, argClassCoherence, argClassSpace, pid=None):
        self.Director['db'][Name] = {'pid': pid, 'P': {'db': {}, 'Max': {}},'Set': {'Class': {'Data': {0:{'Bar': [], 'Map': [], 'Zero': [],'Data':[],'Addrees':[]},1:{'Bar': [], 'Map': [], 'Zero': [],'Data':[],'Addrees':[]}}}},'Line': {'Part': [], 'Data': {'AddreesToZero_y': [], 'ZeroToAddrees_x': [],'ZeroToAddrees_x_Tap': []}, 'Track': {}},'arg': {'ClassData': argClassData, 'ClassCoherence': argClassCoherence,'ClassSpace': argClassSpace}}


        self.Director['db'][Name]['Mode']     = 1
        if not 'Try' in argClassData:
            argClassData['Try'] = 0
            self.Director['db'][Name]['Mode'] = 0
        if not 'Track' in argClassData:
            argClassData['Track'] = 1

        self.Director['Class']['Data'].Create(Name=(Name, 0))
        if argClassData['TypeAddrees'] == 'Auto':
            self.Director['Class']['Data'].SetAddrees(Name=(Name, 0), List=argClassData['Addrees'])
            self.Director['Class']['Data'].SetData(Name=(Name, 0), List=argClassData['Data'], Mode='While')
        elif argClassData['TypeAddrees'] == 'Manual':
            self.Director['Class']['Data'].SetData(Name=(Name, 0), List=argClassData['Data'], Mode='For')
            self.Director['Class']['Data'].ManualSetAddress(Name=(Name, 0), List=argClassData['Addrees'])

        self.Director['Class']['Data'].Create(Name=(Name, 1))
        IndexNum = self.Director['Class']['Data'].SetAddrees(Name=(Name, 1),List=self.Director['Class']['Addrees'].CreateAddrees(ListNumTap=argClassData['ListNumTap']),Mode='For', Try=argClassData['Try'])
        self.Director['Class']['Data'].SetData(Name=(Name, 1), List=[[x] for x in range(IndexNum)], Mode='While')

        self.Director['Class']['Data'].Create(Name=(Name, 2))
        Index, Back = 0, None
        for List in self.Director['Class']['Addrees'].CreateAddrees(ListNumTap=[[argClassData['Track'], list(self.Director['Class']['Data'].DataToAddrees(Name=(Name, 0), Data=None))]], Range=None):
            try:
                self.Director['Class']['Data'].SetDataAndAddrees(Name=(Name, 2), List=[[self.Director['Class']['Data'].AddreesToData(Name=(Name, 1), Addrees=List[0])[Index], List]], Mode='For')
                Index += 1
                if not Back == List[0]:
                    Index = 0
                Back = List[0]
            except:
                Index = 0

        self.Director['Class']['Coherence'].Create(Name=(Name, 0), List=argClassCoherence['Data'],Space_Bar=argClassCoherence['Space_Bar'])
        self.Director['Class']['Coherence'].AddClassData(Name=(Name, 0), Class=self.Director['Class']['Data'],ClassName=(Name, 0))
        self.Director['Class']['Space'].Create(Name=(Name, 0), Start=argClassSpace['Start'], Stop=argClassSpace['Stop'],X=argClassSpace['X'], Y=argClassSpace['Y'],Separate=argClassSpace['Separate'], Non=argClassSpace['Non'])

        Line = self.Line(Name=Name)
        self.Director['db'][Name]['Line']['Part'] = list(self.Director['Class']['List'].IndexLopPart(ListInList=Line['Data']['ZeroToAddrees_x'], Part=3))
        return self.Director['Class']

    def Set(self, Name, Data):
        if 'Set' in self.Director['db'][Name]:
            self.Director['db'][Name]['Set']['Class']['Data'][0]['Zero'] = []
            for D in Data:
                self.Director['db'][Name]['Set']['Class']['Data'][0]['Data'] = self.Director['db'][Name]['Set']['Class']['Data'][0]['Data'][-100:] + [D]
                for Addrees in self.Director['Class']['Data'].DataToAddrees(Name=(Name, 0), Data=D):
                    AddreesToMap = self.Director['Class']['Data'].DataToMap(Name=(Name, 0), Data=D)
                    self.Director['db'][Name]['Set']['Class']['Data'][0]['Addrees'] = self.Director['db'][Name]['Set']['Class']['Data'][0]['Addrees'][-100:] + [Addrees]
                    self.Director['db'][Name]['Set']['Class']['Data'][0]['Bar']     = self.Director['db'][Name]['Set']['Class']['Data'][0]['Bar'][-100:] + self.Director['Class']['Data'].DataToBar(Name=(Name, 0), Data=D)
                    self.Director['db'][Name]['Set']['Class']['Data'][0]['Map']     = self.Director['db'][Name]['Set']['Class']['Data'][0]['Map'][-100:] + AddreesToMap['Map']
                    self.Director['db'][Name]['Set']['Class']['Data'][0]['Zero']   += AddreesToMap['Zero']

                    D1    = self.Director['Class']['Data'].AddreesToData(Name=(Name, 2), Addrees=self.Director['db'][Name]['Set']['Class']['Data'][0]['Addrees'][-self.Director['db'][Name]['arg']['ClassData']['Track']:][::-1], Index=True)
                    if D1:
                        AddreesToMap = self.Director['Class']['Data'].DataToMap(Name=(Name, 1), Data=D1[0][0])
                        self.Director['db'][Name]['Set']['Class']['Data'][1]['Data']    = self.Director['db'][Name]['Set']['Class']['Data'][1]['Data'][-100:]    + D1[0]
                        self.Director['db'][Name]['Set']['Class']['Data'][1]['Addrees'] = self.Director['db'][Name]['Set']['Class']['Data'][1]['Addrees'][-100:] + [Addrees]
                        self.Director['db'][Name]['Set']['Class']['Data'][1]['Bar']     = self.Director['db'][Name]['Set']['Class']['Data'][1]['Bar'][-100:]     + self.Director['Class']['Data'].DataToBar(Name=(Name, 1), Data=D1[0][0])
                        self.Director['db'][Name]['Set']['Class']['Data'][1]['Map']     = self.Director['db'][Name]['Set']['Class']['Data'][1]['Map'][-100:]     + AddreesToMap['Map']
                        self.Director['db'][Name]['Set']['Class']['Data'][1]['Zero']   += AddreesToMap['Zero']

            self.Director['Class']['Space'].Set(Name=(Name, 0), Data=Data)
            self.Director['Class']['Coherence'].Set(Name=(Name, 0), Data=Data)

            SetDistance   = self.SetDistance(Name=Name)
            SetArranging  = self.SetArranging(Name=Name)
            SetSpace      = self.SetSpace(Name=Name)
            SetComparison = self.SetComparison(Name=Name, Addrees={})
            SetEart       = self.SetEart(Name=Name)

            return {'Distance': SetDistance, 'Arranging': SetArranging, 'Space': SetSpace,'SetComparison': SetComparison, 'SetEart': SetEart,'Data':self.Director['db'][Name]['Set']['Class']['Data']}

    def Line(self, Name):
        Line = self.Director['Class']['Coherence'].Line(Name=(Name, 0),ValuesView=['Move', 'Static', 'Count', 'Data', 'Sleep','ClassData'])

        self.Director['db'][Name]['Line']['Line'] = Line
        self.Director['db'][Name]['Line']['Data'] = {}

        self.Director['db'][Name]['Line']['Data']['ZeroToAddrees_x'] = []
        for List in Line['Line']:
            if (Name, 0) in List['ClassData']:
                self.Director['db'][Name]['Line']['Data']['ZeroToAddrees_x'].append(List['ClassData'][(Name, 0)]['Addrees'][0].copy())

        self.Director['db'][Name]['Line']['Data']['ZeroToAddrees_x_Tap'] = [[x[n] for x in self.Director['db'][Name]['Line']['Data']['ZeroToAddrees_x']] for n in range(len(self.Director['db'][Name]['Line']['Data']['ZeroToAddrees_x'][-1]))]

        self.Director['db'][Name]['Line']['Data']['AddreesToZero_y'] = []
        for n in range(len(self.Director['db'][Name]['Line']['Data']['ZeroToAddrees_x'][-1])):
            self.Director['db'][Name]['Line']['Data']['AddreesToZero_y'].append([])
            for List in Line['Line']:
                if (Name, 0) in List['ClassData']:
                    self.Director['db'][Name]['Line']['Data']['AddreesToZero_y'][-1].append(
                        self.Director['Class']['Addrees'].AddreesToZero(Addrees=List['ClassData'][(Name, 0)]['Addrees'][0],ListNumTap=self.Director['db'][Name]['arg']['ClassData']['ListNumTap'])[n])
        return self.Director['db'][Name]['Line']

    def Command(self, Name, Func, Command, arg={}):
        if Func == 'Comparison' and Command == 'Clear':
            self.Director['db'][Name]['Comparison']['db'][arg['Index']]['n'] = 0
            turtle.TNavigator.reset(self.Director['db'][Name]['Comparison']['db'][arg['Index']]['RawTurtle'])
            self.Director['db'][Name]['Comparison']['db'][arg['Index']]['RawTurtle'].pencolor('')
            self.Director['db'][Name]['Comparison']['db'][arg['Index']]['RawTurtle'].clear()
            print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg})

        elif Func == 'Comparison' and Command == 'Color':
            self.SetComparison(Name=Name, Addrees={arg['Index']: arg['Tap']})
            print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg})

        elif Func == 'Space' and Command == 'Set':
            Data = self.Director['db'][Name]['Space']['db'][arg['Mode']]['Entry'].get()
            DataList = []
            for Data in Data.split(' '):
                try:
                    n = int(Data)
                except:
                    pass
                else:
                    DataList.append(n)

            Set = self.Director['Class']['Space'].Set(Name=(Name, 0), Data=DataList)
            self.SetSpace(Name=Name)
            print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg, 'Data': DataList})

            while self.Director['db'][Name]['Space']['db'][arg['Mode']]['Entry'].get():
                self.Director['db'][Name]['Space']['db'][arg['Mode']]['Entry'].delete(0)

        elif Func == 'Distance' and Command == 'Set':
            Data = self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Entry'].get()
            DataList = []
            for Data in Data.split(' '):
                try:
                    n = int(Data)
                except:
                    pass
                else:
                    DataList.append(n)

            Set = self.Set(Name=Name, Data=DataList)
            self.SetDistance(Name=Name)
            print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg, 'Data': DataList})

            while self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Entry'].get():
                self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Entry'].delete(0)

        elif Func == 'Arranging' and Command == 'Set':
            Data = self.Director['db'][Name]['Arranging']['Entry'].get()
            for Data in Data.split(' '):
                try:
                    n = int(Data)
                except:
                    pass
                else:
                    Set = self.Set(Name=Name, Data=[n])
                    self.SetArranging(Name=Name)
                    print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg, 'Data': n})

            while self.Director['db'][Name]['Arranging']['Entry'].get():
                self.Director['db'][Name]['Arranging']['Entry'].delete(0)

        elif Func == 'Comparison' and Command == 'Selected':
            if arg['Tap'] in self.Director['db'][Name]['Comparison']['Selected']:
                self.Director['db'][Name]['Comparison']['Selected'].remove(arg['Tap'])
            else:
                self.Director['db'][Name]['Comparison']['Selected'].append(arg['Tap'])

            while self.Director['db'][Name]['Comparison']['Entry'].get():
                self.Director['db'][Name]['Comparison']['Entry'].delete(0)

            if self.Director['db'][Name]['Comparison']['Selected']:
                for Data in self.Director['Class']['Data'].AddreesToData(Name=(Name, 0), Addrees=
                self.Director['db'][Name]['Comparison']['Selected']):
                    for Data in Data:
                        self.Director['db'][Name]['Comparison']['Entry'].insert(0, str(Data) + ' ')
                        print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg, 'Data': Data})

        elif Func == 'Distance' and Command == 'Selected':
            if arg['Tap'] in self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Selected']:
                self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Selected'].remove(arg['Tap'])
            else:
                self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Selected'].append(arg['Tap'])

            while self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Entry'].get():
                self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Entry'].delete(0)

            if self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Selected']:
                for Data in self.Director['Class']['Data'].AddreesToData(Name=(Name, 0), Addrees=
                self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Selected']):
                    for Data in Data:
                        self.Director['db'][Name]['Distance']['db'][arg['Mode']]['Entry'].insert(0, str(Data) + ' ')
                        print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg, 'Data': Data})

        elif Func == 'Arranging' and Command == 'Selected':
            if arg['Tap'] in self.Director['db'][Name]['Arranging']['Selected']:
                self.Director['db'][Name]['Arranging']['Selected'].remove(arg['Tap'])
            else:
                self.Director['db'][Name]['Arranging']['Selected'].append(arg['Tap'])

            while self.Director['db'][Name]['Arranging']['Entry'].get():
                self.Director['db'][Name]['Arranging']['Entry'].delete(0)

            if self.Director['db'][Name]['Arranging']['Selected']:
                for Data in self.Director['Class']['Data'].AddreesToData(Name=(Name, 0),Addrees=self.Director['db'][Name]['Arranging']['Selected']):
                    for Data in Data:
                        self.Director['db'][Name]['Arranging']['Entry'].insert(0, str(Data) + ' ')
                        print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg, 'Data': Data})

        elif Func == 'Earth' and Command == 'Get':
            while self.Director['db'][Name]['Earth']['Entry'].get():
                self.Director['db'][Name]['Earth']['Entry'].delete(0)

            GetSelectedEarth = self.GetSelectedEarth(Name=Name)['Data']
            self.Director['db'][Name]['Earth']['Entry'].insert(0,
                                                               ' '.join([str(Data) for Data in GetSelectedEarth][::-1]))
            print({'Name': Name, 'Func': Func, 'arg': arg, 'Command': Command, 'Data': GetSelectedEarth})

        elif (Func == 'Earth' or Func == 'Place') and Command == 'Track':
            self.Director['db'][Name][Func]['Selected'] = self.Director['db'][Name][Func]['Earth'].Selected
            self.Director['db'][Name][Func]['Earth'].Selected = {}
            if Func == 'Earth':
                self.SetEart(Name=Name)
            elif Func == 'Place':
                self.SetPlace(Name=Name)
            print({'Name': Name, 'Func': Func, 'arg': arg, 'Command': Command,
                   'Track': self.Director['db'][Name][Func]['Selected']})

        elif Func == 'Earth' and Command == 'Set':
            Data = self.Director['db'][Name]['Earth']['Entry'].get()
            for Data in Data.split(' '):
                try:
                    n = int(Data)
                except:
                    pass
                else:
                    Set = self.Set(Name=Name, Data=[n])
                    self.SetEart(Name=Name)
                    print({'Name': Name, 'Func': Func, 'Command': Command, 'arg': arg, 'Data': n})

            while self.Director['db'][Name]['Earth']['Entry'].get():
                self.Director['db'][Name]['Earth']['Entry'].delete(0)

    def CreateSpace(self, Name, Tkinter=True, Frame=None, Mode='Space', figsize=(60, 4), dpi=80, side=tkinter.LEFT):
        if not 'Space' in self.Director['db'][Name]:
            self.Director['db'][Name]['Space'] = {'db': {}}

        if Tkinter:
            self.Director['db'][Name]['Space']['db'][Mode] = {'Frame': tkinter.Frame(Frame), 'Mode': Mode,
                                                              'Selected': [], 'db': {}, 'Tkinter': Tkinter}
            self.Director['db'][Name]['Space']['db'][Mode]['FrameTools'] = tkinter.Frame(
                self.Director['db'][Name]['Space']['db'][Mode]['Frame'])
            self.Director['db'][Name]['Space']['db'][Mode]['FrameTools'].pack()

            self.Director['db'][Name]['Space']['db'][Mode]['FrameEntry'] = tkinter.Frame(
                self.Director['db'][Name]['Space']['db'][Mode]['FrameTools'])
            self.Director['db'][Name]['Space']['db'][Mode]['FrameEntry'].pack(side=side, anchor=tkinter.N)
            self.Director['db'][Name]['Space']['db'][Mode]['FrameButton'] = tkinter.Frame(
                self.Director['db'][Name]['Space']['db'][Mode]['FrameTools'])
            self.Director['db'][Name]['Space']['db'][Mode]['FrameButton'].pack(side=side, anchor=tkinter.N)

            self.Director['db'][Name]['Space']['db'][Mode]['Entry'] = tkinter.Entry(
                self.Director['db'][Name]['Space']['db'][Mode]['FrameEntry'])
            self.Director['db'][Name]['Space']['db'][Mode]['Entry'].pack()

            tkinter.Button(self.Director['db'][Name]['Space']['db'][Mode]['FrameButton'], text="Set",
                           command=lambda Name=Name, Command='Set', Func='Space', arg={'Mode': Mode}: self.Command(
                               Name=Name, Command=Command, Func=Func, arg=arg)).pack(side=tkinter.LEFT,
                                                                                     anchor=tkinter.N)
        else:
            self.Director['db'][Name]['Space']['db'][Mode] = {'Mode': Mode, 'db': {}, 'Tkinter': Tkinter}

        for Index, Values in self.Director['Class']['Space'].Show(Name=(Name, 0)).items():
            if Tkinter:
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index] = {
                    'Frame': tkinter.LabelFrame(self.Director['db'][Name]['Space']['db'][Mode]['Frame'])}
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['FrameTools'] = tkinter.Frame(
                    self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['Frame'])
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['FrameTools'].pack()

                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['FrameButton'] = tkinter.Frame(
                    self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['FrameTools'])
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['FrameButton'].pack()

                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['figure'] = plt.Figure(figsize=figsize,
                                                                                                   dpi=dpi)
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['add_subplot'] = \
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['figure'].add_subplot(111)
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['FigureCanvasTkAgg'] = FigureCanvasTkAgg(
                    self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['figure'],
                    self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['Frame'])
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['get_tk_widget'] = \
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['FigureCanvasTkAgg'].get_tk_widget().pack(
                    side=tkinter.LEFT, fill=tkinter.BOTH)
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['add_subplot'].set_title('Ops ')
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index]['Frame'].pack()
            else:
                self.Director['db'][Name]['Space']['db'][Mode]['db'][Index] = {}

        return Tkinter and self.Director['db'][Name]['Space']['db'][Mode]['Frame']

    def CreateWiner(self, Name, Tkinter=True, Frame=None):
        if not Name in self.Director['db']:
            self.Director['db'][Name] = {}

        self.Director['db'][Name]['Winer'] = {'db': {},'Tkinter':Tkinter, 'Selected': [], 'Frame': tkinter.Frame(Frame)}
        self.Director['db'][Name]['Winer']['FrameTools'] = tkinter.Frame(self.Director['db'][Name]['Winer']['Frame'])
        self.Director['db'][Name]['Winer']['FrameTools'].pack()

        self.Director['db'][Name]['Winer']['FrameEntry'] = tkinter.Frame(self.Director['db'][Name]['Winer']['FrameTools'])
        self.Director['db'][Name]['Winer']['FrameEntry'].pack(side=tkinter.LEFT, anchor=tkinter.N)
        self.Director['db'][Name]['Winer']['FrameButton'] = tkinter.Frame(self.Director['db'][Name]['Winer']['FrameTools'])
        self.Director['db'][Name]['Winer']['FrameButton'].pack(side=tkinter.LEFT, anchor=tkinter.N)

        nb = tkinter.ttk.Notebook(self.Director['db'][Name]['Winer']['Frame'])
        nb.pack()

        for Name_ in self.Name(pid=True) + ['All']:
            self.Director['db'][Name]['Winer']['db'][Name_] = {'Frame': tkinter.Frame(nb)}
            nb.add(self.Director['db'][Name]['Winer']['db'][Name_]['Frame'], text=Name_)

            Frame = tkinter.LabelFrame(self.Director['db'][Name]['Winer']['db'][Name_]['Frame'])
            Frame.pack(side=tkinter.LEFT, anchor=tkinter.N)

            self.CreateComparison(Name=(Name_, 'win'), Frame=Frame,forward=5, linewidth=4,Num=49, width=100, height=100, Addrees={1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2], 5: [0, 1, 2],6: [0, 1, 2], 7: [0, 1, 2], 8: [0, 1, 2]}, Line=True).pack()

        return self.Director['db'][Name]['Winer']['Frame']

    def CreateComparison(self, Name, Tkinter=True, Frame=None,forward=5, linewidth=4,Num=1000, width=1000, height=100, Addrees={}, side=tkinter.LEFT,Line=None):
        if not Name in self.Director['db']:
            self.Director['db'][Name] = {}

        if Tkinter:
            self.Director['db'][Name]['Comparison'] = {'db': {}, 'Tkinter': Tkinter, 'Selected': [],'Frame': tkinter.Frame(Frame), 'Addrees': Addrees}
            ClassData = None
            if not Addrees:
                ClassData = True
                Addrees = self.Director['Class']['Data'].Tap(Name=(Name, 0), Index=True)

            if ClassData:
                self.Director['db'][Name]['Comparison']['Entry'] = tkinter.Entry(
                    self.Director['db'][Name]['Comparison']['Frame'])
                self.Director['db'][Name]['Comparison']['Entry'].pack()
        else:
            self.Director['db'][Name]['Comparison'] = {'db': {}, 'Tkinter': Tkinter, 'Addrees': Addrees}

        for Index, Tap in Addrees.items():
            if Tkinter:
                if Line:
                    Frame = tkinter.LabelFrame(self.Director['db'][Name]['Comparison']['Frame'])
                    Frame.pack(side=side, anchor=tkinter.N)
                    Frame.configure(text=str(Index))

                    self.Director['db'][Name]['Comparison']['db'][Index] = {'Frame': tkinter.Frame(Frame),'width':linewidth,'forward':forward,'Num':Num, 'n': 0}
                    self.Director['db'][Name]['Comparison']['db'][Index]['Frame'].pack()
                else:
                    self.Director['db'][Name]['Comparison']['db'][Index] = {'Frame': self.Director['db'][Name]['Comparison']['Frame'],'width':linewidth,'forward':forward,'Num':Num, 'n': 0}
                    self.Director['db'][Name]['Comparison']['db'][Index]['Frame'].pack(side=side, anchor=tkinter.N)

                if Line:
                    self.Director['db'][Name]['Comparison']['db'][Index]['Entry'] = tkinter.Entry(
                        self.Director['db'][Name]['Comparison']['db'][Index]['Frame'])
                    self.Director['db'][Name]['Comparison']['db'][Index]['Entry'].pack()

                self.Director['db'][Name]['Comparison']['db'][Index]['Canvas'] = tkinter.Canvas(
                    self.Director['db'][Name]['Comparison']['db'][Index]['Frame'], width=width, height=height)
                self.Director['db'][Name]['Comparison']['db'][Index]['Canvas'].pack()
                self.Director['db'][Name]['Comparison']['db'][Index]['RawTurtle'] = turtle.RawTurtle(
                    self.Director['db'][Name]['Comparison']['db'][Index]['Canvas'])
                self.Director['db'][Name]['Comparison']['db'][Index]['FrameTools'] = tkinter.Frame(
                    self.Director['db'][Name]['Comparison']['db'][Index]['Frame'])
                self.Director['db'][Name]['Comparison']['db'][Index]['FrameTools'].pack()

                self.Director['db'][Name]['Comparison']['db'][Index]['FrameButton'] = tkinter.Frame(
                    self.Director['db'][Name]['Comparison']['db'][Index]['FrameTools'])
                self.Director['db'][Name]['Comparison']['db'][Index]['FrameButton'].pack()
                self.Director['db'][Name]['Comparison']['db'][Index]['Tap'] = Tap

                for Tap in Tap:
                    if ClassData:
                        tkinter.Checkbutton(self.Director['db'][Name]['Comparison']['db'][Index]['FrameButton'],
                                            text=str(Tap), variable=random.random(),
                                            command=lambda Name=Name, Command='Selected', Func='Comparison',
                                                           Tap=Tap: self.Command(Name=Name, Command=Command, Func=Func,
                                                                                 arg={'Tap': Tap})).pack(
                            side=tkinter.LEFT, anchor=tkinter.N)
                    else:
                        tkinter.Button(self.Director['db'][Name]['Comparison']['db'][Index]['FrameButton'],
                                       text=str(Tap), command=lambda Name=Name, Command='Color', Func='Comparison',
                                                                     arg={'Tap': Tap, 'Index': Index}: self.Command(
                                Name=Name, Command=Command, Func=Func, arg=arg)).pack(side=tkinter.LEFT,
                                                                                      anchor=tkinter.N)
                tkinter.Button(self.Director['db'][Name]['Comparison']['db'][Index]['FrameButton'], text='c',
                               command=lambda Name=Name, Command='Clear', Func='Comparison',
                                              arg={'Index': Index}: self.Command(Name=Name, Command=Command, Func=Func,
                                                                                 arg=arg)).pack(side=tkinter.LEFT,
                                                                                                anchor=tkinter.N)
            else:
                self.Director['db'][Name]['Comparison']['db'][Index] = {'n': 0,'Num':Num}

        return Tkinter and self.Director['db'][Name]['Comparison']['Frame']

    def CreateEarth(self, Name, Tkinter=True, Frame=None, width=1500, height=76, side=tkinter.LEFT):
        if Tkinter:
            self.Director['db'][Name]['Earth'] = {'Frame': tkinter.Frame(Frame), 'TrackAddreesList': [], 'Selected': {},
                                                  'Track': {}, 'Tkinter': Tkinter}
            self.Director['db'][Name]['Earth']['FrameTools'] = tkinter.Frame(
                self.Director['db'][Name]['Earth']['Frame'])
            self.Director['db'][Name]['Earth']['FrameTools'].pack(side=side, anchor=tkinter.N)

            self.Director['db'][Name]['Earth']['FrameEntry'] = tkinter.Frame(
                self.Director['db'][Name]['Earth']['FrameTools'])
            self.Director['db'][Name]['Earth']['FrameEntry'].pack()

            self.Director['db'][Name]['Earth']['FrameButton'] = tkinter.Frame(
                self.Director['db'][Name]['Earth']['FrameTools'])
            self.Director['db'][Name]['Earth']['FrameButton'].pack()

            tkinter.Button(self.Director['db'][Name]['Earth']['FrameButton'], text="Track",
                           command=lambda Name=Name, Command='Track', Func='Earth': self.Command(Name=Name,
                                                                                                 Command=Command,
                                                                                                 Func=Func)).pack(
                side=tkinter.LEFT, anchor=tkinter.N)
            tkinter.Button(self.Director['db'][Name]['Earth']['FrameButton'], text="Set",
                           command=lambda Name=Name, Command='Set', Func='Earth': self.Command(Name=Name,
                                                                                               Command=Command,
                                                                                               Func=Func)).pack(
                side=tkinter.LEFT, anchor=tkinter.N)
            tkinter.Button(self.Director['db'][Name]['Earth']['FrameButton'], text="Get",
                           command=lambda Name=Name, Command='Get', Func='Earth': self.Command(Name=Name,
                                                                                               Command=Command,
                                                                                               Func=Func)).pack(
                side=tkinter.LEFT, anchor=tkinter.N)

            self.Director['db'][Name]['Earth']['Entry'] = tkinter.Entry(
                self.Director['db'][Name]['Earth']['FrameEntry'])
            self.Director['db'][Name]['Earth']['Entry'].pack()

            self.Director['db'][Name]['Earth']['Earth'] = Earth(self.Director['db'][Name]['Earth']['Frame'],
                                                                width=width, height=height)
            self.Director['db'][Name]['Earth']['Earth'].pack()
            return self.Director['db'][Name]['Earth']['Frame']
        else:
            self.Director['db'][Name]['Earth'] = {'TrackAddreesList': [], 'Selected': {}, 'Track': {},
                                                  'Tkinter': Tkinter}

    def CreateDistance(self, Name,FrameName=None, Tkinter=True, Frame=None, Mode='Coherence', figsize=(60, 4), dpi=80,
                       side=tkinter.LEFT):
        if not 'Distance' in self.Director['db'][Name]:
            self.Director['db'][Name]['Distance'] = {'db': {}}

        if FrameName == None:
            FrameName = Mode

        if Tkinter:
            self.Director['db'][Name]['Distance']['db'][Mode] = {'Frame': tkinter.Frame(Frame), 'Selected': [],
                                                                 'db': {}, 'Mode': Mode,'FrameName':FrameName , 'Tkinter': Tkinter}
            self.Director['db'][Name]['Distance']['db'][Mode]['FrameTools'] = tkinter.Frame(
                self.Director['db'][Name]['Distance']['db'][Mode]['Frame'])
            self.Director['db'][Name]['Distance']['db'][Mode]['FrameTools'].pack()

            self.Director['db'][Name]['Distance']['db'][Mode]['FrameButton'] = tkinter.Frame(
                self.Director['db'][Name]['Distance']['db'][Mode]['FrameTools'])
            self.Director['db'][Name]['Distance']['db'][Mode]['FrameButton'].pack()

            if Mode in ['Bar', 'Map']:
                for Tap in self.Director['Class']['Data'].Tap(Name=(Name, 0)):
                    tkinter.Checkbutton(self.Director['db'][Name]['Distance']['db'][Mode]['FrameButton'], text=str(Tap),
                                        variable=random.random(),
                                        command=lambda Name=Name, Command='Selected', Func='Distance',
                                                       arg={'Tap': Tap, 'Mode': Mode}: self.Command(Name=Name,
                                                                                                    Command=Command,
                                                                                                    Func=Func,
                                                                                                    arg=arg)).pack(
                        side=tkinter.LEFT, anchor=tkinter.N)

            self.Director['db'][Name]['Distance']['db'][Mode]['Entry'] = tkinter.Entry(
                self.Director['db'][Name]['Distance']['db'][Mode]['FrameButton'])
            self.Director['db'][Name]['Distance']['db'][Mode]['Entry'].pack(side=side, anchor=tkinter.N)
            tkinter.Button(self.Director['db'][Name]['Distance']['db'][Mode]['FrameButton'], text="Set",
                           command=lambda Name=Name, Command='Set', Func='Distance',arg={'Mode':Mode}: self.Command(Name=Name,
                                                                                                  Command=Command,
                                                                                                  Func=Func,arg=arg)).pack(
                side=tkinter.LEFT, anchor=tkinter.N)
        else:
            self.Director['db'][Name]['Distance']['db'][Mode] = {'db': {}, 'Mode': Mode, 'Tkinter': Tkinter}

        a = self.Director['Class']['Data'].DataAndAddrees(Name=(Name, 0))
        for Index in range(Mode in ['Data', 'Coherence', 'Index'] and 1 or len(a['Addrees'][-1])):
            if Tkinter:
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index] = {
                    'Frame': tkinter.LabelFrame(self.Director['db'][Name]['Distance']['db'][Mode]['Frame'], text=FrameName),
                    'Selected': []}
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['FrameTools'] = tkinter.Frame(
                    self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['Frame'])
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['FrameTools'].pack()

                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['FrameButton'] = tkinter.Frame(
                    self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['FrameTools'])
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['FrameButton'].pack()

                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['figure'] = plt.Figure(figsize=figsize,
                                                                                                      dpi=dpi)
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['add_subplot'] = \
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['figure'].add_subplot(111)
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['FigureCanvasTkAgg'] = FigureCanvasTkAgg(
                    self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['figure'],
                    self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['Frame'])
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['get_tk_widget'] = \
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index][
                    'FigureCanvasTkAgg'].get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['add_subplot'].set_title('Ops ')
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index]['Frame'].pack()
            else:
                self.Director['db'][Name]['Distance']['db'][Mode]['db'][Index] = {}

        return Tkinter and self.Director['db'][Name]['Distance']['db'][Mode]['Frame']

    def CreateArranging(self, Name, Tkinter=True, Frame=None, figsize=(60, 4), dpi=80, side=tkinter.LEFT):
        if Tkinter:
            self.Director['db'][Name]['Arranging'] = {'Frame': tkinter.Frame(Frame), 'Selected': [], 'Tkinter': Tkinter}

            self.Director['db'][Name]['Arranging']['FrameTools'] = tkinter.Frame(
                self.Director['db'][Name]['Arranging']['Frame'])
            self.Director['db'][Name]['Arranging']['FrameTools'].pack()

            self.Director['db'][Name]['Arranging']['FrameButton'] = tkinter.Frame(
                self.Director['db'][Name]['Arranging']['FrameTools'])
            self.Director['db'][Name]['Arranging']['FrameButton'].pack()

            for Tap in self.Director['Class']['Data'].Tap(Name=(Name, 0)):
                tkinter.Checkbutton(self.Director['db'][Name]['Arranging']['FrameButton'], text=str(Tap),
                                    variable=random.random(),
                                    command=lambda Name=Name, Command='Selected', Func='Arranging',
                                                   Tap=Tap: self.Command(Name=Name, Command=Command, Func=Func,
                                                                         arg={'Tap': Tap})).pack(side=tkinter.LEFT,
                                                                                                 anchor=tkinter.N)

            self.Director['db'][Name]['Arranging']['Entry'] = tkinter.Entry(
                self.Director['db'][Name]['Arranging']['FrameButton'])
            self.Director['db'][Name]['Arranging']['Entry'].pack(side=side, anchor=tkinter.N)
            tkinter.Button(self.Director['db'][Name]['Arranging']['FrameButton'], text="Set",
                           command=lambda Name=Name, Command='Set', Func='Arranging': self.Command(Name=Name,
                                                                                                   Command=Command,
                                                                                                   Func=Func)).pack(
                side=tkinter.LEFT, anchor=tkinter.N)

            self.Director['db'][Name]['Arranging']['figure'] = plt.Figure(figsize=figsize, dpi=dpi)
            self.Director['db'][Name]['Arranging']['add_subplot'] = self.Director['db'][Name]['Arranging'][
                'figure'].add_subplot(111)
            self.Director['db'][Name]['Arranging']['FigureCanvasTkAgg'] = FigureCanvasTkAgg(
                self.Director['db'][Name]['Arranging']['figure'], self.Director['db'][Name]['Arranging']['Frame'])
            self.Director['db'][Name]['Arranging']['get_tk_widget'] = self.Director['db'][Name]['Arranging'][
                'FigureCanvasTkAgg'].get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
            return self.Director['db'][Name]['Arranging']['Frame']
        else:
            self.Director['db'][Name]['Arranging'] = {'Tkinter': Tkinter}

    def P(self, Name, Line=None):
        if not Line:
            Line = self.Line(Name=Name)

        IfSpees = self.Director['Class']['List'].IfSpees(PartList=self.Director['db'][Name]['Line']['Part'],
                                                         ListInList=Line['Data']['ZeroToAddrees_x'],
                                                         IfSpees=list(range(1, 30)))
        IfSpeesMatch = []

        for Index in range(len(IfSpees['ListTrackAdd'])):
            if not str(IfSpees['ListTrackAdd'][Index]).__hash__() in self.Director['db'][Name]['P']['db']:
                self.Director['db'][Name]['P']['db'][str(IfSpees['ListTrackAdd'][Index]).__hash__()] = {
                    'Log': {'Count': IfSpees['ListTrackAdd'].count(IfSpees['ListTrackAdd'][Index]),
                            'Add': IfSpees['ListTrackAdd'][Index].copy(), 'Len': IfSpees['ListTrackLen'][Index],
                            'Index': IfSpees['ListTrackIndex'][Index]}, 'Center': {}, 'Values': {}, 'Back': {}}

            self.Director['db'][Name]['P']['db'][str(IfSpees['ListTrackAdd'][Index]).__hash__()]['Values']['Add'] = \
            IfSpees['ListTrackAdd'][Index]
            self.Director['db'][Name]['P']['db'][str(IfSpees['ListTrackAdd'][Index]).__hash__()]['Values']['Len'] = \
            IfSpees['ListTrackLen'][Index]
            self.Director['db'][Name]['P']['db'][str(IfSpees['ListTrackAdd'][Index]).__hash__()]['Values']['Count'] = \
            IfSpees['ListTrackAdd'].count(IfSpees['ListTrackAdd'][Index])
            self.Director['db'][Name]['P']['db'][str(IfSpees['ListTrackAdd'][Index]).__hash__()]['Values']['Index'] = \
            IfSpees['ListTrackIndex'][Index]

        for Key, Values in self.Director['db'][Name]['P']['db'].items():
            if not 'Len' in Values['Center']:
                Values['Center']['Len'] = []

            if Values['Back']:
                if Values['Values']['Len'] == Values['Back']['Len']:
                    Values['Center']['Len'] = Values['Center']['Len'] + [0]
                else:
                    Values['Center']['Len'] = Values['Center']['Len'] + [1]

        for Key, Values in self.Director['db'][Name]['P']['db'].copy().items():
            Chk = {'Fixed': (
            len(Values['Center']['Len']), Values['Center']['Len'].count(0), Values['Center']['Len'].count(1)),
                   'Distance difference': len(range(Values['Log']['Index'][0], Values['Values']['Index'][0])),
                   'Shrinking teams': len(range(len(range(Values['Values']['Index'][0], Values['Values']['Index'][1])),
                                                len(range(Values['Log']['Index'][0], Values['Log']['Index'][1]))))}

            if not Values['Values']['Add'] in IfSpees['ListTrackAdd']:
                if not Values['Values']['Count'] in self.Director['db'][Name]['P']['Max']:
                    self.Director['db'][Name]['P']['Max'][Values['Values']['Count']] = {'Distance difference': [],
                                                                                        'Shrinking teams': []}

                self.Director['db'][Name]['P']['Max'][Values['Values']['Count']]['Distance difference'].append(
                    Chk['Distance difference'])
                self.Director['db'][Name]['P']['Max'][Values['Values']['Count']]['Shrinking teams'].append(
                    Chk['Shrinking teams'])
                del self.Director['db'][Name]['P']['db'][Key]
            else:
                if Values['Values']['Len'] > Values['Log']['Len']:
                    self.Director['db'][Name]['P']['db'][Key]['Log'] = Values['Values']
                    self.Director['db'][Name]['P']['db'][Key]['Center']['Len'] = []
                    self.Director['db'][Name]['P']['db'][Key]['Back'] = {}
                else:
                    if Values['Values']['Len'] == Values['Log']['Len']:
                        self.Director['db'][Name]['P']['db'][Key]['Center']['Len'] = []
                    Values['Back'] = Values['Values'].copy()

                if Chk['Shrinking teams'] > int(Values['Log']['Len'] / 2) or Values['Values']['Len'] < 7 and \
                        Values['Values']['Count'] >= 4:
                    IfSpeesMatch.append(Values['Values']['Add'])

        return {'ListTrackAdd': IfSpeesMatch, 'Line': Line}

    def SetWiner(self, Data):
        SetWiner = {'All':{'List': []}}
        for Key, Values in self.Director['db'].items():
            if 'pid' in Values:
                Key = Values['pid']
            else:
                continue

            if not Key in SetWiner:
                SetWiner[Key] = {'List': []}

            for Key_, Values_ in Values.items():
                if type(Values_) == dict:
                    if 'db' in Values_:
                        for Key__, Values__ in Values_['db'].items():
                            if 'Entry' in Values__:
                                for n in ''.join(Values__['Entry'].get()).split(' '):
                                    try:
                                        SetWiner['All']['List'].append(int(n))
                                        SetWiner[Key]['List'].append(int(n))
                                    except:
                                        pass

                    if 'Entry' in Values_:
                        for n in ''.join(Values_['Entry'].get()).split(' '):
                            try:
                                SetWiner['All']['List'].append(int(n))
                                SetWiner[Key]['List'].append(int(n))
                            except:
                                pass

        for Key,Values in SetWiner.items():
            Count = self.Director['Class']['List'].Count(List=Values['List'])
            for n in range(1, 9):
                if (Key, 'win') in self.Director['db']:
                    while self.Director['db'][(Key, 'win')]['Comparison']['db'][n]['Entry'].get():
                        self.Director['db'][(Key, 'win')]['Comparison']['db'][n]['Entry'].delete(0)

                    if Count:
                        if n in Count:
                            [self.Director['db'][(Key, 'win')]['Comparison']['db'][n]['Entry'].insert(0, str(D) + ' ') for D in Count[n]]
                            if True in [D in Count[n] for D in Data]:
                                self.SetComparison(Name=(Key, 'win'), Addrees={n: 1})
                            else:
                                self.SetComparison(Name=(Key, 'win'), Addrees={n: 0})

    def SetDistance(self, Name):
        Distance = {}
        if 'Distance' in self.Director['db'][Name]:
            DataFrame = []
            for Key, Values in self.Director['db'][Name]['Distance']['db'].items():
                for Key_, Values_ in Values['db'].items():
                    if Values['Mode'] in ['Bar','Bar2']:
                        DataFrame = [list(Index.values())[Key_] for Index in self.Director['db'][Name]['Set']['Class']['Data'][Values['Mode'] == 'Bar2' and 1 or Values['Mode'] == 'Bar' and 0]['Bar']]
                    elif Values['Mode'] in ['Map','Map2']:
                        DataFrame = [list(Index.values())[Key_] for Index in self.Director['db'][Name]['Set']['Class']['Data'][Values['Mode'] == 'Map2' and 1 or Values['Mode'] == 'Map' and 0]['Map']]
                    elif Values['Mode'] in ['Data','Data2']  and self.Director['db'][Name]['Set']['Class']['Data'][Values['Mode'] == 'Data' and 1 or Values['Mode'] == 'Data2' and 0]['Map']:
                        DataFrame = [list(Index.values())[-1] for Index in self.Director['db'][Name]['Set']['Class']['Data'][Values['Mode'] == 'Data2' and 1 or Values['Mode'] == 'Data' and 0]['Map']]
                        Values['Tkinter'] and Values_['Frame'].configure(text='Data ' + str([list(x.values())[-1] for x in self.Director['db'][Name]['Set']['Class'][ 'Data'][Values['Mode'] == 'Data2' and 1 or Values['Mode'] == 'Data' and 0]['Zero']]))
                    elif Values['Mode'] == 'Index':
                        DataFrame = [x['Index'] for x in self.Line(Name=Name)['Line']['History']]
                    elif Values['Mode'] == 'Coherence':
                        Line = self.Line(Name=Name)
                        DataFrame = [x['Space_Bar'] for x in Line['Line']['History']]
                        Values['Tkinter'] and Values_['Frame'].configure(text='Coherence ' + str([x['Bar'] for x in Line['Line']['History']][-1]))

                    if DataFrame and Values['Tkinter']:
                        Values_['add_subplot'].clear()
                        PandasDataFrame = pandas.DataFrame(DataFrame)
                        PandasDataFrame.plot(kind='line', ax=Values_['add_subplot'])
                        Values_['FigureCanvasTkAgg'].draw()

                    if not Values['Mode'] in Distance:
                        Distance[Values['Mode']] = {}
                    Distance[Values['Mode']][len(Distance[Values['Mode']])] = DataFrame

        return Distance

    def SetArranging(self, Name):
        if 'Arranging' in self.Director['db'][Name]:
            Line = self.Line(Name=Name)
            TryInTry = self.Director['Class']['List'].TryInTry(ListInList=Line['Data']['ZeroToAddrees_x_Tap'])
            DataFrame = {}
            for Key, Values in self.Director['Class']['List'].PartListInList(ListInList=TryInTry).items():
                if not Key in DataFrame:
                    DataFrame[Key] = {}
                for l in Values:
                    DataFrame[Key][l[0]] = l[2]

            if self.Director['db'][Name]['Arranging']['Tkinter']:
                self.Director['db'][Name]['Arranging']['add_subplot'].clear()
                PandasDataFrame = pandas.DataFrame(list(DataFrame.values()), index=list(DataFrame.keys()),
                                                   columns=self.Director['Class']['Data'].Tap(Name=(Name, 0)))
                PandasDataFrame.plot(kind='bar', legend=True, stacked=True,
                                     ax=self.Director['db'][Name]['Arranging']['add_subplot'])
                self.Director['db'][Name]['Arranging']['FigureCanvasTkAgg'].draw()
            return {'DataFrame': {0: DataFrame}}

    def SetComparison(self, Name, Addrees={}):
        if Name in self.Director['db'] and 'Comparison' in self.Director['db'][Name]:
            if self.Director['db'][Name]['Comparison']['Tkinter']:
                if not Addrees and not self.Director['db'][Name]['Comparison']['Addrees']:
                    Line = self.Line(Name=Name)
                    for List in Line['Line']['Line']:
                        if (Name, 0) in List['ClassData']:
                            for n in range(len(List['ClassData'][(Name, 0)]['Addrees'][0])):
                                Addrees[n] = List['ClassData'][(Name, 0)]['Addrees'][0][n]
                            break

                Colors = ['#0408f1', '#20f303', '#f53603', '#000000', '#deaf27', '#f4ff03', '#03aa8f', '#eb7b4a',
                          '#42efe3',
                          '#bfb9c9', '#5027c1', '#b44340', '#e151ae', '#c78993', '#c0ed1f', '#f37777', '#730f45',
                          '#cb9821',
                          '#d3f5c0', '#cd48a8', '#f701c0', '#5772ad', '#4f9e14', '#589dba', '#34db7e', '#217aff',
                          '#792791',
                          '#d95787', '#7b030e', '#2a3e33', '#52a37c', '#deaf27']

                for Key, Values in self.Director['db'][Name]['Comparison']['db'].items():
                    if Key in Addrees:
                        Values['RawTurtle'].speed(0)
                        Values['RawTurtle'].pencolor(Colors[Values['Tap'].index(Addrees[Key])])
                        Values['RawTurtle'].width(Values['width'])
                        Values['RawTurtle'].forward(Values['n'] + Values['forward'])
                        Values['RawTurtle'].left(60)
                        Values['n'] += 1
                        if Values['Num'] == Values['n']:
                            turtle.TNavigator.reset(Values['RawTurtle'])
                            Values['RawTurtle'].pencolor('')
                            Values['n'] = 0

    def SetEart(self, Name):
        if 'Earth' in self.Director['db'][Name]:
            Line = self.Line(Name=Name)
            if self.Director['db'][Name]['Earth']['Selected']:
                self.Director['db'][Name]['Earth']['Track'] = self.Director['Class']['List'].Track(
                    ListInList=Line['Data']['AddreesToZero_y'],
                    List=self.Director['db'][Name]['Earth']['Selected'].values())
            else:
                P = self.P(Name=Name, Line=Line)
                self.Director['db'][Name]['Earth']['Track'] = self.Director['Class']['List'].Track(
                    ListInList=P['Line']['Data']['AddreesToZero_y'], List=[
                        self.Director['Class']['Addrees'].AddreesToZero(Addrees=Part, ListNumTap=
                        self.Director['db'][Name]['arg']['ClassData']['ListNumTap'], In=True) for Part in
                        P['ListTrackAdd']])

            if self.Director['db'][Name]['Earth']['Tkinter']:
                self.Director['db'][Name]['Earth']['Earth'].Set(ListInList=Line['Data']['AddreesToZero_y'],
                                                                Track=self.Director['db'][Name]['Earth']['Track'])

            return {'List': {0: Line['Data']['AddreesToZero_y']},
                    'Track': {0: self.Director['db'][Name]['Earth']['Track']}}

    def SetSpace(self, Name):
        if 'Space' in self.Director['db'][Name]:
            Space = {}
            for key, Values in self.Director['db'][Name]['Space']['db'].items():
                for Key_, Values_ in self.Director['Class'][
                    Values['Mode'] in ['Space', 'Sleep'] and 'Space' or Values['Mode']].Show(Name=(Name, 0)).items():
                    DataFrame = Values_[Values['Mode']]
                    if Values['Tkinter']:
                        if Values['Mode'] in ['Space', 'Sleep']:
                            if Values['Mode'] == 'Space':
                                Values['db'][Key_]['Frame'].configure(text=str(
                                    {'Mode': Values['Mode'], 'Data': Values_['Data'], 'Separate': Values_['Separate'],
                                     'Non': Values_['Non']}))
                            else:
                                Values['db'][Key_]['Frame'].configure(text=str(
                                    {'Mode': Values['Mode'], 'Data': Values_['Data'], 'Non': Values_['Non'],
                                     'Sleep': DataFrame[-2:]}))

                        Values['db'][Key_]['add_subplot'].clear()
                        PandasDataFrame = pandas.DataFrame(DataFrame)
                        PandasDataFrame.plot(kind='line', ax=Values['db'][Key_]['add_subplot'])
                        Values['db'][Key_]['FigureCanvasTkAgg'].draw()
                    if not Values['Mode'] in Space:
                        Space[Values['Mode']] = {}
                    Space[Values['Mode']][len(Space)] = DataFrame

            return {'DataFrame': Space}

    def GetSelectedEarth(self, Name):
        DataList = []
        AddreesList = []
        for Part in self.Director['db'][Name]['Earth']['Earth'].Selected.values():
            AddreesList.append(list(Part.values()))
            Addrees = []
            for t in range(len(self.Director['db'][Name]['Line']['Data']['ZeroToAddrees_x'][-1])):
                if t in Part:
                    Addrees.append(Part[t])
                else:
                    Addrees.append(None)

            ZeroToAddrees = []
            for Tap in self.Director['Class']['Addrees'].ZeroToAddrees(Addrees=Addrees, ListNumTap=
            self.Director['db'][Name]['arg']['ClassData']['ListNumTap']):
                if type(Tap) == int:
                    ZeroToAddrees.append(Tap)

            self.Director['db'][Name]['Earth']['TrackAddreesList'] = []
            if ZeroToAddrees:
                self.Director['db'][Name]['Earth']['TrackAddreesList'] += ZeroToAddrees
                for Data in self.Director['Class']['Data'].AddreesToData(Name=(Name, 0), Addrees=ZeroToAddrees):
                    DataList += Data
        self.Director['db'][Name]['Earth']['Earth'].Selected = {}
        return {'Data': DataList, 'Addrees': AddreesList}
