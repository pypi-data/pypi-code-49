from zipfile import ZipFile
import json
import magic
from datetime import datetime
from jezdzenka.classes.Type import Type


class Pkpass:
    def __init__(self, pkpass):
        self.file = pkpass
        self.fileStruct = {
            "info": "pass.json",
            "sig": "signature",
            "manifest": "manifest.json"
        }
        self.copied_data = self.read()

    def is_valid(self):
        return "application/zip" in magic.from_file(self.file, mime=True)

    def get_type(self):
        if self.copied_data.get("boardingPass"):
            return Type.TRANSIT, "boardingPass"
        if self.copied_data.get("coupon"):
            return Type.COUPON, "coupon"
        if self.copied_data.get("eventTicket"):
            return Type.EVENT, "eventTicket"
        if self.copied_data.get("storeCard"):
            return Type.CARD, "storeCard"
        return Type.OTHER, "genericPass"

    def get_special_values(self):
        return {
            "boardingPass": ['departure', 'arrival', 'boardingTime', 'departurePlatform', 'departureStationName',
                             'carNumber', 'destinationStationName', 'flightNumber', 'destinationAirportName',
                             'departureTerminal', 'departureGate'],
            "eventTicket": ['eventName', 'venueName', 'venueEntrance', 'runtime']
        }.get(self.get_type()[1], [])

    def read(self):
        if self.is_valid():
            with ZipFile(self.file, 'r') as zipfile:
                data = zipfile.read(self.fileStruct.get("info"))
                return json.loads(data)
        return {}

    def regular_data(self):
        return {'id': self.copied_data.get("serialNumber"), 'organization': self.copied_data.get("organizationName"),
                'relevant_date': datetime.fromisoformat(self.copied_data.get("relevantDate")),
                'colour': '#%02x%02x%02x' % eval(self.copied_data.get("backgroundColor").strip("rgb")[1:-1]),
                'type': self.get_type()[0]}


class Special:
    def __init__(self, copied_data, type):
        self.copied_data = copied_data
        self.type = type

    def special_data(self, data, variables):
        for variable in variables:
            if self.copied_data.get(variable):
                data[variable] = self.copied_data.get(variable)
            elif self.get_primary_field_by_key(variable, type):
                data[variable] = self.get_primary_field_by_key(variable, type)
            elif self.get_auxiliary_field_by_key(variable, type):
                data[variable] = self.get_auxiliary_field_by_key(variable, type)
            elif self.get_secondary_field_by_key(variable, type):
                data[variable] = self.get_secondary_field_by_key(variable, type)
            elif self.get_back_field_by_key(variable, type):
                data[variable] = self.get_back_field_by_key(variable, type)

        return data

    def get_primary_field_by_key(self, key, type):
        data = self.copied_data.get(self.type).get("primaryFields")
        for item in data:
            if item.get("key") == key:
                return item.get("value")
        return False

    def get_auxiliary_field_by_key(self, key, type):
        data = self.copied_data.get(self.type).get("auxiliaryFields")
        for item in data:
            if item.get("key") == key:
                return item.get("value")
        return False

    def get_secondary_field_by_key(self, key, type):
        data = self.copied_data.get(self.type).get("secondaryFields")
        for item in data:
            if item.get("key") == key:
                return item.get("value")
        return False

    def get_back_field_by_key(self, key, type):
        data = self.copied_data.get(self.type).get("backFields")
        for item in data:
            if item.get("key") == key:
                return item.get("value")
        return False