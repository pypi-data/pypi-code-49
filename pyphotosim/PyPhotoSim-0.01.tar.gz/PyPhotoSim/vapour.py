# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:24:17 2016

@author: knoerk
"""




from astropy import units as u
from astropy import constants as c
from copy import deepcopy
import numpy as np
from astropy.visualization import quantity_support
quantity_support()
          
    
class vap:
    r_one=287.058 * u.J/(u.kg*u.K)
    r_two=461.523 * u.J/(u.kg*u.K)
    #molecular diffusity for heat:
    diff_heat=21.5E-6 *u.m**2 / u.s
    specHeatofAir = 1006 * (u.joule / (u.kg * u.K))
    
    def __init__(self, temp=25*u.Celsius, rH=0.5, Pressure=101325 * u.Pascal, par=1000 * u.umol*u.m**-2*u.s**-1,cs = 300 * u.umol/u.mol, ws= 2 * u.m/u.s,  sw2par=2.114, volume=1*u.m**3,solarInc=40):
        #sw2par defaults to values of Britton and Dodd (1976)        
        self.__volume=volume
        self.__temp=temp
        
        ##check supplied units:
        #TODO: complete this
        if (hasattr(temp,'unit')):
            if temp.unit!=u.Celsius:
                raise AttributeError( ('wrong unit for temp ({}) supplied, expected {}').format(temp.unit,u.Celsius) )
        else:
            raise AttributeError( ('unitless supplied for {}, expected {}').format('temp',u.Celsius) )
            
        
        
        
        if rH>1:
            self.__rH=rH/(10**len(str(round(rH))))
            print( ('given rH is {0} and thus greater 100%. Settig rH to {1}').format(rH,self.__rH))
        else:
            self.__rH=rH
        
        self.__Pressure=Pressure.copy()
        self.__PAR=par.copy()
        self.__ws=ws.copy()
        self.__Cs=cs.copy()
        self.__sw2par=sw2par
        self.__shortwave = par * (1/self.__sw2par * (u.J * u.umol**-1) )
        self.__calcVPandSo(self.__temp, self.__rH, self.__Pressure)
        self.__calcMasses__()
        self.__Qdf=0.5*par.copy()
        self.__Qdr=0.5*par.copy()
        self.__solarInc=solarInc
        self.__outflow=0*u.m**3

    def __add__(self, other):
        if isinstance(other,vap)!= True:
            raise AttributeError('can only add objects of type vap')
        
        tempSelf=deepcopy(self)
        
        tempSelf.volume=tempSelf.volume+other.volume
        tempSelf.__massAir=tempSelf.massAir+other.massAir
        tempSelf.temp=( (self.temp.to('Kelvin', equivalencies=u.temperature())*self.massAir+other.temp.to('Kelvin', equivalencies=u.temperature())*other.massAir)/tempSelf.massAir ).to('Celsius', equivalencies=u.temperature() )
        tempSelf.aH=(self.aH*self.volume+other.aH*other.volume)/tempSelf.volume
        tempSelf.Cs=(self.Cs*self.volume+other.Cs*other.volume)/tempSelf.volume
        tempSelf.__calcMasses__()
        return tempSelf
        

    def __sub__(self, volume):
        if volume.unit.physical_type!='volume':
            raise AttributeError('can only substract volumes')
        tempSelf=deepcopy(self)
        tempSelf.volume=tempSelf.volume-volume
        tempSelf.__calcMasses__()
        return tempSelf
    
    def __truediv__(self, divisor):
        if (isinstance(divisor,float)!= True) and (isinstance(divisor,int)!= True):
            raise AttributeError('can only div by int or float')
        
        tempSelf=deepcopy(self)
        
        tempSelf.volume=tempSelf.volume/divisor
        tempSelf.__massAir=tempSelf.massAir/divisor
        tempSelf.__calcMasses__()
        return tempSelf
    
    def __mul__(self, multi):
        if (isinstance(multi,float)!= True) and (isinstance(multi,int)!= True):
            raise AttributeError('can only multiply with int or float')
        
        tempSelf=deepcopy(self)
        
        tempSelf.volume=tempSelf.volume*multi
        tempSelf.__massAir=tempSelf.massAir*multi
        tempSelf.__calcMasses__()
        return tempSelf


###Properties of volume independant paramters
    def __setTemp(self,temp):
        SVP=((6.1094*np.exp((17.625*(temp.value))/(243.04+(temp.value))))*(1.00071*np.exp(0.0000045*(self.__Pressure.to("hPa").value))))* u.hectopascal
        rH=self.__VP / SVP
        self.__calcVPandSo(temp, rH, self.__Pressure)
    def __getTemp(self):    
        return self.__temp
    temp=property(__getTemp,__setTemp)

    def __getOutflow(self):    
        return self.__outflow
    outflow=property(__getOutflow)

    def __setQdf(self,QdfRatio):
        if QdfRatio<=1:
            self.__Qdf=self.__PAR*QdfRatio
            self.__Qdr=(1-QdfRatio)*self.__PAR
        else:
           raise ArithmeticError('Qdf must be >=1')
    def __getQdf(self):
        return self.__Qdf
    Qdf=property(__getQdf,__setQdf)

    def __setQdr(self,QdrRatio):
        if QdrRatio<=1:
            self.__Qdr=self.__PAR*QdrRatio
            self.__Qdf=(1-QdrRatio)*self.__PAR
        else:
           raise ArithmeticError('Qdr must be >=1')
    def __getQdr(self):
        return self.__Qdr
    Qdr=property(__getQdr,__setQdr)


    def __setsolarInc(self,solarInc):
        if solarInc<=90:
            self.__solarInc=solarInc
        else:
           raise ArithmeticError('solarInc must be >=90')
    def __getsolarInc(self):
        return self.__solarInc
    solarInc=property(__getsolarInc,__setsolarInc)

    
    def __setTempK(self,temp):
        raise NotImplementedError
    def __getTempK(self):    
        return self.__temp.to('Kelvin', equivalencies=u.temperature())
    tempK=property(__getTempK,__setTempK)
    
    
    
    def __setrH(self,rH):
        self.__calcVPandSo(self.__temp, rH, self.__Pressure)
    def __getrH(self):    
        return self.__rH
    rH=property(__getrH,__setrH)   

    def __getPAR(self):
        return self.__PAR
    def __setPAR(self,par):
        self.__PAR=par
        self.__shortwave = par * (1/self.__sw2par * (u.J * u.umol**-1) )
    PAR=property(__getPAR,__setPAR)
    
    def __getPressure(self):
        return self.__Pressure
    def __setPressure(self,Pressure):
        self.__calcVPandSo(self.__temp, self.__rH, Pressure)
    Pressure=property(__getPressure,__setPressure)
    
    def __getSVP(self):
        return self.__SVP
    def __setSVP(self,svp):
        self.__temp=(-(12152000000*np.log((11253448*svp.to(u.hPa).value)/68800629)-54684*self.__Pressure.to(u.hPa).value)/(50000000*np.log((11253448*svp.to(u.hPa).value)/68800629)-225*self.__Pressure.to(u.hPa).value-881250000)) *u.Celsius
        self.__calcVPandSo(self.__temp, self.__rH, self.__Pressure)
    SVP=property(__getSVP,__setSVP)
    
    def __getVPD(self):
        return self.__VPD
    def __setVPD(self,vpd):
        if vpd>self.__SVP:
            raise ArithmeticError('VPD larger than SVP')
        else:
            self.__rH=-( (vpd-self.__SVP)/ self.__SVP)
            self.__calcVPandSo(self.__temp, self.__rH, self.__Pressure)
    VPD=property(__getVPD,__setVPD)
    
    def __getVP(self):
        return self.__VP
    def __setVP(self,vp):
        pass
    VP=property(__getVP,__setVP)
    
    
    def __getCs(self):
        return self.__Cs
    def __setCs(self,cs):
        self.__Cs=cs
        self.__mfco2=((((self.__Pressure*self.__Cs) /(c.R*self.__temp.to('Kelvin', equivalencies=u.temperature())))*44.00964*(u.g/u.mol))) / (self.__densOfAir)
    Cs=property(__getCs,__setCs)
    
    def __getmfco2(self):
        return self.__mfco2#.to(u.g/u.kg)
    def __setmfco2(self,__mfco2):
        raise NotImplementedError#self.__mfco2=((((self.__Pressure*self.__Cs) /(c.R*self.__temp.to('Kelvin', equivalencies=u.temperature())))*44.00964*(u.g/u.mol))) / (self.__densOfAir)
    mfco2=property(__getmfco2,__setmfco2)
    

    def __getShortwave(self):
        return self.__shortwave
    shortwave=property(__getShortwave)
    
    def __getmolar_mass_humid_air(self):
        return self.__molar_mass_humid_air
    molar_mass_humid_air=property(__getmolar_mass_humid_air)

    def __getws(self):
        return self.__ws
    def __setws(self,ws):
        pass
    ws=property(__getws,__setws)

    def __getslopeOfSatPress(self):
        return self.__slopeOfSatPress
    slopeOfSatPress=property(__getslopeOfSatPress)

    def __getdensOfAir (self):
        return self.__densOfAir
    densOfAir=property(__getdensOfAir)
    
    def __getpsyConst(self):
        return self.__psyConst
    def __setpsyConst(self,PsyConst):
        pass
    psyConst=property(__getpsyConst,__setpsyConst)    
    
    def __getlatHeatVapWater(self):
        return self.__latHeatVapWater
    def __setlatHeatVapWater(self,LatHeatVapWater):
        pass
    latHeatVapWater=property(__getlatHeatVapWater,__setlatHeatVapWater)

    def __getemissivity_atmo(self):
        return self.__emissivity_atmo
    def __setemissivity_atmo(self,Emissivity_atmo):
        pass
    emissivity_atmo=property(__getemissivity_atmo,__setemissivity_atmo)
      
    def __getmH(self):
        return self.__mH
    def __setmH(self,mh):
        rH=(self.__Pressure*mh)/self.__SVP
        self.__calcVPandSo(self.temp, rH, self.__Pressure)
    mH=property(__getmH,__setmH) 
    
    def __getsH(self):
        return self.__sH
    def __setsH(self,sh):
        self.__VP=(362055*self.__Pressure*sh)/(136864*sh+225191)
        rH=self.__VP.to(u.Pa).value/self.__SVP.to(u.Pa).value
        self.__calcVPandSo(self.temp, rH, self.__Pressure)
    sH=property(__getsH,__setsH)

    def __getaH(self):
        return self.__aH
    def __setaH(self,ah):
        rH=((self.r_two*self.__temp.to('Kelvin', equivalencies=u.temperature())*ah)/self.__SVP).to(u.g/u.g).value
        self.__calcVPandSo(self.temp, rH, self.__Pressure)
    aH=property(__getaH,__setaH)     
    
    
    ###Properteis of volume related parameters
    def __getVolume(self):
        return self.__volume
    def __setVolume(self,Volume):
        self.__volume=Volume
    volume=property(__getVolume,__setVolume)
            
    def __getMassAir(self):
        return self.__massAir
    def __setMassAir(self,massAir):
        raise NotImplementedError
    massAir=property(__getMassAir,__setMassAir)
    
    def __getMassH2O(self):
        return self.__massH2O
    def __setMassH2O(self,massH2O):
        raise NotImplementedError
    massH2O=property(__getMassH2O,__setMassH2O)
    
    def __getMassCO2(self):
        return self.__massCO2
    def __setMassCO2(self,massCO2):
        raise NotImplementedError
    massCO2=property(__getMassCO2,__setMassCO2)
    
    def __getMolAir(self):
        return self.__molAir
    def __setMolAir(self,MolAir):
        raise NotImplementedError
    molAir=property(__getMolAir,__setMolAir)
    
    def __getMolH2O(self):
        return self.__massH2O
    def __setMolH2O(self,molH2O):
        raise NotImplementedError
    molH2O=property(__getMolH2O,__setMolH2O)
    
    def __getMolCO2(self):
        return self.__molCO2
    def __setMolCO2(self,molCO2):
        raise NotImplementedError
    molCO2=property(__getMolCO2,__setMolCO2)
    
    
    
    def __calcVPandSo(self, temp, rH, Pressure):
        self.__temp=temp
        self.__rH=rH if rH <= 1 else 0.999
        self.__Pressure=Pressure        
        
        self.__SVP=((6.1094*np.exp((17.625*(self.__temp.value))/(243.04+(self.__temp.value))))*(1.00071*np.exp(0.0000045*(self.__Pressure.to("hPa").value))))* u.hectopascal
        self.__VP=self.__SVP*self.__rH
        self.__VPD=self.__SVP-self.__VP
        self.__rf=self.r_one/( 1.0-self.__rH*self.__SVP/self.Pressure*(1.0-self.r_one/self.r_two) ) #Die Gaskonstante der feuchten Luft 
        self.__densOfAir = (self.__Pressure)/ ( self.__rf *  self.__temp.to('Kelvin', equivalencies=u.temperature())  )
        self.__latHeatVapWater = ((50.09 - 0.9298 * (self.__temp.to('Kelvin', equivalencies=u.temperature()).value / 1000) - 65.19 * (self.__temp.to('Kelvin', equivalencies=u.temperature()).value / 1000) ** 2) * u.kJ / u.mol) / (18.0153 * u.g / u.mol)
        
        # 13 from Moualeu-Ngangua 2016
        self.__slopeOfSatPress=((17.502*(240*u.Celsius).to('Kelvin', equivalencies=u.temperature())*self.__VPD)/( (240*u.Celsius).to('Kelvin', equivalencies=u.temperature())+self.__temp.to('Kelvin', equivalencies=u.temperature()) )**2).to(u.hPa/u.Kelvin)

        self.__psyConst = (self.specHeatofAir * self.__Pressure) / ((self.__latHeatVapWater) * 0.622)
        self.__E_ = self.__slopeOfSatPress / self.__psyConst
        self.__aH=(self.__VP/(self.r_two*self.__temp.to('Kelvin', equivalencies=u.temperature()))).to(u.g/u.m**3)
        self.__sH=( ( (18.01528/28.9644)*self.__VP ) / (self.__Pressure-(1-18.01528/28.9644)*self.__VP) ).to(u.g/u.kg)
        self.__mH=self.__VP/self.__Pressure

        #emissivity of atmosphere (D4 from leining (1995):	
        self.__emissivity_atmo = 0.642 * (self.__VP.to(u.Pa).value / self.__temp.to('Kelvin', equivalencies=u.temperature()).value)**(1.0 / 7.0)
        self.__molar_mass_humid_air=self.__densOfAir*((c.R*self.__temp.to('Kelvin', equivalencies=u.temperature()))/self.__Pressure)
        self.__mfco2=((((self.__Pressure*self.__Cs) /(c.R*self.__temp.to('Kelvin', equivalencies=u.temperature())))*44.00964*(u.g/u.mol))) / (self.__densOfAir)
        

    def __calcMasses__(self):
        self.__massAir=self.densOfAir*self.__volume
        self.__massH2O=self.aH*self.__volume
        self.__massCO2=self.mfco2*self.__massAir
        
        self.__molAir=self.__massAir/self.molar_mass_humid_air
        self.__molH2O=self.__massH2O/(18.01528*u.g/u.mol)
        self.__molCO2=self.__massCO2/(44.0095*u.g/u.mol)
        
    def mix(self, other,inplace=False):
        if isinstance(other,vap)!= True:
            raise ValueError('can only mix objects of type vap')
        elif inplace==False:
            tempself=self+other
            return (tempself-other.volume)
        elif inplace==True:
            tempself=(self+other)-other.volume
            self.__dict__.update(tempself.__dict__)
        
    def transpire(self, Water):
        if Water.unit.physical_type=='mass':    
            gaseousVolume=( (Water/(18.01528 *(u.g/u.mol) ) )* c.R * self.temp.to('Kelvin', equivalencies=u.temperature()) ) / self.Pressure
            self.__outflow=self.__outflow+gaseousVolume.cgs
            self.aH=((self.aH*self.volume)+Water)/(self.volume+gaseousVolume)
            return(gaseousVolume)
        elif Water.unit.physical_type=='amount of substance': 
            gaseousVolume=( Water* c.R * self.temp.to('Kelvin', equivalencies=u.temperature()) ) / self.Pressure
            self.__outflow=self.__outflow+gaseousVolume.cgs
            self.mH=( (self.mH* ( self.massAir/self.molar_mass_humid_air ) ) +Water ) / ( (self.massAir/self.molar_mass_humid_air)+Water )
        else:
            raise ValueError('Can only accept mass or moles as argument')
        self.__calcMasses__()
        #add gasvol to outflow!
        
    def assim(self, CO):
        if CO.unit.physical_type=='mass':    
            gaseousVolume=( (CO/(44.0095 *(u.g/u.mol) ) )* c.R * self.temp.to('Kelvin', equivalencies=u.temperature()) ) / self.Pressure
            self.__outflow=self.__outflow-gaseousVolume.cgs
            self.mfco2=((self.mfco2*self.massAir)-CO)/(self.massAir-CO)
        elif CO.unit.physical_type=='amount of substance':
            gaseousVolume=( CO* c.R * self.temp.to('Kelvin', equivalencies=u.temperature()) ) / self.Pressure
            self.__outflow=self.__outflow-gaseousVolume.cgs
            self.Cs=( (self.Cs* ( self.massAir/self.molar_mass_humid_air ) ) -CO ) / ( (self.massAir/self.molar_mass_humid_air)-CO )
        else:
            raise ValueError('Can only accept mass or moles as argument')
        self.__calcMasses__()
        #add gasvol to outflow!
    
    def calcET0(self,solarRadiation):
        
        Rns=(1-0.23)*solarRadiation
        Rnl=(4.903*10**-9*u.MJ*u.K**-4*u.m**-2*u.day**-1)*(self.tempK**4)*(0.34-0.14*np.sqrt(self.VP.to(u.kPa).value))
             
        Rn=Rns-Rnl
        
        ga=1/(208/self.ws)
        gs=1/(70*u.s/u.m)
        
        radTerm=self.slopeOfSatPress*(Rn-0)
        vpdTerm=self.densOfAir*self.specHeatofAir*self.VPD*ga
        
        lowerTerm=self.latHeatVapWater*(self.slopeOfSatPress+self.psyConst*(ga/gs) )     
        self.ET0=((radTerm+vpdTerm)/(lowerTerm)).to(u.g/u.m**2/u.s)
        
        return(self.ET0.to(u.g/u.m**2/u.s))

        
class vapArray:
    
    #def __init__(self, temp=[25], rH=[0.5], Pressure=[101325], par=[1000],ws= 2, cs = [400], sw2par=2.114,volume=1*u.m**3):
    def __init__(self, temp=[25], rH=[0.5], Pressure=[101325], par=[1000],cs = [300], ws= [2], sw2par=[2.114], volume=[1],solarInc=[40]):
        self.__members=[]
        for i in range(0,len(temp)):
            self.__members.append(vap(temp[i]*u.Celsius, rH[i], Pressure[i] * u.Pascal, par[i]* u.umol*u.m**-2*u.s**-1,cs[i]* u.umol/u.mol, ws[i]* u.m/u.s,  sw2par[i], volume[i]*u.m**3,solarInc[i]))
            #self.__members.append(vap(temp[i]*u.Celsius,rH[i],Pressure[i]* u.Pascal,par[i] * u.umol*u.m**-2*u.s**-1,cs[i]* u.umol/u.mol))
        
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
        
    def append(self,vapor):
        if isinstance(vapor,vap)!= True:
            raise AttributeError('can only append objects of type vap')
        self.__members.append(vapor)

        
        
        




#%%        

if __name__ == "__main__":
    lst=vapArray()
    air=vap(temp=25*u.Celsius,rH=0.5,volume=12*u.m**3)   
    for i in range(10):
        lst.append(deepcopy(air))
        air.rH+=0.1000#air.rH+0.1#10*u.Celsius
        print(air.rH)
        
