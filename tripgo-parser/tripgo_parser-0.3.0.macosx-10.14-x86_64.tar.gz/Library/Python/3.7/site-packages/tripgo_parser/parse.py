import numpy as np
import json
import time
import pandas as pd
import numpy as np
from os import path
import os

class JsonData():
    def __init__(self, jsonData):
        self.rawJsonData = jsonData
        self.jsonData = self.open()

    def open(self):
        with open(self.rawJsonData, 'r') as file:
            openedJson = json.loads(file.read())

        return openedJson

class Parse:
    def __init__(self, jsonData, startime='', tripid=''):
        self.jsonData = jsonData
        self.allGroups = self.jsonData['groups']
        self.allSegmentTemplates = self.jsonData['segmentTemplates']
        self.allGroupData = {}
        self.numberOfGroups = len(self.allGroups)
        self.tripid = tripid
        self.startime = startime
        self.missingTaxi = 0
        self.missingWalking = 0
        self.missingCycling = 0
        self.missingDriving= 0
        self.missingTransit = 0
        self.missingTrain = 0
        self.missingBus = 0
        self.missingTram = 0

        self.bestIndex = \
        {
        'driving': self.getBestDriving(),
        'taxi': self.getBestTaxi(),
        'cycling': self.getBestCycling(),
        'walking': self.getBestWalking(),
        'transit': self.getBestTransit()
        }


    def getCompiledData(self):
        transitData = self.getTransitData()
        drivingData = self.getDrivingData()
        taxiData = self.getTaxiData()
        cyclingData = self.getCyclingData()
        walkingData = self.getWalkingData()

        compiled_data = \
        {
        'startime': self.startime,
        'car': abs(self.missingDriving - 1), 'taxi': abs(self.missingTaxi - 1),
        'cycling': abs(self.missingCycling - 1),
        'walking': abs(self.missingWalking -1),
        'transit': abs(self.missingTransit - 1),
        **transitData,
        **drivingData,
        **taxiData,
        **cyclingData,
        **walkingData
        }

        if self.tripid != '':
            compiled_data.update({'tripid': self.tripid})

        if self.startime != '':
            compiled_data.update({'startime': self.startime})

        return compiled_data

    def getBusData(self):
        index = self.bestIndex.get('bus')
        if index is None:
            self.missingBus += 1
            return {}
        else:
            group = self.allGroups[index]
            groupData = Group(group, self.jsonData)

            parsedGroupData = \
            {
            'bus_travelTime': groupData.totalTravelTime,
            'bus_frequency': groupData.frequency,
            'bus_weightedScore': groupData.weightedScore, # for testing
            'bus_waitTime': groupData.waitTime,
            'bus_calorieCost': groupData.caloriesCost,
            'bus_numberOfModes': len(groupData.segmentData['Modes']),
            'bus_modes': groupData.tripModes,
            'bus_walkingDistance': groupData.segmentData['Walking Distance'],
            'bus_numberOfTransfers': groupData.numberOfTransfers,
            'bus_hassleCost': groupData.hassleCost,
            'bus_timeOnBus': groupData.timeOnMainMode,
            'bus_timeNotOnBus': groupData.timeOnOtherModes
            }

            return parsedGroupData

    def getTrainData(self):
        index = self.bestIndex.get('train')
        if index is None:
            self.missingTrain += 1
            return {}
        else:
            group = self.allGroups[index]
            groupData = Group(group, self.jsonData)

            parsedGroupData = \
            {
            'train_travelTime': groupData.totalTravelTime,
            'train_frequency': groupData.frequency,
            'train_weightedScore': groupData.weightedScore, # for testing
            'train_waitTime': groupData.waitTime,
            'train_caloriesCost': groupData.caloriesCost,
            'train_modeSwapCount': len(groupData.segmentData['Modes']),
            'train_modes': groupData.tripModes,
            'train_walkingDistance': groupData.segmentData['Walking Distance'],
            'train_numberOfTransfers': groupData.numberOfTransfers,
            'train_hassleCost': groupData.hassleCost,
            'train_timeOnTrain': groupData.timeOnMainMode,
            'train_timeNotOnTrain': groupData.timeOnOtherModes
            }

            return parsedGroupData

    def getTramData(self):
        index = self.bestIndex.get('tram')
        if index is None:
            self.missingTram += 1
            return {}
        else:
            group = self.allGroups[index]
            groupData = Group(group, self.jsonData)

            parsedGroupData = \
            {
            'tram_travelTime': groupData.totalTravelTime,
            'tram_frequency': groupData.frequency,
            'tram_weightedScore': groupData.weightedScore, # for testing
            'tram_waitTime': groupData.waitTime,
            'tram_calorieCost': groupData.caloriesCost,
            'tram_modeSwapCount': len(groupData.segmentData['Modes']),
            'tram_modes': groupData.tripModes,
            'tram_walkingDistance': groupData.segmentData['Walking Distance'],
            'tram_numberofTransfers': groupData.numberOfTransfers,
            'tram_hassleCost': groupData.hassleCost,
            'tram_timeOnTram': groupData.timeOnMainMode,
            'tram_timeNotOnTram': groupData.timeOnOtherModes
            }

            return parsedGroupData


    def getDrivingData(self):
        index = self.bestIndex.get('driving')
        if index is None:
            self.missingDriving += 1
            return {}
        else:
            group = self.allGroups[index]
            groupData = Group(group, self.jsonData)

            parsedGroupData = \
            {
            'car_travelTime': groupData.totalTravelTime,
            'car_weightedScore': groupData.weightedScore, # for testing
            'car_fuelCost': groupData.segmentData['Fuel Cost'],
            'car_privateParkingExists': groupData.segmentData['Parking Exists'],
            'car_privateParkingCost': groupData.segmentData['Parking Cost'],
            'car_travelTime_trafficless': groupData.segmentData['Traffic-less Duration'],
            'car_calorieCost': groupData.caloriesCost, 'car_walkingDistance': groupData.segmentData['Walking Distance'], 'car_hassleCost': groupData.hassleCost,
            'car_drivingDistances': groupData.segmentData['Distances'].get('me_car'),
            }

            return parsedGroupData

    def getCyclingData(self):
        index = self.bestIndex.get('cycling')
        if index is None:
            self.missingCycling += 1
            return {}
        else:
            group = self.allGroups[index]
            groupData = Group(group, self.jsonData)

            parsedGroupData = \
            {
            'cycling_travelTime': groupData.totalTravelTime,
            'cycling_weightedScore': groupData.weightedScore, # for testing
            'cycling_calorieCost': groupData.caloriesCost,
            'cycling_hassleCost': groupData.hassleCost,
            'cycling_distances': sum(groupData.segmentData['Distances'].values()),
            'cycling_distance_safe': groupData.segmentData['Meters Safe'],
            'cycling_distance_unsafe': groupData.segmentData['Meters Unsafe']
            }
            return parsedGroupData

    def getWalkingData(self):
        index = self.bestIndex.get('walking')
        if index is None:
            self.missingWalking += 1
            return {}
        else:
            group = self.allGroups[index]
            groupData = Group(group, self.jsonData)

            parsedGroupData = \
            {
            'walking_travelTime': groupData.totalTravelTime,
            'walking_weightedScore': groupData.weightedScore, # for testing
            'walking_calorieCost': groupData.caloriesCost,
            'walking_hassleCost': groupData.hassleCost,
            'walking_distances': groupData.segmentData['Distances'].get('wa_wal')
            }
            return parsedGroupData

    def getTaxiData(self):
        index = self.bestIndex.get('taxi')
        if index is None:
            self.missingTaxi += 1
            return {}
        else:
            group = self.allGroups[index]
            groupData = Group(group, self.jsonData)

            parsedGroupData = \
            {
            'taxi_travelTime': groupData.totalTravelTime,
            'taxi_weightedScore': groupData.weightedScore, # for testing
            'taxi_waitTime': groupData.segmentData['Wait Time'],
            'taxi_cost': groupData.segmentData['Taxi Fare'],
            'taxi_walkingDistance': groupData.segmentData['Walking Distance'],
            'taxi_hassleCost': groupData.hassleCost
            }
            return parsedGroupData
    
    def getTransitData(self):
        index = self.bestIndex.get('transit')
        if index is None:
            self.missingTransit += 1
            return {}
        
        else:
            group = self.allGroups[index]
            groupData = Group(group, self.jsonData)

            parsedGroupData = \
            {
            'transit_totalTravelTime': groupData.totalTravelTime,
            'transit_weightedScore': groupData.weightedScore,
            'transit_waitTime': groupData.waitTime,
            'transit_mainMode': groupData.mode,
            'transit_allModes': groupData.tripModes,
            'transit_timeOnMainMode': groupData.timeOnMainMode,
            'transit_timeOnOtherModes': groupData.timeOnOtherModes,
            'transit_timeOnEachMode': groupData.segmentData['Travel Times'],
            'transit_distances': groupData.segmentData['Distances'], 
            'transit_modes': groupData.segmentData['Modes'],
            'transit_start': groupData.segmentData['Start'],
            'transit_end': groupData.segmentData['End'],
            'transit_hassleCost': groupData.hassleCost,
            'transit_numberOfTransfers': groupData.numberOfTransfers
            }

            return parsedGroupData

    ### 'Best' functions to be deleted, retain only getBest()

    def getBestBus(self):
        bus = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)
            if 'pt_pub_bus' in groupData.mode:
                bus[i] = groupData.weightedScore

        if bus != {}:
            busGroupNumberMin = min(bus, key=lambda x: bus.get(x))
            return busGroupNumberMin

    def getBestTram(self):
        tram = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)
            if 'pt_pub_tram' in groupData.mode:
                tram[i] = groupData.weightedScore

        if tram != {}:
            tramGroupNumberMin = min(tram, key=lambda x: tram.get(x))
            return tramGroupNumberMin

    def getBestTrain(self):
        train = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)
            if 'pt_pub_train' in groupData.mode:
                train[i] = groupData.weightedScore

        if train != {}:
            trainGroupNumberMin = min(train, key=lambda x: train.get(x))
            return trainGroupNumberMin

    def getBestDriving(self):
        driving = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)
            if 'me_car' in groupData.mode:
                driving[i] = groupData.weightedScore

        if driving != {}:
            drivingGroupNumberMin = min(driving, key=lambda x: driving.get(x))
            return drivingGroupNumberMin

    def getBestCycling(self):
        cycling = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)
            if 'cy_bic' in groupData.mode:
                cycling[i] = groupData.weightedScore

        if cycling != {}:
            cyclingGroupNumberMin = min(cycling, key=lambda x: cycling.get(x))
            return cyclingGroupNumberMin

    def getBestTaxi(self):
        taxi = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)
            if 'ps_tax' in groupData.mode:
                taxi[i] = groupData.weightedScore

        if taxi != {}:
            taxiGroupNumberMin = min(taxi, key=lambda x: taxi.get(x))
            return taxiGroupNumberMin

    def getBestWalking(self):
        walking = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)
            if 'wa' in groupData.mode:
                walking[i] = groupData.weightedScore

        if walking != {}:
            walkingGroupNumberMin = min(walking, key=lambda x: walking.get(x))
            return walkingGroupNumberMin
    
    def getBestTransit(self):
        transit = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)
            if 'pt_pub' in groupData.mode:
                transit[i] = groupData.weightedScore
            
        if transit != {}:
            transitGroupNumberMin = min(transit, key=lambda x: transit.get(x))
            return transitGroupNumberMin
    
    def getBest(self, mode=''):
        best = {}
        for i in range(len(self.allGroups)):
            group = self.allGroups[i]
            groupData = Group(group, self.jsonData)

            if mode != '':
                if mode in groupData.mode:
                    best[i] = groupData.weightedScore
            else:
                best[i] = groupData.weightedScore
        
        if best != {}:
            bestGroupNumberMin = min(best, key=lambda x: best.get(x))
            return bestGroupNumberMin
            
            

class Group:
    def __init__(self, groupData, jsonData):
        self.jsonData = jsonData
        self.groupData = groupData
        self.frequency = self.checkFrequency()
        self.bestTripID = self.getLowestWS()
        self.getTripData()

    def checkFrequency(self):
        try:
            frequency = self.groupData['frequency']
        except:
            frequency = 'N/A'
        return frequency

    def getTripData(self):
        for trip in self.groupData['trips']:
            if trip['id'] == self.bestTripID:
                tripData = Trip(trip, self.jsonData)
                self.travelTime = tripData.totalTravelTime
                self.caloriesCost = tripData.caloriesCost
                self.hassleCost = tripData.hassleCost
                self.totalTravelTime = tripData.totalTravelTime
                self.mode = tripData.tripMode
                self.weightedScore = tripData.weightedScore
                self.tripMode = tripData.tripMode
                self.tripModes = tripData.tripModesAlt
                self.numberOfTransfers = tripData.numberOfTransfers
                self.segmentData = tripData.segmentData
                self.timeOnMainMode = tripData.timeOnMainMode
                self.timeOnOtherModes = tripData.timeOnOtherModes
                

    def getLowestWS(self):
        tripsWS = {}
        tripsWSs = []
        for trip in self.groupData['trips']:
            tripsWS[trip['id']] = trip['weightedScore']
            tripsWSs.append(trip['weightedScore'])

        minimumTripWS = min(tripsWS, key=lambda x: tripsWS.get(x))
        self.weightedScore = min(tripsWSs)

        return minimumTripWS

class Trip:
    def __init__(self, tripData, jsonData):
        self.jsonData = jsonData
        self.tripData = tripData
        self.mainSegmentHashCode = tripData['mainSegmentHashCode']
        self.weightedScore = tripData['weightedScore']
        self.caloriesCost = tripData['caloriesCost']
        self.id = tripData['id']
        self.totalTravelTime = tripData['arrive'] - tripData['depart']
        self.hassleCost = tripData['hassleCost']
        self.tripModes, self.tripModesAlt = self.getModes()
        self.tripMode = self.getMode()
        self.segmentData = self.getSegmentData()
        self.numberOfTransfers = self.numberOfTransferss()
        self.timeOnMainMode = self.getTimeOnMainMode()
        self.timeOnOtherModes = self.getTimeOnOtherModes()

    def getSegmentData(self):
        segmentsData = \
        {
        'Local Cost': 0,
        'Fuel Cost': 0,
        'Parking Cost': 0,
        'Parking Exists': False,
        'Modes': [],
        'Distances': {},
        'Start': {},
        'End': {},
        'Travel Times': {},
        'Walking Distance': 0,
        'Traffic-less Duration': 0,
        'Wait Time': 0,
        'Meters Safe': 0,
        'Meters Unsafe': 0
        }

        for segmentData in self.tripData['segments']:
            segmentHashCode = segmentData['segmentTemplateHashCode']
            segmentTravelTime = segmentData['endTime'] - segmentData['startTime']
            segment = Segment(segmentHashCode, self.jsonData)
            segmentsData['Fuel Cost'] += segment.fuelCost
            segmentsData['Parking Cost'] += segment.parkingCost
            segmentsData['Parking Exists'] = segment.hasParking
            segmentsData['Modes'].append(segment.mode)
            segmentsData['Distances'][segment.mode] = segment.distance
            segmentsData['Travel Times'][segment.mode] = segmentTravelTime
            segmentsData['Walking Distance'] += segment.walkingDistance
            segmentsData['Traffic-less Duration'] += segment.durationWithoutTraffic
            segmentsData['Meters Safe'] += segment.metersSafe
            segmentsData['Meters Unsafe'] += segment.metersUnsafe
            if 'pt_pub' in segment.mode:
                segmentsData['Start'][segment.mode] = {segment.PTstart: segmentData['startTime']}
                segmentsData['End'][segment.mode] = {segment.PTend: segmentData['endTime']}
            if 'ps_' in segment.mode:
                segmentsData['Taxi Fare'] = segment.localCost
            if 'stationary_' in segment.mode:
                segmentsData['Wait Time'] += segmentTravelTime
        
        return segmentsData
    
    def filterStartEnd(self, data):
        dictionary = {k: v for k, v in dict.items() if v is not None}
        return dictionary


    def getMode(self):
        mainSegment = Segment(self.mainSegmentHashCode, self.jsonData)
        mainSegmentMode = mainSegment.mode

        return mainSegmentMode

    def getModes(self):
        tripModes = []
        tripModesAlt = {}
        i = 0
        for segment in self.tripData['segments']:
            segmentHashCode = segment['segmentTemplateHashCode']
            segmentTemplate = Segment(segmentHashCode, self.jsonData)
            tripModesAlt[i] = segmentTemplate.mode
            i += 1
        return tripModes, tripModesAlt

    def numberOfTransferss(self):
        numberOfTransfers = 0
        for item in self.segmentData['Modes']:
            if 'pt' in item:
                numberOfTransfers += 1

        if numberOfTransfers > 0:
            numberOfTransfers -= 1

        return numberOfTransfers


    def getTimeOnMainMode(self):
        timeOnMainMode = 0
        for segment in self.tripData['segments']:
            if segment['segmentTemplateHashCode'] == self.mainSegmentHashCode:
                timeOnMainMode += (segment['endTime'] - segment['startTime'])

        return timeOnMainMode

    def getTimeOnOtherModes(self):
        timeOnOtherModes = 0
        for segment in self.tripData['segments']:
            if segment['segmentTemplateHashCode'] != self.mainSegmentHashCode:
                timeOnOtherModes += (segment['endTime'] - segment['startTime'])

        return timeOnOtherModes

class Segment:
    def __init__(self, segmentHashCode, jsonData):
        self.jsonData = jsonData
        self.allSegmentTemplates = jsonData['segmentTemplates']
        self.segmentHashCode = segmentHashCode
        self.segmentTemplate = self.findSegment()
        self.localCost = self.localCosts()
        self.fuelCost = self.fuelCosts()
        self.hasParking = self.hasParkings()
        self.parkingCost = self.parkingCosts()
        self.mode = self.segmentTemplate['modeInfo'].get('identifier')
        self.distance = self.distances()
        self.walkingDistance = self.walkingDistances()
        self.durationWithoutTraffic = self.durationWithoutTraffics()
        self.metersSafe = self.metersSafes()
        self.metersUnsafe = self.metersUnsafes()
        self.PTstart = self.getPTStart()
        self.PTend = self.getPTEnd()

    def getPTStart(self):
        if 'pt_pub' in self.mode:
            try:
                start = self.segmentTemplate['from']['address']
            finally:
                return start
    
    def getPTEnd(self):
        if 'pt_pub' in self.mode:
            try:
                end = self.segmentTemplate['to']['address']
            finally:
                return end
    
    def findSegment(self):
        for segmentTemplate in self.allSegmentTemplates:
            if segmentTemplate['hashCode'] == self.segmentHashCode:
                return segmentTemplate

    def localCosts(self):
        try:
            localCost = self.segmentTemplate['localCost']['cost']
        except:
            localCost = 0
        return localCost

    def fuelCosts(self):
        fuelCost = 0
        try:
           costComponents = self.segmentTemplate['localCost']['costComponents']
           for costComponent in costComponents:
               if costComponent['type'] == 'FUEL':
                   fuelCost += costComponent['cost']
        except:
            pass
        return fuelCost

    def parkingCosts(self):
        parkingCost = 0
        try:
            costComponents = self.segmentTemplate['localCost']['costComponents']
            for costComponent in costComponents:
                if costComponent['type'] == 'PARKING':
                    parkingCost += costComponent['cost']
        except:
            pass
        return parkingCost

    def hasParkings(self):
        hasParking = False
        try:
            if self.segmentTemplate['hasCarParks']:
                hasParking = True
        except:
            pass
        return hasParking

    def walkingDistances(self):
        walkingDistance = 0
        try:
            if 'wa_wal' in self.segmentTemplate['modeInfo']['identifier']:
                walkingDistance += self.segmentTemplate['metres']
        except:
            pass

        return walkingDistance

    def durationWithoutTraffics(self):
        durationWithoutTraffic = 0
        try:
            durationWithoutTraffic += self.segmentTemplate['durationWithoutTraffic']
        except:
            pass

        return durationWithoutTraffic

    def metersSafes(self):
        metersSafe = 0
        try:
            metersSafe += self.segmentTemplate['metresSafe']
        except:
            pass

        return metersSafe

    def metersUnsafes(self):
        metersUnsafe = 0
        try:
            metersUnsafe += self.segmentTemplate['metresUnsafe']
        except:
            pass

        return metersUnsafe
    
    def distances(self):
        distance = 0
        try:
            distance += self.segmentTemplate['metres']
        finally:
            return distance
        
def csv_parser(csv_path):
    try:
        df = pd.read_csv(csv_path)
        df = df.dropna()
    except Exception as e:
        print("Import error: " + str(e))

    return df

def deleteErrors(jsonData, tripid, startime):
    error = False
    path = 'tripgodata/' + str(tripid) + '-' + str(startime) + '.json'

    if 'error' in jsonData:
        os.remove(path)
        print("file removed.")
        error = True

    try:
        jsonData['groups']
    except:
        os.remove(path)
        print('file removed.')
        error = True
        return error

    return error

