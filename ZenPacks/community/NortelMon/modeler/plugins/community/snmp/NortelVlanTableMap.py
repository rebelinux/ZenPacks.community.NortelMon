# ==============================================================================
# NortelVlanTableMap modeler plugin
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

__doc__="""NortelVlanTableMap maps rcVlanTable monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
import binascii
class NortelVlanTableMap(SnmpPlugin):
    """Map Nortel Vlan table to model."""
    maptype = "NortelVlanTableMap"
    modname = "ZenPacks.community.NortelMon.NortelVlanTable"
    relname = "NortelVlanTable"
    

    snmpGetTableMaps = (
        GetTableMap('vlan',
        '.1.3.6.1.4.1.2272.1.3.2.1',
                    {
                        '.1': 'vlanid',
                        '.2': 'vlanname',
                        '.9': 'vlanstgid',
                        '.10': 'vlantype',
                        '.11': 'vlanportmembers',
                        '.19': 'vlanmac',
                    }
                    ),
    )
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        vlans = tabledata.get("vlan")
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not vlans:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        for oid, data in vlans.iteritems():
            try:
                om = self.objectMap(data)
                om.id = self.prepId(om.vlanname)
                om.snmpindex = om.vlanid
                if om.vlantype not in self.vtype.keys():
                    om.vlantype = 0 
                om.vlantype = self.vtype[om.vlantype]
                om.vlanmac = self.asmac(om.vlanmac)
                om.vlanportmembers = binascii.hexlify(om.vlanportmembers)
            except AttributeError:
                continue
            rm.append(om)
        return rm


    vtype = { 0: 'Unknown',
                       1: 'By Port',
                       2: 'By Subnet',
                       3: 'By Protocol',
                       4: 'By Src Mac',
                       5: 'By Dst Mac',
                       6: 'By Stacked Vlan',
                       7: 'By IDS Vlan',
                     }

