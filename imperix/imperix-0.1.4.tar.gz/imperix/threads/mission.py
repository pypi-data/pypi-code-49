# Developed by Aptus Engineering, Inc. <https://aptus.aero>
# See LICENSE.md file in project root directory

REFRESH_INTERVAL_SECONDS = 3.0

import time

# Mission Update handler
def missionUpdateHandler(active, missionUpdateCallback, apiURL="https://api.imperix.ai/"):
    '''
    Connection handling task - to be started as a thread.

    Parameters
    ----------
    @param active [bool] - should thread be running?
    @param missionUpdateCallback [func(mission)] - callback function to be called when node's mission is updated.
    @param apiURL [str] - Imperix Commander API URL
    '''
    
    while active: # Keep thread running
        
        try:
            # TODO - Get mission from API
            pass

        except:
            pass

        time.sleep(REFRESH_INTERVAL_SECONDS)