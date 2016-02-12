#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from unittest.mock import *

from alarm import Alarm
from sensor import Sensor


class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_too_low_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(15))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_too_high_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(22))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_normal_pressure_doesnt_sound_alarm(self):
        alarm = Alarm(sensor=TestSensor(18))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_with_pressure_ok_with_mock_fw(self):
        test_sensor = Mock(Sensor)
        test_sensor.sample_pressure.return_value = 18
        alarm = Alarm(test_sensor)
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_with_too_high_pressure(self):
        with patch('alarm.Sensor') as test_sensor_class:
            test_sensor_instance = Mock()
            test_sensor_instance.sample_pressure.return_value = 22
            test_sensor_class.return_value = test_sensor_instance
            alarm = Alarm()
            alarm.check()
            self.assertTrue(alarm.is_alarm_on)

    @patch("alarm.Sensor")
    def test_check_with_too_low_pressure(self, test_sensor_class):
        with patch('alarm.Sensor') as test_sensor_class:
            test_sensor_instance = Mock()
            test_sensor_instance.sample_pressure.return_value = 15
            test_sensor_class.return_value = test_sensor_instance
            alarm = Alarm()
            alarm.check()
            self.assertTrue(alarm.is_alarm_on)


class TestSensor:

    def __init__(self, pressure):
        self.pressure = pressure

    def sample_pressure(self):
        return 15
