# ==============================================================================
# PassportDeviceMap modeler plugin
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

__doc__ = """PassportDeviceMap
Use Nortel Passport Oid to determine hardware model + serial number as well
as OS information."""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
import string
class PassportDeviceMap(SnmpPlugin):
    """Map mib elements from Nortel mib to get hw and os products.
    """
    modname = "ZenPacks.community.NortelMon.PassportDeviceMap"
    relname = "PassportDeviceMap"
    maptype = "PassportDeviceMap"

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.2272.1.4.2.0' : 'setHWSerialNumber',
        '.1.3.6.1.2.1.1.1.0' : 'setHWProductKey',
        '.1.3.6.1.2.1.1.9.1.3.1' : 'setOSProductKey',
        '.1.3.6.1.4.1.2272.1.1.46.0' : 'totalmem',
        '.1.3.6.1.4.1.2272.1.4.1.0' : 'chastype',
        '.1.3.6.1.4.1.2272.1.4.5.0' : 'chasnumports',
        '.1.3.6.1.4.1.2272.1.4.3.0' : 'chashwrevision',
        '.1.3.6.1.4.1.2272.1.100.1.5.0' : 'chasbasemac',
        })

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        if getdata['setHWProductKey'] is None: return None
        om = self.objectMap(getdata)
        maps = []
        if om.setHWProductKey:
            chassis = om.setHWProductKey
            hw = chassis.split()
            om.setHWProductKey = 'Passport ' + hw[0]
            om.setOSProductKey = 'Software Version ' + hw[1].strip('()')
            om.setOSProductKey = MultiArgs(om.setOSProductKey, "Nortel")
            om.setHWProductKey = MultiArgs(om.setHWProductKey, "Nortel")
            if (om.chastype not in self.chassistypeMap.keys()):
                om.chastype = 1
            om.chastype = self.chassistypeMap[om.chastype]
            if om.chasbasemac:
                om.chasbasemac = self.asmac(om.chasbasemac)
            maps.append(om)
            return maps
        return maps

    chassistypeMap = { 1: 'unknown chassis',
                       2: '3  slot chassis',
                       6: '4  slot chassis',
                       7: '3  slot chassis',
                       8: '8  slot chassis',
                       9: '2  slot chassis (seahawk)',
                       280887558: '6  slot chassis (raptillion)',
                       280887562: '10 slot chassis (raptillion)',
                       1623064842: '10 slot Central Office Chassis',
                       280887555: '3  slot chassis (raptillion)',
                       1086197761: '1 slot 12 port (cobra)',
                       1086201857: '1 slot 24 port (cobra)',
                       1086210049: '1 slot 52 port (cobra)',
                       1354629382: '6 slot 8300 POE chassis',
                       1354629386: '10 slot 8300 POE chassis',
                     }
