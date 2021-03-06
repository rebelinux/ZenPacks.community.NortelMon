# ==============================================================================
# PassportConPortMap modeler plugin
#
# Zenoss community Zenpack for Avaya (Nortel) Passport Devices
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

__doc__="""PassportConPortMap maps rc2kCpuEthernetPortTable monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class PassportConPortMap(SnmpPlugin):
    """Map Nortel Passport Console Port table to model."""
    maptype = "PassportConPortMap"
    modname = "ZenPacks.community.NortelMon.PassportConPort"
    relname = "PassportConPort"
    

    snmpGetTableMaps = (
        GetTableMap('port',
		'.1.3.6.1.4.1.2272.1.100.2.1',
                    {
                        '.1': 'cpuethernetportindex',
                        '.2': 'cpuethernetportdescr',
                        '.5': 'ethernetportaddr',
                        '.6': 'cpuethernetportmask',
                        '.7': 'cpuethernetportgateway',
                        '.8': 'cpuethernetportnetwork',
                        '.15': 'portmgmtmacaddr',
                    }
                    ),
	)
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        ports = tabledata.get("port")
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not ports:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in ports.iteritems():
            try:
                om = self.objectMap(data)
                om.id = self.prepId("Mgmt Port")
                om.snmpindex = om.cpuethernetportindex
                om.portmgmtmacaddr = self.asmac(om.portmgmtmacaddr)
            except AttributeError:
                continue
            rm.append(om)
        return rm
