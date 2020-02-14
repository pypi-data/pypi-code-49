from unittest import TestCase
from logzero import logger
from zeroinger.time.dateutils import DateUtils
from datetime import datetime


class TestDateUtils(TestCase):
    def test_now(self):
        now_act = DateUtils.now()
        now_gold = datetime.now()
        str_act = now_act.strftime('%Y-%m-%d %H:%M:%S')
        str_gold = now_gold.strftime('%Y-%m-%d %H:%M:%S')

        self.assertEqual(str_act, str_gold, "获取当前时间错误")

    def test_date2str(self):
        now = datetime.now().replace(2019, 12, 2, 3, 4, 5, 678000)
        self.assertEqual('2019-12-02 03:04:05.678', DateUtils.date2str(now))
        self.assertEqual('20191202 03:04:05 678', DateUtils.date2str(now, "YYYYMMDD HH:mm:ss SSS"))

    def test_str2date(self):
        self.assertEqual('2019-12-02 03:04:05.678', DateUtils.date2str(DateUtils.str2date('2019-12-02 03:04:05.678')))
        pass
        # self.fail()

    def test_of(self):
        a = DateUtils.of(2019, 1, 2, 3, 4, 5, 6, 7)
        self.assertEqual('2019-01-02 03:04:05.006', DateUtils.date2str(a))
        b = DateUtils.of(None, None, None, None, 4, None, 6, 7)
        c = datetime.now().replace(minute=4, microsecond=6000)
        self.assertEqual(DateUtils.date2str(c), DateUtils.date2str(b))
        logger.info('{}-{}'.format(DateUtils.date2str(c), DateUtils.date2str(b)))

        # self.fail()

    def test_set(self):
        pass
        # self.fail()

    def test_add_time(self):
        a = DateUtils.of(2019, 1, 2, 3, 4, 5, 6, 7)
        b = DateUtils.add_time(a, -1, 1, 1, 1, 1, 1, 1, 1)
        logger.info('test_add_time|{}|{}'.format(DateUtils.date2str(a), DateUtils.date2str(b)))
        self.assertEqual('2018-02-03 04:05:06.007', DateUtils.date2str(b))

    def test_time_delta_with_diff_unit(self):
        start = DateUtils.of(2019, 1, 2, 3, 4, 5, 6, 7)
        end = DateUtils.of(2020, 2, 2, 4, 4, 6, 7, 8)
        logger.info('时间差{}'.format(DateUtils.time_delta_with_diff_unit(end, start)))
        # self.fail()

        # def test_time_diff_by(self):
        #     self.fail()
