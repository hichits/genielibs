import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.flow.configure import configure_flow_monitor_cache_entry


class TestConfigureFlowMonitorCacheEntry(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          LG-PK:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9300
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['LG-PK']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_flow_monitor_cache_entry(self):
        result = configure_flow_monitor_cache_entry(self.device, 'fl_mon_Po', 'flow_Po', 300, 2000)
        expected_output = None
        self.assertEqual(result, expected_output)
