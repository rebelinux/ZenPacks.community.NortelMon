# ==============================================================================
# PassportVlanPortMap modeler plugin
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

__doc__="""PassportVlanPortMap maps rcVlanPortTable monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
import binascii
class PassportVlanPortMap(SnmpPlugin):
    """Map Nortel Passport Vlan Port to model."""
    maptype = "PassportVlanPortMap"
    modname = "ZenPacks.community.NortelMon.PassportVlanPort"
    relname = "PassportVlanPort"
    

    snmpGetTableMaps = (
        GetTableMap('vport',
		'.1.3.6.1',
                    {
                        '.4.1.2272.1.3.3.1.1': 'vlanportindex',
                        '.4.1.2272.1.3.3.1.3': 'vlanportids',
                        '.4.1.2272.1.3.3.1.4': 'vlanporttype',
                        '.4.1.2272.1.3.3.1.7': 'vlanpvid',
                        '.4.1.2272.1.3.3.1.8': 'vlantag',
                        '.2.1.31.1.1.1.1' : 'intname',
                        '.4.1.2272.1.4.10.1.1.35': 'description',
                        }
                    ),
	)
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        vports = tabledata.get("vport")
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not vports:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        def spt(string, size):
            return [string[i:i+size] for i in range(0, len(string), size)]
        for oid, data in vports.iteritems():
            try:
                om = self.objectMap(data)
                om.id = self.prepId(om.intname)
                om.snmpindex = om.vlanportindex
                om.vlanporttype = self.porttype[om.vlanporttype]
                om.vlantag = self.tagtype[om.vlantag]
                om.vlanportindex = om.id
                om.vlanportids = binascii.hexlify(om.vlanportids)
                vlanid = spt(om.vlanportids, 4)
                list = []
                for port in vlanid:
                    list.append(int(port, 16))
                    om.vlanportids = list
            except AttributeError:
                continue
            rm.append(om)
        return rm


    porttype = { 1: 'Access',
                       2: 'Trunk',
                     }
    tagtype = { 1: 'Yes',
                       2: 'No',
                     }
