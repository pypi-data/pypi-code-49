from Attack_cion.Attack_cion import Data,List,Addrees
import random

Class = {'Addrees':Addrees(),'List':List(),'Data':Data()}

Class['Data'].SetAddrees(Name=0, List=list(Class['Addrees'].CreateAddrees(ListNumTap=[(6, 2)])))
Class['Data'].SetData(Name=0, List=Class['List'].Part(List=random.sample(list(range(37)), 37), Part=1), Mode='While')
for Key,Values in Class['Data'].Show(Name=0).items():
    print(Key,Values)

randint = random.randint(0,36)
print('randint',randint)

DataToAddrees = Class['Data'].DataToAddrees(Name=0,Data=randint)
for DataToAddrees in DataToAddrees:
    AddreesToData = Class['Data'].AddreesToData(Name=0,Addrees=DataToAddrees)
    AddreesToZero = Class['Addrees'].AddreesToZero(Addrees=DataToAddrees, ListNumTap=[(6, 2)])
    ZeroToAddrees = Class['Addrees'].ZeroToAddrees(Addrees=AddreesToZero, ListNumTap=[(6, 2)])
    print('AddreesToData',AddreesToData)
    print('DataToAddrees',DataToAddrees)
    print('AddreesToZero',AddreesToZero)
    print('ZeroToAddrees',ZeroToAddrees)
