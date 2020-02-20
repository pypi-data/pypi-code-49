from lifelines import WeibullAFTFitter
from lifelines.datasets import load_rossi
import pandas as pd

class WeibullAFTSuite:

    def setup(self):
        self.wf = WeibullAFTFitter(fit_intercept=True)
        self.data = load_rossi()
        self.data20 = pd.concat([load_rossi()] * 20)

    def time_wf_on_rossi(self):
        self.wf.fit(self.data, 'week', 'arrest')


    def time_wf_on_20_rossi(self):
        self.wf.fit(self.data20, 'week', 'arrest')

