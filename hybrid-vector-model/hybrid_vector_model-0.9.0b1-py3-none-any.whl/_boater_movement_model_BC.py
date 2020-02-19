
import os
import sys

import numpy as np
import matplotlib
if os.name == 'posix':
    # if executed on a Windows server. Comment out this line, if you are working
    # on a desktop computer that is not Windows.
    matplotlib.use('Agg')
from matplotlib import pyplot as plt
import autograd.numpy as ag

try:
    from .hybrid_vector_model import *
    from .boater_movement_model import *
except ImportError:
    from hybrid_vector_model import *
    from boater_movement_model import *

# The first command line argument specifies the output file to which all output
# will be written.     
from vemomoto_core.tools.tee import Tee                
if len(sys.argv) > 1:
    teeObject = Tee(sys.argv[1])


def create_predicted_observed_box_plot(observedData, median, quartile1, 
                                       quartile3, percentile5, percentile95, 
                                       mean, labels=None, title="", 
                                       fileName=None):
    
    fig, axes = plt.subplots(1, 1)
    
    if labels is None:
        labels = range(len(percentile5))
    
    stats = []
    for p5, p25, p50, p75, p95, m, label in zip(percentile5, quartile1, 
                                                median, quartile3, 
                                                percentile95, mean, labels):
        
        item = {}
        item["label"] = label
        item["mean"] = m
        item["whislo"] = p5
        item["q1"] = p25
        item["med"] = p50
        item["q3"] = p75
        item["whishi"] = p95
        item["fliers"] = [] # required if showfliers=True
        stats.append(item)
        
    
    lineprops = dict(color='purple')
    boxprops = dict(color='green')
    
    plt.boxplot(observedData)
    axes.bxp(stats, widths=0.5, boxprops=boxprops, whiskerprops=lineprops, 
             medianprops=lineprops)
    plt.title(title)
    
    if fileName is not None:
        plt.savefig(fileName + ".png", dpi=1000)
        plt.savefig(fileName + ".pdf")
        

    

def probability_equal_lengths_for_distinct_paths(edgeNumber=1000, 
                                                 upperBound=None,
                                                 resultPrecision=0.1,
                                                 machinePrecision=1e-15,
                                                 experiments=100000):
    if not upperBound:
        upperBound = np.round(resultPrecision/edgeNumber**2
                              /machinePrecision)
    variance = ((upperBound+1)**2 - 1) / 12 * np.sqrt(edgeNumber)
    mean = upperBound / 2 * edgeNumber
    
    prob1 = 0
    endI = edgeNumber//2-1
    for i in range(endI+1):
        print(i, prob1)
        end = i == endI
        x = np.arange(i*upperBound-0.5, (i+1)*upperBound+end)
        if not i:
            x[0] = 0
        elif end:
            x[-1] = mean
        cdf = normaldist.cdf(x, loc=mean, scale=np.sqrt(variance))
        prob = cdf
        prob[1:] = prob[1:]-prob[:-1]
        prob = prob[1:]
        prob *= prob
        prob1 += np.sum(prob)
    prob1 *= 2
    probAll = 1-np.power(1-prob1, experiments)
    return prob1, probAll

def nbinom_fit(data):
    f = lambda x: -np.sum(nbinom.logpmf(data, x[0], np.exp(-x[1]*x[1]))) 
    
    x0 = (1, 1)
    res = op.minimize(f, x0, method="SLSQP", options={"disp":True})
    
    
    return res.x[0], np.exp(-res.x[1]*res.x[1])

def nbinom_fit_test(n, k1, k2, p=0.4):
    
    data1 = nbinom.rvs(k1, p, size=n)
    data2 = nbinom.rvs(k2, p, size=n)
    data = np.concatenate((data1, data2))
    
    x = nbinom_fit(data)
    print(x)
    
    priorMean = nbinom.mean(k1, p) + nbinom.mean(k2, p)
    posteriorMean = nbinom.mean(*x)
    print(priorMean, 2*posteriorMean)

def draw_operating_hour_reward(kappa):
    
    
    times = np.linspace(0, 12, 10000)
    
    captured = 2*vonmises.cdf(12+times, kappa, 12, 12/np.pi) - 1
    
    plt.plot(2*times, captured)
    plt.xlabel("Operation time")
    plt.ylabel("Covered boater flow")
    
    plt.show()

def main():
    
    #nbinom_fit_test(1000, 1, 100, 0.5)
    #print(probability_equal_lengths_for_distinct_paths(1000, 1e5))
    #sys.exit()
    
    #draw_operating_hour_reward(1.05683124)
    #sys.exit()
    
    restart = True
    restart = False
    #print("test4")
     
      
    """ 
    
    stationSets = [
        np.array([b'6', b'9', b'20', b'6b']),
        np.array([b'14', b'18', b'22', b'6b', b'18b']),
        ]
    
    fileNameEdges = "LakeNetworkExample_full.csv"
    fileNameVertices = "LakeNetworkExample_full_vertices.csv"
    fileNameOrigins = "LakeNetworkExample_full_populationData.csv"
    fileNameDestinations = "LakeNetworkExample_full_lakeData.csv"
    fileNamePostalCodeAreas = "LakeNetworkExample_full_postal_code_areas.csv"
    fileNameObservations = "LakeNetworkExample_full_observations.csv"
    fileNameObservations = "LakeNetworkExample_full_observations_new2.csv"
    fileNameObservations = "shortExample3_SimulatedObservations.csv"
    fileNameObservations = "shortExample1_SimulatedObservations.csv"
    fileNameObservations = "LakeNetworkExample_full_observations_new.csv"
    fileNameComparison = ""
    complianceRate = 0.5
    
    fileNameSave = "shortExample3"
    fileNameSave = "shortExample2"
    fileNameSaveNull = "shortExampleNull"
    fileNameSave = "shortExample1"
    
    '''
    fileNameEdges = "LakeNetworkExample_mini.csv"
    fileNameVertices = "LakeNetworkExample_mini_vertices.csv"
    fileNameOrigins = "LakeNetworkExample_mini_populationData.csv"
    fileNameDestinations = "LakeNetworkExample_mini_lakeData.csv"
    fileNamePostalCodeAreas = "LakeNetworkExample_mini_postal_code_areas.csv"
    fileNameObservations = "LakeNetworkExample_mini_observations.csv"
    
    #fileNameEdges = "LakeNetworkExample_small.csv"
    #fileNameVertices = "LakeNetworkExample_small_vertices.csv"
    
    fileNameSave = "debugExample"
    #'''
    """ 
    fileNameEdges = "ExportEdges_HighwayTraffic.csv" 
    fileNameEdges = "ExportEdges.csv" 
    fileNameVertices = "ExportVertices.csv"
    fileNameOrigins = "ExportPopulation.csv"
    fileNameDestinations = "ExportLakes.csv"
    fileNamePostalCodeAreas = "ExportPostal_Code_Data.csv"
    fileNameObservations = "ZebraMusselSimulation_1.3-0.35-0.8-1.2-11000_SimulatedObservations.csv"
    fileNameObservations = "ZebraMusselSimulation_1.4-0.2-0.8-1.2-1_SimulatedObservations.csv"
    fileNameObservations = "ZebraMusselSimulation_1.4-0.2-0.8-1.2-1_SimulatedObservationsFalseAdded.csv"
    fileNameObservations = "ExportBoaterSurveyFalseRemoved.csv"
    fileNameObservations = "ZebraMusselSimulation_1.4-0.2-0.8-1.2-11000_SimulatedObservations.csv"
    fileNameObservations = "ZebraMusselSimulation_1.6-0.2-0.8-1.1-1_SimulatedObservations.csv"
    fileNameObservations = "ExportBoaterSurvey.csv"
    fileNameObservations = "ExportBoaterSurvey_HR_fit.csv"
    fileNameObservations = "ExportBoaterSurvey_HR_val.csv"
    fileNameObservations = "ExportBoaterSurvey_HR_with_days_fit.csv"
    fileNameObservations = "ExportBoaterSurvey_HR_with_days_validation.csv"
    complianceRate = 0.7959
    
    fileNameSave = "Sim_1.4-0.1-0.8-1.1-1_PathTest" # for road network only.
    fileNameSave = "Sim_1.4-0.2-1-1-1_HR_opt" # for optimization of inspection locations
    fileNameSave = "Sim_1.4-0.2-1-1-1_HR_HW_1" 
    fileNameSave = "Sim_1.4-0.2-1-1-1_HR_val" # for validation
    fileNameComparison = fileNameSave
    fileNameSave = "Sim_1.4-0.2-1-1-1_HR_HW" #for fit and road traffic estimates
    fileNameSaveNull = "Sim_1.4-0.2-1-1-1_HR_HW_null" #for fit and road traffic estimates
    fileNameSaveNull = "Sim_1.4-0.2-1-1-1_HR_val_null" #for fit and road traffic estimates
    #"""  
     
    #redraw_predicted_observed(fileNameSave, fileNameComparison)
    #sys.exit()
    
    print("Starting test. (2)")
     
    #print("Seed")
    
    #np.random.seed() 
    
    routeParameters = ( 
                          (1.4, .2, 1, 1)
                       )
    #"""
    #"""
    flowParameters = {}
    #best parameters one more parameter 
    flowParameters["parametersConsidered"] = np.array( 
        [True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True]
        )
    flowParameters["paramters"] = np.array(
        [-1.71042747e+01,1.15230704e+00,1.23546394e+03,5.55260234e+00,3.50775439e+00,2.53985567e+01,1.01026970e+03,8.86681452e+02,0,-1.8065007296786513,2.69364013e+00,-3.44611446e+00]
        )
    nullParameters = {}
    #best parameters one more parameter 
    nullParameters["parametersConsidered"] = flowParameters["parametersConsidered"].copy()
    nullParameters["parametersConsidered"][:] = False
    #nullParameters["parametersConsidered"][:3] = True
    nullParameters["paramters"] = np.array([-50., 10.])
    nullParameters["paramters"] = np.array([7.42643338e-01, 5.15536529e+04])
    
    #print(TrafficFactorModel.convert_parameters(None, flowParameters["paramters"][2:], flowParameters["parametersConsidered"][2:]))
    #sys.exit()
    """
    #best parameters one less parameter 
    flowParameters["parametersConsidered"] = np.array( 
        [True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True]
        )
    flowParameters["paramters"] = np.array(
        [-1.71042747e+01,1.15230704e+00,1.23546394e+03,5.55260234e+00,3.50775439e+00,2.53985567e+01,1.171835466180462,-1.8065007296786513,2.69364013e+00,-3.44611446e+00]
        )
    
    #best parameters
    flowParameters["parametersConsidered"] = np.array( 
        [True,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,True]
        )
    flowParameters["paramters"] = np.array(
        [-1.71042747e+01,1.15230704e+00,1.23546394e+03,5.55260234e+00,3.50775439e+00,2.53985567e+01,1.01026970e+03,8.86681452e+02,-1.8065007296786513,2.69364013e+00,-3.44611446e+00]
        )
        
    
    
    # best parameters old parameterization
    flowParameters["parametersConsidered"] = np.array( 
        [True,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,False,False,False,True,True]
        )
    flowParameters["paramters"] = np.array(
        [-1.71042747e+01,1.15230704e+00,1.23646394e+03,6.55260234e+00,4.50775439e+00,2.63985567e+01,1.01126970e+03,8.87681452e+02,1.64227810e-01,2.69364013e+00,-3.44611446e+00]
        )
    """
    routeChoiceParameters = [0.048790208690779414, -7.661288616999463, 0.0573827962901976]
    nullRouteChoiceParameters = [1, 0, 0.0001]
    travelTimeParameters = np.array([14.00344885,  1.33680321])
    nullTravelTimeParameters = np.array([0, 1e-10])
    properDataRate = 0.9300919842312746
    
    """
    nullModel = HybridVectorModel.new(
                fileNameBackup=fileNameSaveNull, 
                trafficFactorModel_class=TrafficFactorModel,
                fileNameEdges=fileNameEdges,
                fileNameVertices=fileNameVertices,
                fileNameOrigins=fileNameOrigins,
                fileNameDestinations=fileNameDestinations,
                fileNamePostalCodeAreas=fileNamePostalCodeAreas,
                fileNameObservations=fileNameObservations,
                complianceRate=complianceRate,
                preprocessingArgs=None,
                #preprocessingArgs=(10,10,10),
                #considerInfested=True, 
                #findPotentialRoutes=True,
                edgeLengthRandomization=0.001,
                routeParameters=(1.0001, 0.9999, 0.5, 2), 
                readSurveyData=True,
                properDataRate=properDataRate,
                #createRouteChoiceModel=True,
                fitRouteChoiceModel=True,
                #readOriginData=True,
                #readOriginData=True, 
                travelTimeParameters=nullTravelTimeParameters, 
                fitTravelTimeModel=True,
                fitFlowModel=True,
                routeChoiceParameters=nullRouteChoiceParameters, #continueRouteChoiceOptimization=True,
                flowParameters=nullParameters, #continueTrafficFactorOptimization=True, #readDestinationData=True,  readPostalCodeAreaData=True, , #  #findPotentialRoutes=True, #  extrapolateCountData=True , # #readSurveyData=True   ###  #  #   findPotentialRoutes=False ,  readSurveyData=True 
                restart=restart, #readSurveyData=True, 
                )
    sys.exit()
    """
    model = HybridVectorModel.new(
                fileNameBackup=fileNameSave, 
                trafficFactorModel_class=TrafficFactorModel,
                fileNameEdges=fileNameEdges,
                fileNameVertices=fileNameVertices,
                fileNameOrigins=fileNameOrigins,
                fileNameDestinations=fileNameDestinations,
                fileNamePostalCodeAreas=fileNamePostalCodeAreas,
                fileNameObservations=fileNameObservations,
                complianceRate=complianceRate,
                preprocessingArgs=None,
                #preprocessingArgs=(10,10,10),
                #considerInfested=True, 
                #findPotentialRoutes=True,
                edgeLengthRandomization=0.001,
                routeParameters=routeParameters, 
                #readSurveyData=True,
                properDataRate=properDataRate,
                #createRouteChoiceModel=True,
                #fitRouteChoiceModel=True,
                #readOriginData=True,
                #readDestinationData=True, 
                fitFlowModel=True,
                routeChoiceParameters=routeChoiceParameters, continueRoutChoiceOptimization=False,
                flowParameters=flowParameters, continueTrafficFactorOptimization=True, #readDestinationData=True,  readPostalCodeAreaData=True, , #  #findPotentialRoutes=True, #  extrapolateCountData=True , # #readSurveyData=True   ###  #  #   findPotentialRoutes=False ,  readSurveyData=True 
                travelTimeParameters=travelTimeParameters, 
                #fitTravelTimeModel=True,
                restart=restart, #readSurveyData=True, 
                )
    #model.compare_travel_time_distributions(model.fileName)
    
    #sys.exit()
    
    '''
    model = saveobject.load_object(fileNameSave + ".vmm")
    #'''
    #"""
    #model.save_model_predictions()
    '''
    model.save_simulated_observations(shiftNumber=2500, dayNumber=600, 
                                      stationSets=stationSets)
    '''
    #"""
    model.create_quality_plots(saveFileName=model.fileName, worstLabelNo=5,
                               comparisonFileName=fileNameComparison)
    model.test_1_1_regression(20, saveFileName=model.fileName,
                              comparisonFileName=fileNameComparison)
    model.save(model.fileName)
    sys.exit()
    model.save_simulated_observations()
    model.check_count_distributions_NB(fileName=model.fileName+"-pvals")
    sys.exit()
    #"""
    #'''
    #model.optimize_inspection_station_placement(20, saveFileName=model.fileName)
    allowedShifts = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    allowedShifts = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
    allowedShifts = [6, 9, 10, 14, 18]
    allowedShifts = [6., 7., 8., 9., 10., 11., 12., 13., 14., 16., 18., 20., 23.]
    allowedShifts = [4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22]
    allowedShifts = [2, 4 ]
    allowedShifts = [4, 6, 8, 9, 10, 11, 12, 13, 15, 17, 20, 22]
    allowedShifts = [5, 8, 10, 11, 12, 15, 19, 22]
    
    """
    RouteChoiceModel.NOISEBOUND = 0.2
    print("Setting noise bound to", RouteChoiceModel.NOISEBOUND)
    model.fit_route_model(routeParameters, True)
    RouteChoiceModel.NOISEBOUND = 0.02
    print("Setting noise bound to", RouteChoiceModel.NOISEBOUND)
    model.fit_route_model(routeParameters, True)
    """
    
    routeChoiceParamCandidates = [
                                  None,
                                  [0.00739813, -5.80269191, 0.7815986],
                                  [0.19972783, -5.69001292, 0.012684587],
                                  ]
    """
    RouteChoiceModel.NOISEBOUND = 0.2
    for r in routeChoiceParamCandidates:
        print("Setting Route Choice parameters to", r)
        model.fit_route_model(routeParameters, True, np.array(r))
        model.fit_flow_model(flowParameters=flowParameters, continueFlowOptimization=True,
                             refit=True)
    """
        
    def setRouteParameters(m, val, refit=True):
        if val is not None:
            m.NOISEBOUND = 1
            m.fit_route_model(routeParameters, True, np.array(val), False, get_CI=False)
            if refit:
                m.fit_flow_model(flowParameters=flowParameters, continueFlowOptimization=True,
                                 refit=True, get_CI=False)
    def setNoise(m, val):
        if val is not None:
            print("Set noise to", val)
            m.NOISEBOUND = 1
            routeParams = np.array(m.routeModel["routeChoiceModel"].parameters)
            routeParams[0] = val
            m.fit_route_model(True, routeParams, False, get_CI=False)
    defaultArgs = dict(costShift=3.5, costSite=1., shiftLength=8., costRoundCoeff=None, 
                       nightPremium=(5.5, 21, 5), baseTimeInv=24, timeout=3000,
                       init_greedy=True, costBound=80.)#, loadFile=False) 
    
    """
    model.set_infested(b'J54145')
    model.set_infested(b'J54170')
    model.set_infested(b'J54185')
    model.fileName += "Idaho"
    #"""
    model.save_model_predictions()
    
    #model.fileName += "_noinit_"
    #model.create_caracteristic_plot("costBound", [20., 80., 160.], **defaultArgs)
    #model.create_budget_plots(5, 75, 15, **defaultArgs)
    #model.create_budget_plots(55, 100, 10, **defaultArgs)
    #model.create_budget_plots(100, 150, 11, **defaultArgs)
    #model.create_budget_plots(135, 150, 4, **defaultArgs)
    
    sys.exit()
    #model.create_budget_plots(5, 150, 30, **defaultArgs)
    
    
    model.create_caracteristic_plot("costBound", [25., 50., 100.], characteristicName="Budget", **defaultArgs)
    
    #model.create_caracteristic_plot(setRouteParameters, routeChoiceParamCandidates, 
    #                                "NoiseRefit", [0.047, 0.007, 0.2],
    #                                **defaultArgs)
    noise = [0.001, 0.05, 0.2]
    #model.create_caracteristic_plot(setNoise, noise, "Noise level", **defaultArgs)
    
    sys.exit()
    
    for ignoreRandomFlow in False, True:
        #profile("model.optimize_inspection_station_operation(2, 1, 30, 6., allowedShifts=allowedShifts, costRoundCoeff=1, baseTimeInv=18, ignoreRandomFlow=ignoreRandomFlow, saveFileName=model.fileName)", 
        #        globals(), locals()) 
        #"""        
        model.optimize_inspection_station_operation(3.5, 1., 10., 7, #80
                                                    #allowedShifts=allowedShifts, #[6, 8, 10, 11, 12, 14], 
                                                    costRoundCoeff=0.5, 
                                                    nightPremium=(1.2, 22, 6),
                                                    baseTimeInv=24,
                                                    ignoreRandomFlow=ignoreRandomFlow,
                                                    integer=True,
                                                    extended_info=True
                                                    )
    #'''
    """
    print(find_shortest_path(model.roadNetwork.vertices.array,
                             model.roadNetwork.edges.array,
                             0, 9))
    """
    
    """
    stations = [b'386', b'307', b'28']
        
    fromIDs = [b'J54130', b'J54181', b'J54173']
    
    toIDs = [b'L329518145A', b'L328961702A', b'L328974235A']
    
    ps = []
    for stationID, fromID, toID in iterproduct(stations, fromIDs, toIDs):
        #print("Consider journeys from", fromID, "to", toID, "observed at", 
        #      stationID)
        fname = model.fileName + str(stationID + fromID + toID)
        p = model.compare_distributions(stationID, fromID, toID, 15, saveFileName=fname)
        if p is not None:
            ps.append(p)
    
    try:
        print("p distribution:", np.min(ps), np.max(ps), np.histogram(ps))
    except Exception:
        pass
       
    #"""
    #model.compare_distributions(b'3', b'1', b'L1', 15, saveFileName=model.fileName)
    #model.test_1_1_regression(20, routeParameters[0], model.fileName + str(routeParameters[0]))
    #model.save_simulated_observations(shiftNumber=1000, fileName=model.fileName+"1000")
    #model.save_simulated_observations()
    plt.show()
    
    """
    parametersConsidered = np.array([True] * 7)
    #parametersConsidered[2] = False
    #x0Stat = (np.log(5), np.sqrt(-np.log(0.7)), np.sqrt(-np.log(.1)), -3, np.sqrt(-np.log(0.1))) 
    #x0Flex = np.array((np.log(2), 1, np.log(1), -1, 1, 1, -2))
    x0Stat = (1, 0.5, 5, -3, 1.5) 
    x0Stat = (5.5, 0.5, 1.5, -3, 1.5) 
    x0Flex = np.array((2, 1, 1, -1, 1, 1, -2))
    x0 = np.array((*x0Stat, *x0Flex[parametersConsidered]))
    #model.simulate_count_data_test(5, x0, covariates=parametersConsidered)
    model.save_simulated_observations(x0, parametersConsidered, "area", shiftNumber=2000, fileName=model.fileName+"1000")
    #"""
    
    """
    
    #profile("network = TransportNetwork(fileNameEdges, fileNameVertices)", globals(), locals())
    if exists(fileNameSave) and not restart:
        print("Loading file...")
        network = saveobject.load_object(fileNameSave)
        print("Edge number", len(network.edges))
        print("Edge size", network.edges.size)
    else:
        network = TransportNetwork(fileNameEdges, fileNameVertices)
        print("Edge number", len(network.edges))
        network.lock = None 
        print("Saving file...")
        saveobject.save_object(network, fileNameSave)
    
    #network.find_potential_routes(1.5, .2)
    #profile("network.find_potential_routes(1.5, .2)", globals(), locals())  
    #print("Timed execution:", Timer(network.find_potential_routes).timeit(1))
    #network.find_alternative_paths_test(1.5)
    for stretch, lo, prune in (
                               (1.25, .1, .7),
                               (1.5, .2, .7),
                               (1.25, .2, .7),
                               (1.25, .1, 1),
                               (1.25, .2, 1),
                               (1.5, .2, 1),
                               ):
        print("Timed execution:", Timer("network.find_potential_routes(stretch, lo, prune)", globals=locals()).timeit(1))
        print("="*80)
        print()
        print("="*80)
    """
    
if __name__ == '__main__':
    #f = "ZebraMusselSimulation_1.4-0.2-1-1-1_HR_opt[3.5, 1, 50.0, 8, (1.2, 22, 6), 0].dat"
    #o = saveobject.load_object(f)
    #print(o)
    
    
    main()
    # LD_PRELOAD=../anaconda3/lib/libmkl_core.so python ...