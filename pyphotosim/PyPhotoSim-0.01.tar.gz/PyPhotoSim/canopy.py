
import numpy as np
from astropy import units as u
from astropy import constants as c
import copy as cp

from ownClasses.mLeaf import leaf,leafArray
from ownClasses.vapour import vap, vapArray

class Canopy(object):


    def __init__(self, 
                 
                 totalDML=10*u.g,
                 
                 a=0.25,
                 b=0.25,
                 c=0.5,
            
                 F1=0.076,
                 F2=0.303,
                 F3=0.621,
                
                
                 omega=0.2,
                 layers=4,
        
                 SLA=0.02*u.m**2/u.g,
                 Q10=1.5,
                 alpha=0.8,  #leaf absorbtance
                 p=0.04,       #soil albedo
                
                 Tcum=0,
                 RrDM=0.5,
                 RsDM=0.25,
                 RlDM=0.25,
                 RstorageDM=0.0,
        
                 Tbase=10*u.Celsius,
        
                 LAcrit=4*u.m**2,
                 g0= 0.009 * u.mol * u.meter**-2 * u.second**-1,
                 g1= 3.51 *u.kPa**0.5,
                 inAir=vap()
                 ):
        

        self.a=a
        self.b=b
        self.c=c

        self.F1=F1
        self.F2=F2
        self.F3=F3
                
        self.omega=omega  #leaf scattering factor
        self.layers=layers

        self.SLA=SLA.copy()
        self.Q10=Q10
        self.alpha=alpha  #leaf absorbtance
        self.p=p       #soil albedo

        
        self.RrDM=RrDM
        self.RsDM=RsDM
        self.RlDM=RlDM
        self.RstorageDM=RstorageDM

        self.Tbase=Tbase.copy()
        self.LAcrit=LAcrit.copy()

        self.Asl_sum=0
        self.Ash_sum=0
        self.Acum=0
        self.Tcum=0
        
        self.Tsl_sum=0
        self.Tsh_sum=0
       
        self.k15=1*F1+1.82*F2+2.26*F3
        self.k45=0.93*F1+0.68*F2+0.67*F3
        self.k75=0.93*F1+0.68*F2+0.29*F3
        self.g1=g1.copy()
        self.g0=g0.copy()
        self.deathDM=0*u.g
        
      #  self.totalDML=cp.deepcopy(totalDML)
        self.totalDML=totalDML.copy()
        self.rootDM=self.totalDML*self.RrDM
        self.shootDM=self.totalDML*self.RsDM
        
        self.storageDM=self.totalDML*self.RstorageDM
        self.deathLeafDM=0*u.g
        self.leafDM=self.totalDML*self.RlDM
        
        self.totalDM=self.totalDML+self.deathLeafDM
       #print(totalDM)
        self.LA_dead=self.deathLeafDM*self.SLA
        self.LA_live=self.leafDM*self.SLA
        self.LA_total=self.LA_live+0.5*self.LA_dead
        
        self.GDD=0*u.Celsius*u.day
        self.gstage=0
        self.devStages={0:'seedling',1:'tillering',2:'heading',3:'flowering',4:'ripening'}
        self.LeafDeathRate=0
        
        self.dmGainTimestep = 0* u.g
        self.RmTimestep = 0* u.g
        self.AcumTimestep= 0 * u.mol
        self.TcumTimestep= 0 * u.mol
        self.Ash= 0 * u.mol/u.s
        self.Asl= 0 * u.mol/u.s
        self.Tsl= 0 * u.g/u.s
        self.Tsh= 0 * u.g/u.s
        self.shadeRatio=0
        
        self.Oav=np.mean([self.k15,self.k45,self.k75])
        self.inAir=cp.deepcopy(inAir)
        
        self.sunAir=vapArray([])
        [self.sunAir.append(cp.deepcopy(inAir)) for i in range(0,self.layers)]
        for i in self.sunAir:
            i.volume=inAir.volume/self.layers
                
        self.shadeAir=vapArray([])
        [self.shadeAir.append(cp.deepcopy(inAir)) for i in range(0,self.layers)]
        for i in self.shadeAir:
            i.volume=inAir.volume/self.layers
        
        self.sunLeafes=leafArray()
        [self.sunLeafes.append(leaf(g1=g1)) for i in range(0,self.layers)]

        self.shadeLeafes=leafArray()
        [self.shadeLeafes.append(leaf(g1=g1)) for i in range(0,self.layers)]



    def grow(self,inAir,stepsize):

        self.inAir=cp.deepcopy(inAir)
        LAlayer_total=self.LA_total/self.layers
        LAlayer_live=self.LA_live/self.layers


        kbl=self.Oav/(np.sin(np.radians(self.inAir.solarInc)))

        O1=np.max([0.26,0.93*np.sin(np.radians(self.inAir.solarInc))])
        O2=np.max([0.47,0.68*np.sin(np.radians(self.inAir.solarInc))])
        O3=1 - 0.268* O1 - 0.732*O2
        O=self.F1*O1+self.F2*O2+self.F3*O3

        tDMtemp=self.totalDML


        self.LAslTot=0
        self.LAshTot=0

        for i in range(self.layers):

            LALayerCum=(i+1)*(self.LA_total.value/self.layers)
            Idr=self.inAir.Qdr*np.exp(-kbl*np.sqrt((1-self.omega))*LALayerCum) #(Anten 2b)
            Idrdr=self.inAir.Qdr*np.exp(-kbl*LALayerCum)   #(Anten 2c)
            Idrdf=Idr-Idrdr #(Anten 2d)

            Adif=(1-self.p)*self.inAir.Qdf*(  self.a*(1-np.exp(np.sqrt(1-self.omega)*-self.k15*LALayerCum)) + self.b*(1-np.exp(np.sqrt(1-self.omega)*-self.k45*LALayerCum)) + self.c*(1-np.exp(np.sqrt(1-self.omega)*-self.k75*LALayerCum)))
            Idif=self.inAir.Qdf-Adif
            Kdf=-np.log( Idif/self.inAir.Qdf ) / LALayerCum #(Anten 6)

            self.shadeAir[i].PAR=(Kdf/np.sqrt((1-self.omega)))*(Idif+Idrdf)  #(Anten 8)
            self.sunAir[i].PAR=self.shadeAir[i].PAR+(O*self.inAir.Qdr)/np.sin(np.radians(self.inAir.solarInc)) #(Anten 9)
            
            self.sunLeafes[i].Area=np.exp(-kbl*LALayerCum)*LAlayer_live #(Anten 10)
            self.shadeLeafes[i].Area=LAlayer_live-self.sunLeafes[i].Area
            
            self.sunLeafes[i].step(self.sunAir[i])
            self.shadeLeafes[i].step(self.shadeAir[i])

        self.LAslTot=sum(self.sunLeafes['Area'])
        self.LAshTot=sum(self.shadeLeafes['Area'])

                
        self.Asl=(sum(self.sunLeafes['cAtot'])).cgs
        self.Ash=(sum(self.shadeLeafes['cAtot'])).cgs
        self.Tsl=(sum(self.sunLeafes['EmassTot'])).cgs
        self.Tsh=(sum(self.shadeLeafes['EmassTot'])).cgs
        self.TslMole=(sum(self.sunLeafes['EmolTot'])).cgs
        self.TshMole=(sum(self.shadeLeafes['EmolTot'])).cgs            
        
        self.Atot=(self.Asl+self.Ash)
        self.Ttot=(self.Tsl+self.Tsh)
        self.TtotMole=(self.TslMole+self.TshMole)
        
        self.PostTransInAir=cp.deepcopy(inAir)
        self.PostTransInAir.transpire(self.Ttot*u.s)
        self.PostTransInAir.assim(self.Atot*u.s)
        
        self.AcumTimestep=self.Atot*stepsize
        self.TcumTimestep=self.Ttot*stepsize
        self.TcumMoleTimestep=self.TtotMole*stepsize
        self.AcumTimestepMass=(self.AcumTimestep*(44.01 *u.g/u.mol)).cgs
        self.shadeRatio=self.LAshTot/self.LA_live

#########growth
        
        self.dmGainTimestep=self.AcumTimestepMass*(30/44)
        self.RmTimestep=(self.rootDM*0.015+self.shootDM*0.015+self.leafDM*0.03+self.storageDM*0.01)*((stepsize/(24*u.h)).cgs)
        self.RmTimestep = self.RmTimestep * self.Q10**(((inAir.temp.value) - 25.0) / 10.0)
        self.dmGainTimestep=self.dmGainTimestep-self.RmTimestep

        self.dmGainTimestep=self.dmGainTimestep-u.g*(self.dmGainTimestep/(self.dmGainTimestep*self.RrDM*1.444+self.dmGainTimestep*self.RsDM*1.513+self.dmGainTimestep*self.RlDM*1.463+self.dmGainTimestep*self.RstorageDM*1.415))*((stepsize/(24*u.h)).cgs)
        self.totalDML+=self.dmGainTimestep
        self.rootDM+=self.dmGainTimestep*0.5
        self.shootDM+=self.dmGainTimestep*0.25
        self.storageDM+=self.dmGainTimestep*0.0


        if self.dmGainTimestep>0:
            self.leafDM+=self.dmGainTimestep*0.25
            self.LA_live+=(self.dmGainTimestep*0.25*self.SLA)
            self.LA_total+=(self.dmGainTimestep*0.25*self.SLA)
        else:
            self.rootDM+=self.dmGainTimestep*0.25
            self.deathDM+=abs(self.dmGainTimestep)


        self.totalDM=self.totalDML+self.deathDM        
        self.growthRate=((self.totalDML-tDMtemp)/stepsize).to(u.g/u.day)
        self.RelgrowthRate=(self.totalDML-tDMtemp)/self.totalDML

########develop
        self.GDD=((self.GDD+inAir.temp*stepsize) if (inAir.temp-10*u.Celsius) > 0 else 0*u.Celsius*u.day).to(u.Celsius*u.day)
        self.gstage+=1 if ((self.GDD.value%600==0) & (self.GDD.value<2500)) else 0

        if self.gstage<=2:
            self.LeafDeathRateAge=0.0

        elif (self.gstage>2) & (self.gstage<=3):
            self.LeafDeathRateAge=(self.growthRate.value)/(4-self.gstage)
        else:
            self.LeafDeathRateAge=self.gstage/0.04+self.growthRate.value/0.6

        self.LeafDeathRateAge=self.LeafDeathRateAge/1500

        if self.LA_total<=self.LAcrit:
            self.LeafDeathRateShade=0.0
        else:
            self.LeafDeathRateShade=min(0.015,0.015*((self.LA_total.value-self.LAcrit.value)/self.LAcrit.value))

        self.LeafDeathRate=max(self.LeafDeathRateShade,self.LeafDeathRateAge)

            
        LAloss=self.LA_live*self.LeafDeathRate
        DMleafLoss=LAloss/self.SLA
        
        self.LA_dead+=LAloss
        self.LA_live-=LAloss
        self.LA_total=self.LA_live+self.LA_dead*0.5
        
        
        self.deathLeafDM+=DMleafLoss
        self.leafDM-=DMleafLoss
        self.deathDM+=DMleafLoss
        self.totalDM+=DMleafLoss
        self.totalDML-=DMleafLoss


    def Arrhenius(self, k25, Ea, Tk, deltaS=None, Hd=None):
        
        if ( (deltaS is not None) & (Hd is not None) ):
            arg1 = k25 * np.exp((Ea * (Tk.to('Kelvin', equivalencies=u.temperature() ) - 298.15*u.Kelvin)) / (298.15*u.Kelvin * c.R * Tk.to('Kelvin', equivalencies=u.temperature() )))
            arg2 = 1.0 + np.exp( (298.15*u.Kelvin * deltaS - Hd)  / (298.15 * u.Kelvin * c.R) )
            arg3 = 1.0 + np.exp((Tk.to('Kelvin', equivalencies=u.temperature() ) * deltaS - Hd)  / (Tk.to('Kelvin', equivalencies=u.temperature() ) * c.R))
            return (arg1 * arg2) / arg3
        else:
            return k25 * np.exp((Ea * (Tk.to('Kelvin', equivalencies=u.temperature() ) - 298.15*u.Kelvin)) / (298.15*u.Kelvin * c.R * Tk.to('Kelvin', equivalencies=u.temperature() )))




class canArray:
    
    def __init__(self,a=0.25,
                 b=0.25,
                 c=0.5,
            
                 F1=0.076,
                 F2=0.303,
                 F3=0.621,
                
                
                 omega=0.2,
                 layers=4,
        
                 SLA=0.02*u.m**2/u.g,
                 Q10=2,
                 alpha=0.8,  #leaf absorbtance
                 p=0.04,       #soil albedo
        
                 totalDML=10.0*u.g,
                
        
                 Tcum=0,
                 RrDM=0.5,
                 RsDM=0.25,
                 RlDM=0.25,
                 RstorageDM=0.0,
        
                 Tbase=10*u.Celsius,
        
                 LAcrit=4*u.m**2):

        self.__members=[]

    def __setitem__(self,param,values):
        if len(values)!=len(self.__members):
            raise IndexError('length of values does not match number of members')
        for i in range(0,len(self.__members)):
            setattr(self.__members[i],param,values[i])

    def __getitem__(self, param):
        
        if isinstance(param,str):
            try:
                return np.array([getattr(i,param).value for i in self.__members]).squeeze()*getattr(self.__members[0],param).unit
            except AttributeError:
                return np.array([getattr(i,param) for i in self.__members]).squeeze()
        elif isinstance(param,int):
            return self.__members[param]
        elif isinstance(param,slice):
            lst=[]
            for i in range(param.start,param.stop+1):
                lst.append(self.__members[i])
            return lst
            
            
    def __len__(self):
        return len(self.__members)
        
    def append(self,canopy):
        if isinstance(canopy,Canopy)!= True:
            raise AttributeError('can only append objects of type Canopy')
        self.__members.append(canopy)






#%%

if __name__ == '__main__':
    from ownClasses.vapour import vap,vapArray
    import pandas as pd
    from plotnine import *
    import timeit
    from timeit import default_timer as timer

    start = timer()*u.s

    air=vap(temp=25*u.Celsius,rH=0.1,solarInc=90,par=1000*u.umol/u.m**2/u.s)
    air.VPD=2*u.kPa
    air.Qdf=0.8

    
    a=Canopy(layers=3,inAir=air, totalDML = 10*u.g)
    rs=canArray()
    #rs.append(cp.deepcopy(a))

    for i in range(1,4):
        a.grow(air,1*u.day)
        rs.append(cp.deepcopy(a))
        print(i)

    end = timer()*u.s
    print(end - start)
    
    
#%%
    i=range(len(rs))
    dt=pd.DataFrame(zip(i,rs['totalDM'].value,rs['totalDML'].value,rs['deathDM'].value,rs['deathLeafDM'].value,rs['leafDM'].value,rs['dmGainTimestep'].value,rs['RmTimestep'].value,rs['LA_total'].value,rs['LA_live'].value,rs['LA_dead'].value,rs['AcumTimestep'].value,rs['TcumTimestep'].value,rs['Ash'].value,rs['Asl'].value,rs['shadeRatio'].value),
                    columns=['i','totalDM','totalDML','deathDM','deathLeafDM','leafDM','dmGainTimestep','RmTimestep','LA_total','LA_live','LA_dead','AcumTimestep','TcumTimestep','Ash','Asl','shadeRatio'])
    

    from plotnine import *    
    for i in dt.columns[1:]:
       p=ggplot(dt,aes(x='i',y=i))
       p+=geom_point()
       p.draw()


#%%



    

