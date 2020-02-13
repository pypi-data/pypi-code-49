from Attack_cion.Attack_cion import Data,List,Addrees,Director
import random,tkinter

def TestingRoulette(Mode, Frame=None, Roulette=None):
    arg = {'argClassData': {'Data': Class['List'].Part(List=random.sample(list(range(37)), 37), Part=1),'Try':50,'Track':3,'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(4, 2)])),'TypeAddrees': 'Auto', 'ListNumTap': [(4, 2)]},'argClassCoherence': {'Data': Class['List'].Part(List=list(range(37)), Part=1),'Space_Bar': list(range(0,37))},'argClassSpace': {'Start': 0, 'Stop': 36, 'X': 6, 'Y': 4, 'Separate': 3, 'Non': 11}}
    RandomName = str(Mode) + str(random.random())

    ButtonFrame = tkinter.Frame(Frame)
    ButtonFrame.pack()

    for i in range(2):
        tkinter.Button(ButtonFrame, text=str(i == 0 and 'King' or 'writing'),
                       command=lambda Data=i: Command(Data=[Data])).pack(side=tkinter.LEFT, anchor=tkinter.N)

    FrameButton = tkinter.Frame(Frame)
    FrameButton.pack()

    FrameDirector = tkinter.Frame(Frame)
    FrameDirector.pack()

    def Command(Data):
        for Data in Data:
            try:
                n = int(Data)
            except:
                pass
            else:
                for Name in Class['Director'].Name():
                    Set = Class['Director'].Set(Name=Name, Data=[n])

    if Mode == 'Cion':
        arg = {'argClassData': {'Data': Class['List'].Part(List=random.sample(list(range(9)), 9), Part=1), 'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(3, 2)])),'TypeAddrees': 'Auto', 'ListNumTap': [(3, 2)]},'argClassCoherence': {'Data': Class['List'].Part(List=list(range(100)), Part=1),'Space_Bar': list(range(0, 100))},'argClassSpace': {'Start': 0, 'Stop': 36, 'X': 6, 'Y': 4, 'Separate': 3, 'Non': 11}}
        Class['Director'].Create(Name=RandomName + 'Cion1', argClassData={'Data': Class['List'].Part(List=random.sample(list(range(2)), 2), Part=1),'Addrees': list(Class['Addrees'].CreateAddrees(ListNumTap=[(1, 2)])),'Try':100,'Track':10,'TypeAddrees': 'Auto', 'ListNumTap': [(1, 2)]},argClassCoherence={'Data': Class['List'].Part(List=list(range(2)), Part=1),'Space_Bar': list(range(0, 2))}, argClassSpace={'Start': 0, 'Stop': 5, 'X': 6, 'Y': 1, 'Separate': 3, 'Non': 11},pid=Mode)
        Class['Director'].CreateDistance(Name=RandomName + 'Cion1',FrameName='Cion', Mode='Bar2', Frame=FrameDirector, figsize=(20, 4), dpi=30).pack()
    elif Mode == 'Winer':
        Class['Director'].CreateWiner(Name=RandomName, Frame=FrameDirector).pack()

Class = {'Director': Director(), 'Data': Data(), 'Addrees': Addrees(), 'List': List()}

def mainloop():
    Frame = tkinter.Tk()
    Frame.title('What\'s "P=NP? | Roulette Slots"')
    nb = tkinter.ttk.Notebook(Frame)
    nb.pack()

    FrameList = {}
    for Mode in  ['Cion']:
        FrameList[Mode] = tkinter.Frame(nb)
        nb.add(FrameList[Mode], text=Mode)
        TestingRoulette(Mode=Mode, Frame=FrameList[Mode], Roulette=Mode in ['Roulette_Wheel_Red_BlackTennis_player_theory', 'Roulette_Wheel_rd_nd_stTennis_player_theory','Roulette_Wheel_Random_Tennis_player_theory','Roulette_Wheel_Red_Black','Roulette_Wheel_rd_nd_st','Winer'])

    tkinter.mainloop()

