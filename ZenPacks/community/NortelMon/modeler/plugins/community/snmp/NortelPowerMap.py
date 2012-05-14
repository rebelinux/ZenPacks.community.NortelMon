# ==============================================================================
# NortelPowerMap modeler plugin
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

__doc__="""NortelPowerMap maps PowerSupply monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
import textwrap

class NortelPowerMap(SnmpPlugin):
    """Map Nortel power table to model."""
    maptype = "NortelPowerMap"
    modname = "ZenPacks.community.NortelMon.NortelPower"
    relname = "NortelPower"
    

    snmpGetTableMaps = (
        GetTableMap('power',
        '.1.3.6.1.4.1.45.1.6.3.3.1.1',
                    {
                        '.2.4': 'powerindex',
                        '.5.4': 'powerdesc',
                        '.10.4': 'powerstatus',
                    }
                    ),
    )
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        powers = tabledata.get("power")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not powers:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in powers.iteritems():
            try:
                om = self.objectMap(data)
                index = om.powerindex + 1
                sindex = textwrap.wrap(str(index),1)
                om.id = self.prepId("Switch-%s PowerSupply-%s" % tuple(sindex))
                if om.powerstatus not in self.opstatus.keys():
                    om.powerstatus = 1
                om.powerstatus = self.opstatus[om.powerstatus]
                om.snmpindex = oid
                om.powerindex = om.id
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
