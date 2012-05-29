# ==============================================================================
# NortelConDevice modeler plugin
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

__doc__="""NortelConDevice maps Bridge-Mibs monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2012. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from ZenPacks.community.NortelMon.utils import ifix

class NortelConDeviceMap(SnmpPlugin):
    """Map Nortel Topology Table to model."""
    maptype = "NortelConDeviceMap"
    modname = "ZenPacks.community.NortelMon.NortelConDevice"
    relname = "NortelConDevice"
    

    snmpGetTableMaps = (
        GetTableMap('bridge',
		'.1.3.6.1.2.1',
                    {
                        '.17.1.4.1.1': 'baseport',
                        '.17.1.4.1.2': 'baseportindex',
                        '.2.2.1.1': 'ifindex',
                        '.31.1.1.1.1': 'ifname',
                        '.17.4.3.1.1': 'macaddr',
                        '.17.4.3.1.2': 'fdbport',
                        '.17.2.7': 'rootport',               
		    }
		),
	)

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        bridges = tabledata.get("bridge")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not bridges:
            log.warn( 'No data collected for the %s plugin', self.name() )
            return
        
        rm = self.relMap()
        for oid, data in bridges.iteritems():
            try:
                om = self.objectMap(data)
                if om.fdbport == om.rootport:
                    om.clear()
                else:
                    if om.baseportindex == om.ifindex:
                        om.ifname = ifix(self, om.ifname)
                        om.id = self.prepId(om.ifname)
                        om.macaddr = self.asmac(om.macaddr)
                        om.localint = om.ifname
                    else:
                        continue
            except AttributeError:
                continue
            rm.append(om)
        return rm