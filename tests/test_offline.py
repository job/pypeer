import sys, argparse
import os
from jnpr.junos import Device
from lxml import etree

sys.path.append('/home/andy/src/pypeer/lib')
sys.path.append('/Users/andy/src/pypeer/lib')
from pypeer.ConfigDictionary import ConfigDictionary
from pypeer.RouteData import RouteData

def test_username():
	config = ConfigDictionary('/Users/andy/src/pypeer/etc/example.ini')
	thisusername = config.username()
	assert thisusername == 'exampleuser' 

def test_can_find_rtr1():
	config = ConfigDictionary('/Users/andy/src/pypeer/etc/example.ini')
	assert config.get_router_ip('rtr1') == '91.194.69.4'

def test_can_read_prefix_from_route_object():
	resultxml = etree.fromstring(open('/Users/andy/src/pypeer/tests/test_data/bgp_route.xml').read())
	route = RouteData(resultxml.find('.//rt'))
	assert route.prefix() == '199.87.242.0/24'