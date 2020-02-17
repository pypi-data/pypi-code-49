from Wms.RemotingImplementation import Inbound,General
from Wms.RemotingObjects.ShippingLayers import ProcessShipmentArgs

printer = 0
processShipmentArgs = ProcessShipmentArgs()
processShipmentArgs.DocumentPrinter = printer
General.GetLabelPrinterOfCurrentUser = 0
