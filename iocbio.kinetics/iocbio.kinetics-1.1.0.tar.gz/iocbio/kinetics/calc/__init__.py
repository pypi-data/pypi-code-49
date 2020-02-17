"""Modules related to the analysis of the data

The classes in the modules under `iocbio.kinetics.calc` are used as a
base classes for data fitting. In addition, several classes are provided
for fitting and writing the results of the primary data analysis into the
database.

Available analyzers:

- bump to fit temporary transients: :class:`.bump.AnalyzerBump` :class:`.bump.AnalyzerBumpDatabase`
- generic base class: :class:`.generic.AnalyzerGeneric`
- find mean, median, and std: :class:`.mean_med_std.AnalyzerMeanMedStd` :class:`.mean_med_std.AnalyzerMeanMedStdDB`
- fit by linear regression: :class:`.linreg.AnalyzerLinRegress` :class:`.linreg.AnalyzerLinRegressDB` 
- fit by Michaelis-Menten equation: :class:`.mm.AnalyzerMM` :class:`.mm.AnalyzerMMDatabase`
- fit by a sum of linear function and exponent: :class:`.explin_fit.AnalyzerExpLinFit`
- base class for fetching experimental data from the database: :class:`.xy.AnalyzerXY`
- compose multiple analyzers into one: :class:`.composer.AnalyzerCompose`

"""
