from CionAttack.CionAttack import Data,List,Addrees,Director
import random,tkinter

def TestingRoulette(Mode, Frame=None, Roulette=None):
    arg = {'argClassData': {'Data': Class['List'].Part(List=random.sample(list(range(37)), 37), Part=1),'Try':50,'Track':3,'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(4, 2)])),'TypeAddrees': 'Auto', 'ListNumTap': [(4, 2)]},'argClassCoherence': {'Data': Class['List'].Part(List=list(range(37)), Part=1),'Space_Bar': list(range(0,37))},'argClassSpace': {'Start': 0, 'Stop': 36, 'X': 6, 'Y': 4, 'Separate': 3, 'Non': 11}}
    RandomName = str(Mode) + str(random.random())
    print(RandomName)
    def Command(Command):
        if Command == 'ButtonSet':
            Data = EntrySet.get()
            for Data in Data.split(' '):
                try:
                    n = int(Data)
                except:
                    pass
                else:
                    for Name in Class['Director'].Name():
                        Set = Class['Director'].Set(Name=Name, Data=[n])

                    Class['Director'].SetWiner(Data=[n])


            while EntrySet.get():
                EntrySet.delete(0)

    FrameButton = tkinter.Frame(Frame)
    FrameButton.pack()

    EntrySet = tkinter.Entry(FrameButton)
    EntrySet.grid(column=0, row=0)

    ButtonSet = tkinter.Button(FrameButton, text="Set", command=lambda command='ButtonSet': Command(Command=command))
    ButtonSet.grid(column=1, row=0)

    FrameDirector = tkinter.Frame(Frame)
    FrameDirector.pack()

    if Mode == 'Space':
        Class['Director'].Create(Name=RandomName, argClassData=arg['argClassData'],argClassCoherence=arg['argClassCoherence'], argClassSpace=arg['argClassSpace'])
        [Class['Director'].Set(Name=RandomName, Data=[random.randint(0, 36)]) for i in range(100)]
        Class['Director'].CreateSpace(Name=RandomName, Mode='Space', Frame=FrameDirector, figsize=(60, 4), dpi=20).pack()

    elif Mode == 'Sleep':
        Class['Director'].Create(Name=RandomName, argClassData=arg['argClassData'],argClassCoherence=arg['argClassCoherence'], argClassSpace=arg['argClassSpace'])
        [Class['Director'].Set(Name=RandomName, Data=[random.randint(0, 36)]) for i in range(100)]
        Class['Director'].CreateSpace(Name=RandomName, Mode='Sleep', Frame=FrameDirector, figsize=(60, 4), dpi=20).pack()

    elif Mode == 'Earth':
        for Name in range(10):
            arg = {'argClassData': {'Data': Class['List'].Part(List=random.sample(list(range(37)), 37), Part=1),'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(3, 2)])),'Try':1,'Track':1,'TypeAddrees': 'Auto', 'ListNumTap': [(3, 2)]},'argClassCoherence': {'Data': Class['List'].Part(List=list(range(37)), Part=1),'Space_Bar': list(range(1, 38))},'argClassSpace': {'Start': 0, 'Stop': 36, 'X': 6, 'Y': 4, 'Separate': 3, 'Non': 11}}
            Class['Director'].Create(Name=RandomName + str(Name), argClassData=arg['argClassData'],argClassCoherence=arg['argClassCoherence'], argClassSpace=arg['argClassSpace'],pid=Mode)
            Class['Director'].CreateEarth(Name=RandomName + str(Name), Frame=FrameDirector, width=1500, height=76).pack()


    elif Mode in ['Roulette_Wheel_Red_Black', 'Roulette_Wheel_rd_nd_st','Roulette_Wheel_Random']:
        if Mode == 'Roulette_Wheel_Red_Black':
            arg['argClassData'] = {'Data': Class['List'].Part(List=random.sample(list(range(37)), 37), Part=1),'Addrees': [[(0, [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]),(1, [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35])],[(2, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]),(3, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35])],[(4, list(range(1, 19))), (5, list(range(19, 37)))]],'Try':3,'Track':2,'TypeAddrees': 'Manual', 'ListNumTap': [(3, 2)]}
        elif Mode == 'Roulette_Wheel_rd_nd_st':
            arg['argClassData'] = {'Data': Class['List'].Part(List=random.sample(list(range(37)), 37), Part=1),'Addrees': [ [(0, [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]), (1, [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]),(2, [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34])], [(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), (4, [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]),(5, [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])]],'Try':3,'Track':2,'TypeAddrees': 'Manual', 'ListNumTap': [(2, 3)]}

        Create  = Class['Director'].Create(Name=RandomName, argClassData=arg['argClassData'],argClassCoherence=arg['argClassCoherence'], argClassSpace=arg['argClassSpace'],pid=Mode)
        Class['Director'].CreateEarth(Name=RandomName, Frame=FrameDirector, width=1500, height=76).pack()
        Class['Director'].CreateDistance(Name=RandomName, Mode='Bar2', Frame=FrameDirector, figsize=(60, 4), dpi=20).pack()
        Class['Director'].CreateDistance(Name=RandomName, Mode='Index', Frame=FrameDirector, figsize=(60, 4), dpi=20).pack()

    elif Mode == 'Root':
        arg = {'argClassData': {'Data': Class['List'].Part(List=random.sample(list(range(9)), 9), Part=1), 'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(3, 2)])),'TypeAddrees': 'Auto', 'ListNumTap': [(3, 2)]},'argClassCoherence': {'Data': Class['List'].Part(List=list(range(100)), Part=1),'Space_Bar': list(range(0, 100))},'argClassSpace': {'Start': 0, 'Stop': 36, 'X': 6, 'Y': 4, 'Separate': 3, 'Non': 11}}

        arg['argClassSpace']['X'] = 1
        Class['Director'].Create(Name=RandomName, argClassData=arg['argClassData'], argClassCoherence=arg['argClassCoherence'], argClassSpace=arg['argClassSpace'],pid=Mode)
        [Class['Director'].Set(Name=RandomName, Data=[random.randint(0, 36)]) for i in range(100)]

        Class['Director'].CreateComparison(Name=RandomName, Frame=FrameDirector,forward=5, linewidth=4,Num=49, width=100, height=100,side=tkinter.RIGHT).pack()
        Class['Director'].CreateEarth(Name=RandomName, Frame=FrameDirector, width=1500, height=76).pack()

        Class['Director'].CreateComparison(Name=RandomName + 'Root_1', Frame=FrameDirector,forward=5, linewidth=4,Num=49, width=100, height=100,Addrees={0: [0, 1], 1: [0, 1], 2: [0, 1], 3: [0, 1]}).pack()

        Class['Director'].Create(Name=RandomName + 'Cion1', argClassData={'Data': Class['List'].Part(List=random.sample(list(range(2)), 2), Part=1),'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(1, 2)])),'Try':100,'Track':10,'TypeAddrees': 'Auto', 'ListNumTap': [(1, 2)]},argClassCoherence={'Data': Class['List'].Part(List=list(range(2)), Part=1),'Space_Bar': list(range(0, 2))}, argClassSpace={'Start': 0, 'Stop': 5, 'X': 6, 'Y': 1, 'Separate': 3, 'Non': 11},pid=Mode)
        Class['Director'].CreateDistance(Name=RandomName + 'Cion1', Mode='Bar2', Frame=FrameDirector, figsize=(60, 4), dpi=20).pack()
        Class['Director'].Create(Name=RandomName + 'Cion2', argClassData={'Data': Class['List'].Part(List=random.sample(list(range(2)), 2), Part=1),'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(1, 2)])),'Try':100,'Track':10,'TypeAddrees': 'Auto', 'ListNumTap': [(1, 2)]},argClassCoherence={'Data': Class['List'].Part(List=list(range(2)), Part=1),'Space_Bar': list(range(0, 2))}, argClassSpace={'Start': 0, 'Stop': 5, 'X': 6, 'Y': 1, 'Separate': 3, 'Non': 11},pid=Mode)
        Class['Director'].CreateDistance(Name=RandomName + 'Cion2', Mode='Bar2', Frame=FrameDirector, figsize=(60, 4), dpi=20).pack()
        Class['Director'].Create(Name=RandomName + 'Cion3', argClassData={'Data': Class['List'].Part(List=random.sample(list(range(2)), 2), Part=1),'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(1, 2)])),'Try':100,'Track':10,'TypeAddrees': 'Auto', 'ListNumTap': [(1, 2)]},argClassCoherence={'Data': Class['List'].Part(List=list(range(2)), Part=1),'Space_Bar': list(range(0, 2))}, argClassSpace={'Start': 0, 'Stop': 5, 'X': 6, 'Y': 1, 'Separate': 3, 'Non': 11},pid=Mode)
        Class['Director'].CreateDistance(Name=RandomName + 'Cion3', Mode='Bar2', Frame=FrameDirector, figsize=(60, 4), dpi=20).pack()

        Class['Director'].Create(Name=RandomName + 'Coherence', argClassData=arg['argClassData'], argClassCoherence=arg['argClassCoherence'], argClassSpace=arg['argClassSpace'],pid=Mode)
        Class['Director'].CreateDistance(Name=RandomName + 'Coherence', Mode='Coherence', Frame=FrameDirector, figsize=(60, 4), dpi=20).pack()

    elif Mode == 'Comparison':
        for Name in range(10):
            arg = {'argClassData': {'Data': Class['List'].Part(List=random.sample(list(range(37)), 37), Part=1),
                                    'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(3, 2)])),
                                    'TypeAddrees': 'Auto', 'ListNumTap': [(3, 2)]},
                   'argClassCoherence': {'Data': Class['List'].Part(List=list(range(37)), Part=1),
                                         'Space_Bar': list(range(1, 38))},
                   'argClassSpace': {'Start': 0, 'Stop': 36, 'X': 6, 'Y': 4, 'Separate': 3, 'Non': 5}}
            Class['Director'].Create(Name=RandomName + str(Name), argClassData=arg['argClassData'],argClassCoherence=arg['argClassCoherence'], argClassSpace=arg['argClassSpace'], pid='Comparison')
            Class['Director'].CreateComparison(Name=RandomName + str(Name), Frame=FrameDirector,forward=5, linewidth=4,Num=49, width=100, height=100, side=tkinter.RIGHT).pack()
    elif Mode == 'User_Comparison':
        Class['Director'].CreateComparison(Name=RandomName, Frame=FrameDirector,forward=5, linewidth=4,Num=600, width=600, height=600,Addrees={0: [0,1,2,3,4,5,6,7,8,9,10]})

    elif Mode == 'Winer':
        Class['Director'].CreateWiner(Name=RandomName, Frame=FrameDirector).pack()


Class = {'Director': Director(), 'Data': Data(), 'Addrees': Addrees(), 'List': List()}

def mainloop():
    Frame = tkinter.Tk()
    Frame.title('What\'s "P=NP? | Roulette Slots"')
    nb = tkinter.ttk.Notebook(Frame)
    nb.pack()

    FrameList = {}
    for Mode in  ['Root','Roulette_Wheel_Red_Black','Roulette_Wheel_rd_nd_st','Space', 'Sleep','Winer']:
        FrameList[Mode] = tkinter.Frame(nb)
        nb.add(FrameList[Mode], text=Mode)
        TestingRoulette(Mode=Mode, Frame=FrameList[Mode], Roulette=Mode in ['Roulette_Wheel_Red_BlackTennis_player_theory', 'Roulette_Wheel_rd_nd_stTennis_player_theory','Roulette_Wheel_Random_Tennis_player_theory','Roulette_Wheel_Red_Black','Roulette_Wheel_rd_nd_st','Winer'])

    tkinter.mainloop()

