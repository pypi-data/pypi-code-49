# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""


#from pint import UnitRegistry
#u = UnitRegistry()
from astropy import units as u
from astropy import constants as c

from copy import deepcopy
import numpy as np
import pandas as pd

from sympy.solvers import solve
from sympy import Symbol

from timeit import default_timer as timer
from ownClasses.vapour import vap,vapArray


class leaf:
    
    def __init__(self,Vcmax25=121 * u.umol * u.meter**-2 * u.second**-1,
                 Jmax25=150* u.umol * u.meter**-2 * u.second**-1,
                 gamStar25=40.302 *u.umol/u.mol,
                 Km=911*u.umol/u.mol,
                 Rd25=1 * u.umol * u.meter**-2 * u.second**-1,
                 g0= 0.009 * u.mol * u.meter**-2 * u.second**-1,
                 g1= 1.51 *u.kPa**0.5,
                 theta=0.75,
                 k2ll=0.225,
                 gm= 0.3 * u.mol * u.meter**-2 * u.second**-1
                 outAir=vap()
                 ):

        self.Eag=37830*u.J/u.mol	#Activation energy at CO2 compensation point [J mol-1]
        self.Q10=1.5 #ratio of respiration at a given temperature divided by respiration at a temperature 10 degrees lower
        self.Eaj=30000*u.J/u.mol	#activation energy for the parameter [J mol-1]
        self.Eav=60000*u.J/u.mol	#activation energy for the parameter [J mol-1]
        self.deltaSj=650	*u.J/(u.mol*u.Kelvin)	#entropy factor [J mol-1 K-1)
        self.deltaSv=650*u.J/(u.mol*u.Kelvin)	#entropy factor [J mol-1 K-1)
        self.Hdv=200000*u.J/u.mol	 #Deactivation energy for Vcmax [J mol-1]
        self.Hdj=200000*u.J/u.mol #Deactivation energy for Jmax [J mol-1]
        self.outAir=outAir

        self.alphaG=0.0040516/u.s
        self.r0=0.002674* u.mol * u.meter**-2 * u.second**-1
        self.gbW=2.7* u.mol * u.meter**-2 * u.second**-1
        self.gsW=0.2* u.mol * u.meter**-2 * u.second**-1
        self.gsC=0.0125* u.mol * u.meter**-2 * u.second**-1
        self.gbH=self.gbW/1.15
        self.cC=400*u.umol/u.mol
        self.cA= self.cAj=self.cAc = 0 * u.umol * u.meter**-2 * u.second**-1
        self.g0= g0.to(u.mol * u.meter**-2 * u.second**-1).copy()
        self.g1= g1.to(u.kPa**0.5).copy()

        #self.gscb=0.14 * u.umol / u.mol

        self.gmgm.copy()
        self.Km=Km.copy()

        self.k2ll=k2ll#0.225
        self.Theta=theta#.75

        self.Vcmax25=Vcmax25.copy()
        self.Jmax25=Jmax25.copy()
        self.gamStar25=gamStar25.copy()
        self.Rd25=Rd25.copy()

        self.gamStar = self.gamStar25.copy()
        self.Rd = self.Rd25.copy()
        self.Vcmax = self.Vcmax25.copy()
        self.Jmax = self.Jmax25.copy()
        
        self.Area=1*u.m**2/10000
    
    def calcA_G(self,outAir):

        self.outAir=outAir
        self.J=(self.k2ll*self.outAir.PAR+self.Jmax-np.sqrt((self.k2ll*self.outAir.PAR+self.Jmax)**2-4*self.Theta*self.k2ll*self.outAir.PAR*self.Jmax))/(2*self.Theta)

        self.gscb=((1+(self.g1/np.sqrt(self.outAir.VPD)))*(1/self.outAir.Cs))
        self.p2 = self.outAir.Cs + self.Km
        self.p1 = self.outAir.Cs- self.gamStar
        self.g0m = self.g0 + self.gm
        self.k1  = self.outAir.Cs - self.gamStar
        self.k2  = self.outAir.Cs + 2*self.gamStar
        
        c3=self.gscb
        c2=self.g0m-self.gscb*self.Vcmax-self.gscb*self.gm*self.p2
        c1=self.gm*self.p1*self.Vcmax*self.gscb-self.g0m*self.Vcmax-self.g0*self.gm*self.p2
        c0=self.g0*self.gm*self.p1*self.Vcmax


        
        b3 = 4*self.gscb
        b2 = 4*self.g0m - self.J*self.gscb - 4*self.k2*self.gm*self.gscb
        b1 = self.k1*self.gm*self.J*self.gscb - 4*self.k2*self.gm*self.g0 - self.J*self.g0m
        b0 = self.k1*self.gm*self.J*self.g0


        try:
            A=Symbol('A')
            rc=solve(c3.value*np.power(A,3) + c2.value*np.power(A,2) + c1.value*A + c0.value ,A,cubics=False)
            rc=[np.float(i) for i in rc]
            rc=a.tAc if len(rc)==0 else rc
        except:
            rc=self.tAc
        
        try:
            A=Symbol('A')
            rj=solve(b3.value*np.power(A,3) + b2.value*np.power(A,2) + b1.value*A + b0.value ,A,cubics=False)
            rj=[np.float(i) for i in rj]
            rj=a.tAj if len(rj)==0 else rj
        except:
            rj=self.tAj

        rc=np.array(rc)
        self.tAc=min(rc[rc>0]) * u.umol/u.m**2/u.s

        rj=np.array(rj)
        self.tAj=min(rj[rj>0]) * u.umol/u.m**2/u.s
        
        self.tA=min([self.tAc,self.tAj])
        
        
        self.tAtot=self.tA*self.Area
        self.G=self.g0+1.16*(1+(self.g1/np.sqrt(self.outAir.VPD)))*(self.tA/self.outAir.Cs)
                    
        # gsW(t): Stomatal conductance to water vapor
        # gsc(t): Stomatal conductance to CO2
        # gtW(t): Total conductance to water vapor transport
        # gbW Boundary layer Conductance to water transport
        # gbH Conductance to sensible heat transport
        
        #factor to convert from mmol m-2 s-1:
        molTomm=(c.R*self.outAir.tempK)/self.outAir.Pressure
        
       
        gsW=self.gsW.value
        alphaG=self.alphaG.value    
        G=self.G.value
        r0=self.r0.value       
        delta_gsW=1
        
        while np.abs(delta_gsW*1000)>0.05:
            delta_gsW=(alphaG * np.log( (1.6*G-r0) /  (gsW-r0) ) * (gsW-r0))
            gsW=(gsW+delta_gsW*1)

                
        self.delta_gsW=delta_gsW*1000*(u.mmol/u.m**2/u.s**2)
        self.gsW=gsW*1000*(u.mmol/u.m**2/u.s)
        
        #for i in range(100):
        #    self.delta_gsW=(self.alphaG * np.log( (1.6*self.G-self.r0) /  (self.gsW-self.r0) ) * (self.gsW-self.r0)).to(u.mmol/u.m**2/u.s**2)
        #    self.gsW=self.gsW+self.delta_gsW*timestepSize
        
        self.gtW=(self.gbW*self.gsW)/(self.gbW+self.gsW)
        self.gtc=self.gtW*1.6
       

        self.deltaT=(((1/(self.gbH*molTomm) )*(1/ (self.gtW*molTomm) )*self.outAir.psyConst*self.outAir.shortwave)-((1/(self.gbH*molTomm) )*self.outAir.densOfAir*self.outAir.specHeatofAir*self.outAir.VPD))/(self.outAir.densOfAir*self.outAir.specHeatofAir*(self.outAir.psyConst*(1/(self.gtW*molTomm) )+self.outAir.slopeOfSatPress*(1/(self.gbH*molTomm))))
        self.tLeaf=self.outAir.temp+ (self.deltaT.value * u.Celsius)


        self.gamStar =self.Arrhenius(self.gamStar25, self.Eag, self.tLeaf)
        self.Rd = self.Rd25 * self.Q10**(((self.tLeaf.value) - 25.0) / 10.0)
        self.Vcmax = self.Arrhenius(self.Vcmax25, self.Eav, self.tLeaf, self.deltaSv, self.Hdv)
        self.Jmax = self.Arrhenius(self.Jmax25, self.Eaj, self.tLeaf, self.deltaSj, self.Hdj)


        self.E1=(1/(1/self.gtW))
        self.E2=( (self.outAir.molar_mass_humid_air*self.outAir.specHeatofAir* (self.outAir.VPD+self.outAir.slopeOfSatPress*self.deltaT) ) ) 
        self.Eu=( (self.outAir.latHeatVapWater * self.outAir.psyConst) )

        self.Emass=((self.E1*(self.E2/self.Eu)).to(u.g/(u.m**2*u.s))) 
        self.EmassTot=self.Emass*self.Area


        self.Emol=(self.Emass/ (18.01528 * u.g/u.mol )).to(u.mmol/u.m**2/u.s)
        self.EmolTot=self.Emol*self.Area

        #self.Ccc=self.outAir.Cs-self.cAc*(self.gtc+self.gm)/(self.gtc*self.gm)
        #self.Ccj=self.outAir.Cs-self.cAj*(self.gtc+self.gm)/(self.gtc*self.gm)

        #self.cAc=self.Vcmax*(self.Ccc-self.gamStar) / (self.Ccc+self.Km)
        #self.cAj=(self.J*(self.Ccj-self.gamStar))/(4*self.Ccj+8*self.gamStar)
        
        self.cC=self.outAir.Cs-self.cA*(self.gtc+self.gm)/(self.gtc*self.gm)

        self.cAc=self.Vcmax*(self.cC-self.gamStar) / (self.cC+self.Km)
        self.cAj=(self.J*(self.cC-self.gamStar))/(4*self.cC+8*self.gamStar)


        distZeroC=np.abs(0-self.cAc)
        distZeroJ=np.abs(0-self.cAj)
        
        self.cA=(self.cAj if distZeroC>distZeroJ else self.cAc)# - self.Rd
        self.cAtot=self.cA*self.Area

    def step(self,outAir):

        self.calcA_G(outAir)

    def Arrhenius(self, k25, Ea, Tk, deltaS=None, Hd=None):
        
        if ( (deltaS is not None) & (Hd is not None) ):
            arg1 = k25 * np.exp((Ea * (Tk.to('Kelvin', equivalencies=u.temperature() ) - 298.15*u.Kelvin)) / (298.15*u.Kelvin * c.R * Tk.to('Kelvin', equivalencies=u.temperature() )))
            arg2 = 1.0 + np.exp( (298.15*u.Kelvin * deltaS - Hd)  / (298.15 * u.Kelvin * c.R) )
            arg3 = 1.0 + np.exp((Tk.to('Kelvin', equivalencies=u.temperature() ) * deltaS - Hd)  / (Tk.to('Kelvin', equivalencies=u.temperature() ) * c.R))
            return (arg1 * arg2) / arg3
        else:
            return k25 * np.exp((Ea * (Tk.to('Kelvin', equivalencies=u.temperature() ) - 298.15*u.Kelvin)) / (298.15*u.Kelvin * c.R * Tk.to('Kelvin', equivalencies=u.temperature() )))


class leafArray:
    
    def __init__(self):

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
        
    def append(self,Leaf):
        if isinstance(Leaf,leaf)!= True:
            raise AttributeError('can only append objects of type leaf')
        self.__members.append(Leaf)
#%%

from plotnine import *

if __name__ == '__main__':
    from ownClasses.vapour import vap
    from copy import deepcopy
    np.seterr(all='raise')
    air=vap(temp=28*u.Celsius,rH=0.5,solarInc=90,par=100*u.umol/u.m**2/u.s,cs=900 *u.umol/u.mol)
    a=leaf(outAir=air,g0=0.008*u.mol/u.m**2/u.s,g1= 3.8 *u.kPa**0.5,k2ll=0.334,theta=0.2,Jmax25=350* u.umol * u.meter**-2 * u.second**-1)
    lr=leafArray()
    for i in range(0,20):
        a.step(air)
        lr.append(deepcopy(a))
        air.PAR+=100*u.umol/u.m**2/u.s
        #air.Cs+=20 *u.umol/u.mol
        #air.temp+=2 *u.Celsius


#%%
    
    i=range(len(lr))
    par=[i.PAR.value for i in lr['outAir']]
    temp=[i.temp.value for i in lr['outAir']]
    Cs=[i.Cs.value for i in lr['outAir']]
    rH=[i.rH for i in lr['outAir']]
    dt=pd.DataFrame(zip(i,par,rH,temp,Cs,lr['gtW'].value,lr['cC'].value,lr['cA'].value,lr['cAj'].value,lr['cAc'].value,lr['Rd'].value,lr['tLeaf'].value,lr['Emass'].value,lr['Emol'].value),
                    columns=['i','PAR','rH','temp','Cs','gtW','Cc','cA','cAj','cAc','Rd','tLeaf','Emass','Emol'])
    
    
    p=ggplot(dt)
    p+=geom_line(aes(x='PAR',y='cAj'))
    p+=geom_line(aes(x='PAR',y='cAc'),color='red')
    
    p.draw()

    