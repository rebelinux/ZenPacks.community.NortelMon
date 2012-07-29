# ===========================================================================
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
# ===========================================================================

__doc__= """Code Utils"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2012. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Globals import DTMLFile
from Globals import InitializeClass
import re

def devicename(self, ip):
    """try to get the remote device name, using the device ip"""
    try:
        remotedev = self.dmd.Devices.findDeviceByIdOrIp(ip)
        if remotedev.titleOrId():
            return remotedev.titleOrId()
        elif remotedev.title:
            return remotedev.title
        elif remotedev.id:
            return remotedev.id
        else:
            return ip
    except:
        return 'Device Not In Zenoss'

def fixip(self, ip):
    """Process Topology Table Malformed IP IDs"""
    find = ip.find('_')
    if find != -1:
        patern = ip[find:]
        newip = ip.strip(patern)
        return newip
    else:
        return ip

def ifix(self, int, ifindex):
    """Process the Interface name of Avaya Nortel Switches"""
    try:
        intname = int
        patern = 'ifc%s ' % ifindex
        if re.match(patern, intname):
            int = intname.strip(patern)
        name = int.strip('()')
        newname = name.replace('Slot', 'Unit')
        newname = newname.replace(':', '')
        return newname
    except AttributeError:
        return int

def findinterface(self, device, ints):
    """try to get the local interface link, using the interface name"""
    try:
        interfaces = []
        interfaces.append(device.os.interfaces._getOb(ints))
        for obj in interfaces:
            interface = obj.urlLink()
        return interface
    except:
        return ints

def getremotedeviceIP(self, mac):
    """try to get the remote device ip address, using the device mac address"""
    interface = getremoteinterface(mac)
    ipaddr = []
    for ips in interface.getIpAddressObjs():
        ipaddr = ips
    return ipaddr

def getremoteinterface(self, mac):
    """try to find the interfaces from the remote device, using its mac address"""
    try:
        interface = []
        for objects in self.dmd.ZenLinkManager.layer2_catalog(macaddress=mac):
            interfaces = objects.getObject()
            interface.append(interfaces)
        return interface
    except:
        return mac
