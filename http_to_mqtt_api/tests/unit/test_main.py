"""
Test module for main
"""

import unittest
from unittest import mock
from unittest.mock import MagicMock

from main import call_zigbee, get_mqtt_client


class TestMain(unittest.TestCase):
    """
    Test class main
    """

    # Adjust the patch location to match where MQTTClient is imported from
    @mock.patch("main.MQTTClient")
    def test_get_mqtt_client(self, mock_mqtt_client):
        # Assuming your MQTTClient class is correctly mocked
        # and your get_mqtt_client function is properly decorated with @contextmanager

        instance = mock_mqtt_client.return_value
        instance.connect.return_value = None
        instance.disconnect.return_value = None

        # Now, use the get_mqtt_client() as intended
        with get_mqtt_client() as client:
            # Assertions can go here
            instance.connect.assert_called_once()

        # Assert disconnect was called after exiting the 'with' block
        instance.disconnect.assert_called_once()

    @mock.patch("main.get_mqtt_client")
    def test_call_zigbee(self, mock_mqtt_func):
        result = call_zigbee(
            topic="zigbee2mqtt/kitchen_window/", payload="ON", mqtt_client=mock_mqtt_func
        )
        self.assertEqual(
            mock_mqtt_func.publish.call_args.kwargs,
            {"topic": "zigbee2mqtt/kitchen_window/", "payload": "ON"},
        )
        self.assertEqual(result, {"topic": "zigbee2mqtt/kitchen_window/", "payload": "ON"})
