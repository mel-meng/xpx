from unittest import TestCase
import xpx
import logging
import json



class TestReader(TestCase):
    def test_parse_xpx(self):
        f = './workspace/node_link_test.xpx'
        xpx_obj = xpx.parse_xpx(f)
        assert(xpx_obj['nodes']['Node1']['type']=='134')
        assert (xpx_obj['nodes']['Node1']['x'] == '269.097222222222')
        assert (xpx_obj['nodes']['Node2']['type'] == '134')
        assert (xpx_obj['nodes']['Node2']['y'] == '-233.506944444444')

        assert (xpx_obj['links']['Link1']['type'] == '136')
        assert (xpx_obj['links']['Link1']['from'] == 'Node1')

        assert (xpx_obj['links']['Link2']['type'] == '136')
        assert (xpx_obj['links']['Link2']['to'] == 'Node3')

        with open('./workspace/node_link_test.json', 'w') as o:
            json.dump(xpx_obj, o, indent=4)

