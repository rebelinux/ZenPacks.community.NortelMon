# ==============================================================================
# NortelDeviceMapLegacy modeler plugin
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

__doc__ = """NortelDeviceMapLegacy
Use Nortel Oid to determine hardware model + serial number as well
as OS information.
"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap
from Products.DataCollector.plugins.DataMaps import MultiArgs
import re

class NortelDeviceMapLegacy(SnmpPlugin):
    """Map mib elements from Nortel mib to get hw and os products.
    """

    maptype = "NortelDeviceMapLegacy"

    snmpGetMap = GetMap({
        '.1.3.6.1.4.1.45.1.6.3.1.6.0' : 'setHWSerialNumber',
        '.1.3.6.1.4.1.45.1.6.3.1.2.0' : 'setHWProductKey',
        '.1.3.6.1.4.1.45.1.6.3.1.5.0' : 'setOSProductKey',
        })



    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        if getdata['setHWProductKey'] is None: return None
        if getdata['setOSProductKey'] is None: return None
        om = self.objectMap(getdata)
        om.setOSProductKey = 'Software Version ' + om.setOSProductKey.strip('v')
        om.setHWProductKey = om.setHWProductKey[0:om.setHWProductKey.find('HW') - 1]
        om.setHWProductKey = MultiArgs(om.setHWProductKey, "Nortel")
        om.setOSProductKey = MultiArgs(om.setOSProductKey, "Nortel")
        return om
