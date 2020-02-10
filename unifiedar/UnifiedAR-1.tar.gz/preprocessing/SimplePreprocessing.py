from general.utils import Data
from preprocessing.preprocessing_abstract import Preprocessing


class SimplePreprocessing(Preprocessing):

    # remove invalid changes in stream
    def process(self, datasetdscr, dataset):
        removekeys = []
        for sid, info in datasetdscr.sensor_desc.iterrows():
            last = {}
            last['value'] = -1000
            if (info.Nominal | info.OnChange):
                continue
            xs  = dataset.s_events.loc[dataset.s_events.SID == sid]
            min = xs.value.min()
            max = xs.value.max()
            #print(min, max, max-min)
            invalid_changes = (max-min)*0.1
            for key, event in xs.iterrows():
                invalid_changes = event['value']*.1
                if abs(last['value']-event['value']) < invalid_changes:
                    #print (event)
                    removekeys.append(key)
                    continue
                last = event
            # print(removekeys)
        d = Data(dataset.name)
        d.s_events = dataset.s_events.drop(removekeys)
        d.a_events = dataset.a_events
        d.s_event_list = d.s_events.values
        d.acts = dataset.acts
        d.act_map = dataset.act_map
        return d
