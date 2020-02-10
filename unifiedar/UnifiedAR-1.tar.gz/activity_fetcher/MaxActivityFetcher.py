from activity_fetcher.activity_fetcher_abstract import AbstractActivityFetcher

class MaxActivityFetcher(AbstractActivityFetcher):
    def getActivity(self,dataset,window):
        start=window.iat[0,1].value#.first.time
        end=window.iat[window.shape[0]-1,1].value
        acts=(dataset.a_events_tree[start:end])

        if(len(acts)==0):
            return 0
        pacts=[]
        nacts=[]
        for x in acts:
            pacts.append((min(x.end,end)-max(x.begin,start))/(end-start))
            nacts.append(x.data)
        #np.argmax(pacts)
        return nacts[np.argmax(pacts)].Activity
        