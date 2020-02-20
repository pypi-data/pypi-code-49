from diagnostics import *
from scipy.interpolate import interp1d
from numpy import mean, std, log

def PlotMixingRatios(ax, mixr, yaxis, std_mixr = None,
  color = 'C0', style = '-', scale = 'log'):
  ax.plot(mixr, yaxis, color = color, linewidth = 4, linestyle = style)
  if std_mixr is not None:
    ax.fill_betweenx(yaxis, mixr - std_mixr, mixr + std_mixr,
      facecolor = color, edgecolor = None, alpha = '0.4')
  if scale == 'log':
    ax.set_xscale('log')

def PlotTheta(ax, theta, yaxis, std_theta = None, 
  color = 'C1', style = '-'):
  ax.plot(theta, yaxis, color = color, linewidth = 4, linestyle = style)
  if std_theta is not None:
    ax.fill_betweenx(yaxis, theta - std_theta, theta + std_theta,
      facecolor = color, edgecolor = None, alpha = 0.4)

def PlotVelocity(ax, vel, yaxis, scale = 1., eddy = None, xlims = None):
  ntime = len(vel)

  vel = mean(scale*vel, axis = (1,2))
  avg_vel = mean(vel, axis = 0)
  std_vel = std(vel, axis = 0)/sqrt(ntime)
  if eddy is not None:
    avg_eddy = mean(scale*eddy, axis = 0)
    std_eddy = std(scale*eddy, axis = 0)/sqrt(ntime)

  ax.plot(avg_vel, yaxis, color = 'C0', linewidth = 2, linestyle = '-',
    label = '$\overline{w}$')
  ax.fill_betweenx(yaxis, avg_vel - std_vel, avg_vel + std_vel,
    facecolor = 'C0', edgecolor = None, alpha = '0.4')

  if eddy is not None:
    ax.plot(-avg_eddy, yaxis, color = 'C1', linewidth = 2, linestyle = '-',
      label = "-$\overline{w'\\rho'}/\overline{\\rho}$")
    ax.fill_betweenx(yaxis, -avg_eddy - std_eddy, -avg_eddy + std_eddy,
      facecolor = 'C1', edgecolor = None, alpha = '0.4')

  ax.plot([0., 0.], [min(yaxis), max(yaxis)], '0.5', linewidth = 4, alpha = 0.5)

  if xlims is not None:
    ax.set_xlim(xlims)

  ax.legend(fontsize = 15, loc = 0)
  ax.set_xlabel('Mean vertical velocity (mm/s)', fontsize = 15)

def PlotFlux(ax, vel, var, yaxis, eddy_flux = None,
  legend = 'M', label = 'M', xlims = None, unit = None, scale = 1.):
  avg_mean, std_mean = MeanFlux(vel, var, scale = scale)
  if eddy_flux is not None:
    avg_eddy, std_eddy = EddyFluxFromModel(eddy_flux, scale = scale)
  else:
    avg_eddy, std_eddy = EddyFlux(vel, var, scale = scale)

  ax.plot(avg_mean, yaxis, 'C0', linewidth = 2, 
    label = '$\overline{w}\;\overline{%s}$' % legend)
  ax.fill_betweenx(yaxis, avg_mean - std_mean, avg_mean + std_mean,
    facecolor = 'C0', alpha = 0.4, edgecolor = None)

  ax.plot(-avg_eddy, yaxis, 'C1', linewidth = 2,
    label = "$-\overline{w'%s'}$" % legend)
  ax.fill_betweenx(yaxis, -avg_eddy - std_eddy, -avg_eddy + std_eddy,
    facecolor = 'C1', alpha = 0.4, edgecolor = None)

  ax.plot([0., 0.], [min(yaxis), max(yaxis)], '0.5', linewidth = 4, alpha = 0.5)

  if unit != None:
    ax.set_xlabel('%s flux (%s)' % (label, unit), fontsize = 15)
  else:
    ax.set_xlabel('%s flux (10$^{-6}$ kg m$^{-2}$ s$^{-1}$)' % label, fontsize = 15)

  if xlims is not None:
    ax.set_xlim(xlims)

  return avg_mean, std_mean, avg_eddy, std_eddy

def PlotDivergence(ax, avg_mean, avg_eddy, yaxis, std_mean = None, std_eddy = None,
  legend = 'M', label = 'M', xlims = None, unit = None, scale = 1.):
  div_mean = Gradient(avg_mean*scale, yaxis)
  div_eddy = Gradient(avg_eddy*scale, yaxis)

  if std_mean is not None:
    std_div_mean = 0.5*(std_mean[1:] + std_mean[:-1])/(yaxis[1:] - yaxis[:-1])*scale

  if std_eddy is not None:
    std_div_eddy = 0.5*(std_eddy[1:] + std_eddy[:-1])/(yaxis[1:] - yaxis[:-1])*scale

  yaxisf = (yaxis[1:] + yaxis[:-1])/2.

  ax.plot(div_mean, yaxisf, 'C0--', linewidth = 2,
    label = '$\partial_z(\overline{w}\;\overline{%s})$' % legend)
  if std_mean is not None:
    ax.fill_betweenx(yaxisf, div_mean - std_div_mean, div_mean + std_div_mean,
      facecolor = 'C0', alpha = 0.4, edgecolor = None)

  ax.plot(-div_eddy, yaxisf, 'C1--', linewidth = 2,
    label = "$-\partial_z(\overline{w'%s'})$" % legend)
  if std_eddy is not None:
    ax.fill_betweenx(yaxisf, -div_eddy - std_div_eddy, -div_eddy + std_div_eddy,
      facecolor = 'C1', alpha = 0.4, edgecolor = None)

  if unit != None:
    ax.set_xlabel('%s flux divergence (%s)' % (label, unit), fontsize = 15)
  else:
    ax.set_xlabel('%s flux divergence (10$^{-9}$ kg m$^{-3}$ s$^{-1}$)' % label,
      fontsize = 15)

  if xlims is not None:
    ax.set_xlim(xlims)

  return div_mean, div_eddy

def PlotTrend(ax, time, var, yaxis, scale = 1., legend = 'M'):
  avg_trend, std_trend = TemporalTrend(time, var, scale = scale)
  ax.plot([0., 0.], [min(yaxis), max(yaxis)], '0.5', linewidth = 4, alpha = 0.5)
  ax.plot(avg_trend, yaxis, 'k', linewidth = 2,
    label = '$\partial_t\overline{%s}$' % legend)
  ax.fill_betweenx(yaxis, avg_trend - 2.*std_trend, avg_trend + 2.*std_trend,
    color = 'k', alpha = 0.4, edgecolor = None)

def DrawPressureAxis(ax, paxis, x1, pres, ylims):
  lnpfunc = interp1d(log(pres[::-1]), x1[::-1], bounds_error = False)

  ax2 = ax.twinx()
  ax2.set_ylim(ylims)
  ax2.set_yticks([lnpfunc(log(x)) for x in paxis])
  ax2.set_yticklabels(paxis)
  ax2.set_ylabel('Pressure (bar)', fontsize = 20)

  return ax2, lnpfunc
