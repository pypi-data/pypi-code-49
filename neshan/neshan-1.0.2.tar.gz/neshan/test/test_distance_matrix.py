#
# Copyright 2014 Google Inc. All rights reserved.
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#

"""Tests for the distance matrix module."""

from datetime import datetime
import time

import responses

import neshan
import neshan.test as _test


class DistanceMatrixTest(_test.TestCase):

    def setUp(self):
        self.key = 'service.8AwKYt4Tov5II9uvbK5BkiZZ1TMHAM4JnBtm4yft'
        self.client = neshan.Client(self.key)

    @responses.activate
    def test_basic_params(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v1/distance-matrix',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')

        origins = ["Perth, Australia", "Sydney, Australia",
                   "Melbourne, Australia", "Adelaide, Australia",
                   "Brisbane, Australia", "Darwin, Australia",
                   "Hobart, Australia", "Canberra, Australia"]
        destinations = ["Uluru, Australia",
                        "Kakadu, Australia",
                        "Blue Mountains, Australia",
                        "Bungle Bungles, Australia",
                        "The Pinnacles, Australia"]

        matrix = self.client.distance_matrix(origins, destinations)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v1/distance-matrix?'
                            'origins=Perth%%2C+Australia%%7CSydney%%2C+'
                            'Australia%%7CMelbourne%%2C+Australia%%7CAdelaide%%2C+'
                            'Australia%%7CBrisbane%%2C+Australia%%7CDarwin%%2C+'
                            'Australia%%7CHobart%%2C+Australia%%7CCanberra%%2C+Australia&'
                            'destinations=Uluru%%2C+Australia%%7CKakadu%%2C+Australia%%7C'
                            'Blue+Mountains%%2C+Australia%%7CBungle+Bungles%%2C+Australia'
                            '%%7CThe+Pinnacles%%2C+Australia',
                            responses.calls[0].request.url)

    @responses.activate
    def test_mixed_params(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v1/distance-matrix',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')

        origins = ["Bobcaygeon ON", [41.43206, -81.38992]]
        destinations = [(43.012486, -83.6964149),
                        {"lat": 42.8863855, "lng": -78.8781627}]

        matrix = self.client.distance_matrix(origins, destinations)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v1/distance-matrix?'
                            'origins=Bobcaygeon+ON%%7C41.43206%%2C-81.38992&'
                            'destinations=43.012486%%2C-83.6964149%%7C42.8863855%%2C'
                            '-78.8781627',
                            responses.calls[0].request.url)

    @responses.activate
    def test_all_params(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v1/distance-matrix',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')

        origins = ["Perth, Australia", "Sydney, Australia",
                   "Melbourne, Australia", "Adelaide, Australia",
                   "Brisbane, Australia", "Darwin, Australia",
                   "Hobart, Australia", "Canberra, Australia"]
        destinations = ["Uluru, Australia",
                        "Kakadu, Australia",
                        "Blue Mountains, Australia",
                        "Bungle Bungles, Australia",
                        "The Pinnacles, Australia"]

        now = datetime.now()
        matrix = self.client.distance_matrix(origins, destinations)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v1/distance-matrix?'
                            'origins=Perth%%2C+Australia%%7CSydney%%2C+Australia%%7C'
                            'Melbourne%%2C+Australia%%7CAdelaide%%2C+Australia%%7C'
                            'Brisbane%%2C+Australia%%7CDarwin%%2C+Australia%%7CHobart%%2C+'
                            'Australia%%7CCanberra%%2C+Australia&'
                            'destinations=Uluru%%2C+Australia%%7CKakadu%%2C+Australia%%7C'
                            'Blue+Mountains%%2C+Australia%%7CBungle+Bungles%%2C+Australia'
                            '%%7CThe+Pinnacles%%2C+Australia' %
                            (time.mktime(now.timetuple())),
                            responses.calls[0].request.url)


    @responses.activate
    def test_lang_param(self):
        responses.add(responses.GET,
                      'https://api.neshan.org/v1/distance-matrix',
                      body='{"status":"OK","rows":[]}',
                      status=200,
                      content_type='application/json')

        origins = ["Vancouver BC", "Seattle"]
        destinations = ["San Francisco", "Victoria BC"]

        matrix = self.client.distance_matrix(origins, destinations)

        self.assertEqual(1, len(responses.calls))
        self.assertURLEqual('https://api.neshan.org/v1/distance-matrix?'
                            'origins=Vancouver+BC%%7CSeattle&'
                            'destinations=San+Francisco%%7CVictoria+BC',
                            responses.calls[0].request.url)
