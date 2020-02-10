import requests
print("KOT1 1.0.0")

class Weather:
    """ Creates a Weather object getting an apikey as input and either a city name:
    >>> weather1 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Madrid")
    or latitude and longitude coordinates
    >>> weather = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = 41.1, lon = 4.1)
    Use the proper method to get weather for different hours.
    """
    def __init__(self, apikey,
        city = None, lat = None, lon = None):
        if city is not None and lat is None and lon is None:
            self.url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=metric" 
            r = requests.get(self.url)
            self.data = r.json()
        elif city is None and lat is not None and lon is not None:
            self.url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=metric" 
            r = requests.get(self.url)
            self.data = r.json()
        else:
            print("Either a city name, or a pair of latitude and longitude coordinates.")
        
    def next_12h(self):
        """Return every 3-hour data for the next 12 hours as a dict.
        """
        
        if self.data['cod'] == "200":
       
            data_12h = self.data['list'][:5]
                
            return data_12h
        else:
            raise ValueError(self.data['message'])
        
    def next_12h_simplified(self):
        """Returns date, temperature (C), and sky condition every 3 hours
           for the next 12 hours in a simplified string format.
        """
        
        if self.data['cod'] == "200":
       
            new = []
            for i in self.data['list'][:5]:
                 result = f"{i['dt_txt']}, {i['main']['temp']}, {i['weather'][0]['description']}"
                 new.append(result)
                
            return ".\n".join(new)
        else:
            print(self.url)
            raise ValueError(self.data['message'])
        
    def __repr__(self):
        return self.data

if __name__ == "__main__":
    weather1 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", city = "Madrid")
    #weather2 = Weather(apikey = "26631f0f41b95fb9f5ac0df9a8f43c92", lat = 41.1, lon = 4.1)
    #print(weather1.next_12h())
    print(weather1.next_12h_simplified())
    #print(weather2.next_12h())
    #print(weather2.next_12h_simplified())

    
