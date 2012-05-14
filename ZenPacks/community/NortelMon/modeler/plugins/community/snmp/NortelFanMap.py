# ==============================================================================
# NortelFanMap modeler plugin
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

__doc__="""NortelFanMap maps rcChasFanTable monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
import textwrap

class NortelFanMap(SnmpPlugin):
    """Map Nortel Fan table to model."""
    maptype = "NortelFanMap"
    modname = "ZenPacks.community.NortelMon.NortelFan"
    relname = "NortelFan"
    

    snmpGetTableMaps = (
        GetTableMap('fan',
        '.1.3.6.1.4.1.45.1.6.3.3.1.1',
                    {
                        '.2.6': 'fanindex',
                        '.5.6': 'fandesc',
                        '.10.6': 'fanstatus',
                    }
                    ),
    )
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        fans = tabledata.get("fan")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not fans:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in fans.iteritems():
            try:
                om = self.objectMap(data)
                index = om.fanindex + 1
                sindex = textwrap.wrap(str(index),1)
                om.id = self.prepId("Switch-%s Fan-%s" % tuple(sindex))
                if om.fanstatus not in self.opstatus.keys():
                    om.fanstatus = 1
                om.fanstatus = self.opstatus[om.fanstatus]
                om.snmpindex = oid
                om.fanindex = om.id
            except AttributeError:
                continue
            rm.append(om)
        return rm

    opstatus = { 1: 'Other',
                       2: 'NotAvail',
                       3: 'Removed',
                       4: 'Disabled',
                       5: 'Normal',
                       6: 'ResetInProg',
                       7: 'Testing',
                       8: 'Warning',
                       9: 'NonFatalErr',
                       10: 'FatalErr',
                       11: 'NotConfig',
                       12: 'Obsoleted',
                     }
