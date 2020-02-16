"""LICENSE
Copyright 2020 Hermann Krumrey <hermann@krumreyh.com>

This file is part of fat-ffipd.

fat-ffipd is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fat-ffipd is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fat-ffipd.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

from fat_ffipd.test.TestFramework import _TestFramework
from fat_ffipd.bg_tasks import bg_tasks


class TestBackgroundTasks(_TestFramework):
    """
    Tests background tasks
    """

    def test_im_alive(self):
        """
        Tests the I'm alive background task
        :return: None
        """
        im_alive_task = bg_tasks["im_alive"][1]
        im_alive_task()
