from numpy import mean, std, tile, sqrt, array
from scipy.stats import linregress
from scipy.interpolate import interp1d

def MeanFlux(vel, var, scale = 1.):
  ntime, nx3, nx2, nx1 = var.shape
  var_bar = mean(var, axis = (1,2))
  vel_bar = mean(vel, axis = (1,2))
  mean_flux = scale*var_bar*vel_bar

  avg_mean_flux = mean(mean_flux, axis = 0)
  std_mean_flux = std(mean_flux, axis = 0)/sqrt(ntime)
  return avg_mean_flux, std_mean_flux

def EddyFluxFromModel(eddy_flux, scale = 1.):
  ntime = len(eddy_flux)
  avg_eddy_flux = mean(eddy_flux, axis = 0)*scale
  std_eddy_flux = std(eddy_flux, axis = 0)*scale/sqrt(ntime)
  return avg_eddy_flux, std_eddy_flux

def EddyFlux(vel, var, scale = 1.):
  ntime, nx3, nx2, nx1 = var.shape
  var_bar = mean(var, axis = (1,2))
  vel_bar = mean(vel, axis = (1,2))

  vel_pp = vel - tile(vel_bar, (ntime,1,1,1))
  var_pp = var - tile(var_bar, (ntime,1,1,1))
  velvar_bar = mean(vel_pp*var_pp, axis = (1,2))*scale

  avg_eddy_flux = mean(velvar_bar, axis = 0)
  std_eddy_flux = std(velvar_bar, axis = 0)/sqrt(ntime)
  return avg_eddy_flux, std_eddy_flux

def TemporalTrend(time, var, scale = 1.):
  var_bar = mean(var, axis = (1,2))
  _, nx1 = var_bar.shape
  aa, ee = [], []
  for i in range(nx1):
    a, b, r, p, e = linregress(time, var_bar[:,i]*scale)
    aa.append(a)
    ee.append(e)
  return array(aa), array(ee)

def Smooth(var, order = 1):
  if order == 1:
    var[1:-1] = (var[2:] + var[1:-1] + var[:-2])/3.
  elif order == 2:
    var1 = (var[0] + var[1] + var[2])/3.
    varn = (var[-1] + var[-2] + var[-3])/3.
    var[2:-2] = (var[4:] + var[3:-1] + var[2:-2] + var[1:-3] + var[:-4])/5.
    var[1] = var1
    var[-1] = varn
  elif order == 3:
    var1 = (var[0] + var[1] + var[2])/3.
    var2 = (var[0] + var[1] + var[2] + var[3] + var[4])/5.
    varn = (var[-1] + var[-2] + var[-3])/3.
    varn1 = (var[-3] + var[-2] + var[-1] + var[-2] + var[-3])/5.
    var[3:-3] = (var[6:] + var[5:-1] + var[4:-2] + var[3:-3] 
              + var[2:-4] + var[1:-5] + var[:-6])/7.
    var[1] = var1
    var[2] = var2
    var[-1] = varn
    var[-2] = varn1
  return var

def Divergence(var, x1, smooth = 3):
  var = Smooth(var, smooth)
  if smooth > 0:
    var1 = (var[0] + var[1] + var[2])/3.
    varn = (var[-1] + var[-2] + var[-3])/3.
    var[2:-2] = (var[4:] + var[3:-1] + var[2:-2] + var[1:-3] + var[:-4])/5.
    var[1] = var1
    var[-1] = varn
  return (var[1:] - var[:-1])/(x1[1:] - x1[:-1])

def Gradient(var, x1, smooth = 3, order = 1):
  var = Smooth(var, smooth)
  if order == 1:
    return (var[1:] - var[:-1])/(x1[1:] - x1[:-1])
  else:
    return (var[2:] - var[:-2])/(x1[2:] - x1[:-2])
