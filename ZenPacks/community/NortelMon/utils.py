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
__copyright__ = "(C) Copyright Jonathan Colon. 2012. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Globals import DTMLFile
from Globals import InitializeClass

def ifix(self, int):         
    s = int.find('(') 
    n = int.find(')')
    if n < 0 or s < 0:
        return int 
    else:
        fint = int[s+1:n] 
        fint1 = fint.replace('Slot', 'Unit')
        fint2 = fint1.replace(':', '')
        return fint2

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
        
        