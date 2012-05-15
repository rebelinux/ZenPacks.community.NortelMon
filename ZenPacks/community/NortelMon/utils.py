# ==============================================================================
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

__doc__="""Code Utils"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Globals import DTMLFile
from Globals import InitializeClass

def findinterface(self, device, ints):
    try:
        int = []
        int.append(device.os.interfaces._getOb(ints))
        for obj in int:
            interface = obj.urlLink()
        return interface
    except:
        return ints
def localinterface(self, device, ints):
    return findinterface(self, device, ints)

def remoteswitch(self, ips):
    """try to get the remote device, using the management IP"""
    dev = self.dmd.Devices.findDeviceByIdOrIp(ips)
    if dev:
        if dev.urlLink() is None:
            return ips
        else:
            return dev.urlLink()
    else:
        return ips