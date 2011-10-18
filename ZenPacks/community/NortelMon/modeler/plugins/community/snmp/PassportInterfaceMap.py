# ==============================================================================
# PassportInterfaceMap modeler plugin
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

__doc__ = """PassportInterfaceMap

    Extends the standard InterfaceMap to use the ifAlias as the interface's
    name instead of the ifDescr. This can be useful when many interfaces on
    the same device have the same ifDescr."""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from copy import deepcopy
from Products.DataCollector.plugins.zenoss.snmp.InterfaceMap \
    import InterfaceMap
from Products.DataCollector.plugins.CollectorPlugin import GetTableMap

class PassportInterfaceMap(InterfaceMap):
    
    snmpGetTableMaps = InterfaceMap.baseSnmpGetTableMaps + (
        # Extended interface information.
        GetTableMap('ifalias', '.1.3.6.1.2.1.31.1.1.1',
                {'.1' : 'ifName',
                 '.6' : 'ifHCInOctets',
                 '.7' : 'ifHCInUcastPkts',
                 '.15': 'highSpeed'}
        ),
        GetTableMap('ifdesc', '.1.3.6.1.4.1.2272.1.4.10.1.1',
                {'.1' : 'ifindex',
                 '.35'  : 'description'}
        ),
    )
    
    def __init__(self, *args, **kwargs):
        # save proxy to self as superclass, to guard against future
        # reload of plugin module changing imported classes (making
        # future super calls fail due to class mismatch)
        self.as_super = super(PassportInterfaceMap,self)
        self.as_super.__init__(*args, **kwargs)

    def process(self, device, results, log):
        """
        Pre-process the IF-MIB ifXTable to use the ifAlias as the interface's
        name instead of the ifDescr.
        """
        if 'ifalias' in results[1] and 'iftable' in results[1]:
            for a_idx, alias in results[1]['ifalias'].items():
                for i_idx, iface in results[1]['iftable'].items():
                    if a_idx == i_idx:
                        results[1]['iftable'][i_idx]['id'] = alias['ifName']
                        
        if 'ifdesc' in results[1] and 'iftable' in results[1]:
            for a_idx, desc in results[1]['ifdesc'].items():
                for i_idx, iface in results[1]['iftable'].items():
                    if desc['ifindex'] == iface['ifindex']:
                        results[1]['ifalias'][i_idx]['description'] = desc['description']
        
        return self.as_super.process(device, results, log)
