"""Tests for
https://www.codewars.com/kata/ad2070-help-lorimar-troubleshoot-his-robots-ultrasonic-distance-analysis."""

import pytest


TEST = [
    ([  ('Distance:', 116.28, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 117.1, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 123.96, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 117.17, 'Meters', 'Sensor 5 malfunction =>lorimar')
        ], (118.6275, 3.5779),
    ([  ('Distance:', 295.68, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 294.78, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 298.21, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 294.84, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 296.54, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 133.84, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 294.41, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 294.82, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 134.61, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 294.86, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 170.88, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 170.87, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 170.47, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 135.5, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 170.9, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 170.08, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 171.36, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 170.08, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 170.92, 'Meters', 'Sensor 5 malfunction =>lorimar'),
        ('Distance:', 170.88, 'Meters', 'Sensor 5 malfunction =>lorimar')
        ], (215.2265, 68.4014)),
]


@pytest.mark.parametrize("sensor_data, result", TEST)
def test_sensor_analysis(sensor_data, result):
    """Test that function returns correct mean from distance and stddev."""
    from mean_stddev_of_distance import sensor_analysis
    assert sensor_analysis(ll) == result
