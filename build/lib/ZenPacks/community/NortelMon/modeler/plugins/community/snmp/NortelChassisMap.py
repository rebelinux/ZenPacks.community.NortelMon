# ==============================================================================
# NortelChassisMap modeler plugin
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

__doc__="""NortelChassisMap maps RC-CHASSIS-MIB monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap

class NortelChassisMap(SnmpPlugin):
    """Map Nortel Topology Table to model."""
    maptype = "NortelChassisMap"
    modname = "ZenPacks.community.NortelMon.NortelChassis"
    relname = "NortelChassis"

    snmpGetTableMaps = (
        GetTableMap('chas',
		'1.3.6.1.4.1.45.1.6.3.3.1.1',
                    {
                        '.2.8': 'unitindex',
                        '.4.8': 'chasstype',
                        '.5.8': 'desc',
                        '.6.8': 'version',
                        '.7.8': 'sernum',
                        '.9.8': 'admstatus',
                        '.10.8': 'operstatus',
                        '.17.8': 'totalport',
		    }
		),
	)

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        chass = tabledata.get("chas")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not chass:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in chass.iteritems():
            try:
                om = self.objectMap(data)
                om.id = self.prepId("Switch_%s" % om.unitindex)
                om.unitnumber = om.id
                om.snmpindex = oid.strip('.')
                if om.operstatus not in self.opstatus.keys():
                    om.operstatus = 1
                om.operstatus = self.opstatus[om.operstatus]
                if om.admstatus not in self.adstatus.keys():
                    om.admstatus = 1
                om.admstatus = self.adstatus[om.admstatus]
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
    
    adstatus = { 1: 'Other',
                       2: 'NotAvail',
                       3: 'Disabled',
                       4: 'Enable',
                       5: 'Reset',
                       6: 'Test',
                     }