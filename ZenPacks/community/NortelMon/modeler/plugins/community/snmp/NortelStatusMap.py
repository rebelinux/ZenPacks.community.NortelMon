# ==============================================================================
# NortelStatusMap modeler plugin
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

__doc__="""NortelStatusMap maps rcChasStatusTable monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
import textwrap

class NortelStatusMap(SnmpPlugin):
    """Map Nortel Status table to model."""
    maptype = "NortelStatusMap"
    modname = "ZenPacks.community.NortelMon.NortelStatus"
    relname = "NortelStatus"
    

    snmpGetTableMaps = (
        GetTableMap('stat',
        '.1.3.6.1.4.1.45.1.6.3',
                    {
                        '.7.1.1.5.5': 'tmpvalue',
                        '.8.1.1.2.3': 'index',
                        '.8.1.1.5.3': 'cpuusage',
                        '.8.1.1.12.3': 'totalmem',
                        '.8.1.1.13.3': 'availablemem',
                    }
                    ),
    )
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        status = tabledata.get("stat")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not status:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in status.iteritems():
            try:
                om = self.objectMap(data)
                index = om.index
                sindex = textwrap.wrap(str(index),1)
                om.id = self.prepId("Switch_%s" % sindex[0])
                om.tmpvalue = str(int(om.tmpvalue / 2)) + 'C'
                om.usedmem = str(om.totalmem - om.availablemem) + 'MB'
                om.totalmem = str(om.totalmem) + 'MB'
                om.availablemem = str(om.availablemem) + 'MB'
                om.cpuusage = str(om.cpuusage) + '%'
                om.snmpindex = om.index
            except AttributeError:
                continue
            rm.append(om)
        return rm
