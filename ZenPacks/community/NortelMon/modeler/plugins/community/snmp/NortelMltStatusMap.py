# ==============================================================================
# NortelMltStatusMap modeler plugin
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

__doc__="""NortelMltStatusMap maps rcMltTable monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
import binascii, re

class NortelMltStatusMap(SnmpPlugin):
    """Map Mlt Status table to model."""
    maptype = "NortelMltStatusMap"
    modname = "ZenPacks.community.NortelMon.NortelMltStatuss"
    relname = "NortelMltStatus"
    

    snmpGetTableMaps = (
        GetTableMap('nmlt',
        '.1.3.6.1.4.1.2272.1.17.10.1',
                    {
                        '.1': 'nmltid',
                        '.2': 'nmltname',
                        '.6': 'nmltvlans',
                        '.7': 'nmltstatus',
                        '.8': 'nmltenable',
                    }
                    ),
    )
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        nmlts = tabledata.get("nmlt")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not nmlts:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        def spt(string, size):
            return [string[i:i+size] for i in range(0, len(string), size)]
        for oid, data in nmlts.iteritems():
            try:
                om = self.objectMap(data)
                string = 'TRUNK'
                if re.search(om.nmltname, string):
                    om.id = self.prepId("TRUNK_%s" % om.nmltid)
                else:
                    om.id = self.prepId(om.nmltname)
                om.snmpindex = om.nmltid
                if om.nmltenable == 2:
                    om.clear()
                if om.nmltenable not in self.nmltena.keys():
                    om.nmltenable = 3
                om.nmltenable = self.nmltena[om.nmltenable]
                if om.nmltstatus not in self.nmltstat.keys():
                    om.nmltstatus = 3
                om.nmltstatus = self.nmltstat[om.nmltstatus]
                om.nmltvlans = binascii.hexlify(om.nmltvlans)
                vlanid = spt(om.nmltvlans, 4)
                list = []
                for port in vlanid:
                    list.append(int(port, 16))
                    om.nmltvlans = list
            except AttributeError:
                continue
            rm.append(om)
        return rm
    
    nmltena = { 1: 'True',
                       2: 'False',
                       3: 'Other',
                     }
    nmltstat = { 1: 'UP',
                       2: 'DOWN',
                       3: 'Other',
                     }