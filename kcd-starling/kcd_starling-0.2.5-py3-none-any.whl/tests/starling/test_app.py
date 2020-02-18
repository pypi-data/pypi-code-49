import pytest

from starling.app import Scrapper
from starling.blueprint_action import BlueprintAction
from starling.blueprint_scrapper import BlueprintScrapper
from starling.exception import RetryTaskExitError
from starling.types import ScrapperData, TaskData, MessageData


class MyScrapper(BlueprintScrapper):
    def tasks(self, action):
        if action == 'tests.starling.test_app.MyAction1':
            return [
                TaskData(action=action, criteria={'from': '20191001', 'to': '20191031'}),
                TaskData(action=action, criteria={'from': '20191101', 'to': '20191130'})
            ]
        else:
            return [TaskData(action=action)]

    @property
    def actions(self):
        return [
            'tests.starling.test_app.MyAction1',
            'tests.starling.test_app.MyAction2',
            'tests.starling.test_app.MyAction3'
        ]

    def authenticate(self):
        pass


class MyValidScrapper(BlueprintScrapper):
    @property
    def actions(self):
        return [
            'tests.starling.test_app.MyAction4'
        ]

    def authenticate(self):
        pass


class MyInvalidScrapper(BlueprintScrapper):
    @property
    def actions(self):
        return [
            'tests.starling.test_app.MyAction5'
        ]

    def authenticate(self):
        pass


class MyAttributeErrorScrapper(BlueprintScrapper):
    @property
    def actions(self):
        return [
            'tests.starling.test_app.MyMyAction1'
        ]

    def authenticate(self):
        pass


class MyAction1(BlueprintAction):
    def fetch(self):
        self.scrapper_data.broadcast_variables['v1'] = 1
        return self.scrapper_data.candidate

    def interval(self):
        return 0


class MyAction2(BlueprintAction):
    def fetch(self):
        if self.scrapper_data.broadcast_variables.get('v1') is None:
            raise RetryTaskExitError('v1 is required')
        return self.scrapper_data.candidate


class MyAction3(BlueprintAction):
    def fetch(self):
        return self.scrapper_data.candidate


class MyAction4(BlueprintAction):
    def fetch(self):
        raise RetryTaskExitError('invalid id', {'is_valid': True})


class MyAction5(BlueprintAction):
    def fetch(self):
        raise RetryTaskExitError('ip blocked')


def test_scrapper():
    res = Scrapper.run(MyScrapper(ScrapperData('place', {'place_id': '123123'}, MessageData(contents='contents'))))
    assert len(res.actions) == 3
    assert len(res.actions['tests.starling.test_app.MyAction1']) == 2
    assert len(res.actions['tests.starling.test_app.MyAction2']) == 1
    assert res.actions['tests.starling.test_app.MyAction1'][0].criteria['from'] == '20191001'
    assert res.actions['tests.starling.test_app.MyAction1'][1].criteria['from'] == '20191101'


def test_valid_scrapper():
    res = Scrapper.run(MyValidScrapper(ScrapperData('place', {'place_id': '123123'}, MessageData(contents='contents'))))
    assert len(res.actions) == 1
    assert res.is_valid is True


def test_invalid_scrapper():
    res = Scrapper.run(
        MyInvalidScrapper(ScrapperData('place', {'place_id': '123123'}, MessageData(contents='contents'))))
    assert len(res.actions) == 1
    assert res.is_valid is False


def test_scrapper_actions():
    res = Scrapper.run(MyScrapper(ScrapperData('place', {'place_id': '123123'}, MessageData(contents='contents')),
                                  actions=[
                                      'tests.starling.test_app.MyAction1',
                                      'tests.starling.test_app.MyAction3'
                                  ]))
    assert len(res.actions) == 2


def test_scrapper_with_attribute_error():
    with pytest.raises(AttributeError) as e:
        Scrapper.run(
            MyAttributeErrorScrapper(ScrapperData('place', {'place_id': '123123'}, MessageData(contents='contents'))))

    assert "module" in str(e.value)
