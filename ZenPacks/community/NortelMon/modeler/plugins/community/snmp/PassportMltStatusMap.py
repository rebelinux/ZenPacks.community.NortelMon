# ==============================================================================
# PassportMltStatusMap modeler plugin
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

__doc__="""PassportMltStatusMap maps rcMltTable monitoring entries"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
import binascii

class PassportMltStatusMap(SnmpPlugin):
    """Map Mlt Status table to model."""
    maptype = "PassportMltStatusMap"
    modname = "ZenPacks.community.NortelMon.PassportMltStatus"
    relname = "PassportMltStatus"
    

    snmpGetTableMaps = (
        GetTableMap('mlt',
        '.1.3.6.1.4.1.2272.1.17.10.1',
                    {
                        '.1': 'mltid',
                        '.2': 'mltname',
                        '.6': 'mltvlans',
                        '.7': 'mltstatus',
                        '.8': 'mltenable',
                        '.12': 'mlttype',
                        '.14': 'mltruntype',
                    }
                    ),
    )
    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        mlts = tabledata.get("mlt")
        
        # Debug: print data retrieved from device.
        log.debug( "Get data = %s", getdata )
        log.debug( "Table data = %s", tabledata )

        # If no data retrieved return nothing.        
        if not mlts:
            log.warn( 'No data collected from %s for the %s plugin', device.id, self.name() )
            return
        rm = self.relMap()
        def spt(string, size):
            return [string[i:i+size] for i in range(0, len(string), size)]
        for oid, data in mlts.iteritems():
            try:
                om = self.objectMap(data)
                om.id = self.prepId(om.mltname)
                om.snmpindex = om.mltid
                if om.mlttype not in self.mltype.keys():
                    om.mlttype = 4
                om.mlttype = self.mltype[om.mlttype]
                if om.mltruntype not in self.mltyperun.keys():
                    om.mltruntype = 4
                om.mltruntype = self.mltyperun[om.mltruntype]
                if om.mltenable not in self.mltena.keys():
                    om.mltenable = 4
                om.mltenable = self.mltena[om.mltenable]
                om.mltvlans = binascii.hexlify(om.mltvlans)
                vlanid = spt(om.mltvlans, 4)
                list = []
                for port in vlanid:
                    list.append(int(port, 16))
                    om.mltvlans = list
            except AttributeError:
                continue
            rm.append(om)
        return rm

    mltype = { 1: 'Normal MLT',
                       2: 'IST MLT',
                       3: 'S-MLT',
                       4: 'Other',
                     }
    mltyperun = { 1: 'Normal MLT',
                       2: 'IST MLT',
                       3: 'S-MLT',
                       4: 'Other',
                     }
    mltena = { 1: 'True',
                       2: 'False',
                       3: 'Other',
                     }