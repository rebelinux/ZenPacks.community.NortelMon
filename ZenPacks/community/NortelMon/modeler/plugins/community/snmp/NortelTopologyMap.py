# ==============================================================================
# NortelTopologyMap modeler plugin
#
# Zenoss community Zenpack for Avaya (Nortel) Devices
# version: 1.0
#
# (C) Copyright Jonathan Colon. All Rights Reserved.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# ==============================================================================

__doc__="""NortelTopologyMap maps SONMP monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class NortelTopologyMap(SnmpPlugin):
    """Map Nortel Topology Table to model."""
    maptype = "NortelTopologyMap"
    modname = "ZenPacks.community.NortelMon.NortelTopology"
    relname = "NortelTopology"
    

    snmpGetTableMaps = (
        GetTableMap('topo',
		'.1.3.6.1',
                    {
                        '.4.1.45.1.6.13.2.1.1.1': 'unit',
                        '.4.1.45.1.6.13.2.1.1.2': 'port',
                        '.4.1.45.1.6.13.2.1.1.3': 'ipaddr',
                        '.4.1.45.1.6.13.2.1.1.5': 'macaddr',
                        '.4.1.45.1.6.13.2.1.1.6': 'chassistype',
                        '.4.1.45.1.6.13.2.1.1.8': 'localseg',
                        '.4.1.45.1.6.13.2.1.1.9': 'curstate',
		    }
		),
        GetTableMap('deviceip',
                '.1.3.6.1',
                    {
                        '.2.1.4.20.1.1': 'ip',
                    }
		),
	)

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        topos = tabledata.get("topo")
        device = tabledata.get("deviceip")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not topos:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        if not device:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in topos.iteritems():
            try:
                om = self.objectMap(data)
                om.id = self.prepId(om.ipaddr)
                om.macaddr = self.asmac(om.macaddr)
                om.localseg = self.local[om.localseg]
                om.curstate = self.state[om.curstate]
                if om.chassistype not in self.type.keys():
                    om.chassistype = 1
                om.chassistype = self.type[om.chassistype]
                if device.has_key(om.ipaddr):
                    om.clear()
            except AttributeError:
                continue
            rm.append(om)
        return rm

    local = { 1: 'Yes',
                       2: 'No',
                     }

    state = { 1: 'Topology Change',
                       2: 'Heartbeat',
                       3: 'New',
                     }
    type = { 1: 'Unknown',
                       2: '3000',
                       3: '3030',
                       4: '2310',
                       5: '2810',
                       6: '2912',
                       7: '2914',
                       8: '271x',
                       9: '2813',
                       10: '2814',
                       11: '2915',
                       12: '5000',
                       13: '2813SA',
                       14: '2814SA',
                       16: '810M',
                       17: '5005',
                       18: 'Alcatel Ethernet',
                       20: '2715SA',
                       21: '2486',
                       22: '28000 serie',
                       23: '28000 serie',
                       24: '5DN00x series',
                       25: 'BayStack Ethernet',
                       26: '23100 series',
                       27: '100Base-T Hub',
                       28: '3000 Fast Ethernet',
                       29: 'Orion switch',
                       31: 'DDS',
                       32: 'Centillion',
                       33: 'Centillion',
                       34: 'Centillion',
                       35: 'BayStack 301',
                       36: 'BayStack TokenRing Hub',
                       37: 'FVC Multimedia Switch',
                       38: 'Switch Node',
                       39: 'BayStack 302 Switch',
                       40: 'BayStack 350 Switch',
                       41: 'BayStack 150 Ethernet Hub',
                       42: 'Centillion 50N switch',
                       43: 'Centillion 50T switch',
                       44: 'BayStack 300 Switches',
                       45: 'BayStack 200 Ethernet Hub',
                       46: 'BayStack 250 Ethernet Hub',
                       48: 'BayStack 450 Switches',
                       49: 'BayStack 410 Switches',
                       50: 'Passport 1200 L3 Switch',
                       51: 'Passport 1250 L3 Switch',
                       52: 'Passport 1100 L3 Switch',
                       53: 'Passport 1150 L3 Switch',
                       54: 'Passport 1050 L3 Switch',
                       55: 'Passport 1051 L3 Switch',
                       56: 'Passport 8610 L3 Switch',
                       57: 'Passport 8606 L3 Switch',
                       58: 'Passport 8010',
                       59: 'Passport 8006',
                       60: 'BayStack 670 wap',
                       61: 'Passport 740',
                       62: 'Passport 750',
                       63: 'Passport 790',
                       64: 'BPS 2000',
                       65: 'Passport 8110 Switch',
                       66: 'Passport 8106 Switch',
                       67: 'BayStack 3580 Gig Switch',
                       68: 'BayStack 10 PSU',
                       69: 'BayStack 420 Switch',
                       70: 'OPTera Metro 1200 ESM',
                       71: 'OPTera 8010co',
                       72: 'OPTera 8610co Switch',
                       73: 'OPTera 8110co Switch',
                       74: 'OPTera 8003',
                       75: 'OPTera 8603 Switch',
                       76: 'OPTera 8103 Switch',
                       77: 'BayStack 380 Switch',
                       78: 'Ethernet Switch 470-48T',
                       79: 'OPTera Metro 1450 ESM',
                       80: 'OPTera Metro 1400 ESM',
                       81: 'Alteon Switch Family',
                       82: 'Ethernet Switch 460-24T-PWR',
                       83: 'OPTera Metro 8010 OPM L2 Switch',
                       84: 'OPTera Metro 8010co OPM L2 Switch',
                       85: 'OPTera Metro 8006 OPM L2 Switch',
                       86: 'OPTera Metro 8003 OPM L2 Switch',
                       87: 'Alteon 180e',
                       88: 'Alteon AD3',
                       89: 'Alteon 184',
                       90: 'Alteon AD4',
                       91: 'Passport 1424 L3 switch',
                       92: 'Passport 1648 L3 switch',
                       93: 'Passport 1612 L3 switch',
                       94: 'Passport 1624 L3 switch',
                       95: 'BayStack 380-24F Fiber 1000 Switch',
                       96: 'ERS 5510-24T',
                       97: 'ERS 5510-48T',
                       98: 'Ethernet Switch 470-24T',
                       99: 'Nortel Networks Wireless LAN Access Point 2220',
                       100: 'Passport RBS 2402 L3 switch',
                       101: 'Alteon Application Switch 2424',
                       102: 'Alteon Application Switch 2224',
                       103: 'Alteon Application Switch 2208',
                       104: 'Alteon Application Switch 2216',
                       105: 'Alteon Application Switch 3408',
                       106: 'Alteon Application Switch 3416',
                       107: 'Nortel Networks Wireless LAN SecuritySwitch 2250',
                       108: 'Ethernet Switch 425-48T',
                       109: 'Ethernet Switch 425-24T',
                       110: 'Nortel Networks Wireless LAN Access Point 2221',
                       111: 'Nortel Metro Ethernet Service Unit 24-T SPF switch',
                       112: 'Nortel Metro Ethernet Service Unit 24-T LX DC switch',
                       113: 'Passport 8300 10-slot chassis',
                       114: 'Passport 8300 6-slot chassis',
                       115: 'ERS 5520-24T-PWR',
                       116: 'ERS 5520-48T-PWR',
                       117: 'Nortel Networks VPN Gateway 3050',
                       118: 'Alteon SSL 310 10/100',
                       119: 'Alteon SSL 310 10/100 Fiber',
                       120: 'Alteon SSL 310 10/100 FIPS',
                       121: 'Alteon SSL 410 10/100/1000',
                       122: 'Alteon SSL 410 10/100/1000 Fiber',
                       123: 'Alteon Application Switch 2424-SSL',
                       124: 'Ethernet Switch 325-24T',
                       125: 'Ethernet Switch 325-24G',
                       126: 'Nortel Networks Wireless LAN Access Point 2225',
                       127: 'Nortel Networks Wireless LAN SecuritySwitch 2270',
                       128: 'Ethernet Switch 470-24T-PWR',
                       129: 'Ethernet Switch 470-48T-PWR',
                       130: 'ERS 5530-24TFD',
                       131: 'Ethernet Switch 3510-24T',
                       132: 'Nortel Metro Ethernet Service Unit 12G AC L3 switch',
                       133: 'Nortel Metro Ethernet Service Unit 12G DC L3 switch',
                       134: 'Nortel Secure Access Switch',
                       135: 'Nortel Networks VPN Gateway 3070',
                       136: 'DDSOPTera Metro 3500',
                       137: 'SMB BES 1010 24T',
                       138: 'SMB BES 1010 48T',
                       139: 'SMB BES 1020 24T PWR',
                       140: 'SMB BES 1020 48T PWR',
                       141: 'SMB BES 2010 24T',
                       142: 'SMB BES 2010 48T',
                       143: 'SMB BES 2020 24T PWR',
                       144: 'SMB BES 2020 48T PWR',
                       145: 'SMB BES 110 24T',
                       146: 'SMB BES 110 48T',
                       147: 'SMB BES 120 24T PWR',
                       148: 'SMB BES 120 48T PWR',
                       149: 'SMB BES 210 24T',
                       150: 'SMB BES 210 48T',
                       151: 'SMB BES 220 24T PWR',
                       152: 'SMB BES 220 48T PWR',
                       153: 'OME 6500',
                       154: 'ERS 4548GT',
                       155: 'ERS 4548GT-PWR',
                       156: 'ERS 4550T',
                       157: 'ERS 4550T-PWR',
                       158: 'ERS 4526FX',
                       159: 'ERS 2500-26T',
                       160: 'ERS 2500-26T-PWR',
                       161: 'ERS 2500-50T',
                       162: 'ERS 2500-50T-PWR',
                       163: 'ERS 4526T',
                       164: 'ERS 4526T-PWR',
                       165: 'ERS 4524GT',
                       166: 'ERS 4526GTX',
                       167: 'ERS 4526GTX-PWR',
                       168: 'MetroNext',
                       169: 'MERS 4600',
                       170: 'ESU 1860T',
                       171: 'ESU 1880S',
                       172: 'ERS 5698TFD-PWR',
                       173: 'ERS 5698TFD',
                       174: 'ERS 5650TD-PWR',
                       175: 'ERS 5650TD',
                       176: 'ERS 5632FD',
                       177: 'Nortel Virtual Services Switch 5000',
                       178: 'ESU 1860V',
                       179: 'ESU 1860S',
                       180: 'ESU 1860B',
                       181: 'Metro ERS 64000',
                       182: 'Metro ERS 8611co',
                       183: 'Metro ERS 8603-R',
                       184: 'ERS 4524GT-PWR',
                       185: 'ERS 6628XSGT',
                       186: 'ERS 6632XTS',
                       187: 'MESU 2400',
                       188: 'WC 8180',
                       190: 'ERS 8003-R',
                       191: 'Ethernet Routing 8803r L3 switch',
                       192: 'Ethernet Routing 8806 L3 switch',
                       193: 'Ethernet Routing 8810 L3 switch',
                       194: 'Ethernet Routing 8810r L3 switch',
                     }

