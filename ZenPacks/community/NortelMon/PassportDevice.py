# ==============================================================================
# PassportDevice object class
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

__doc__="""PassportDevice object class"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from Products.ZenModel.ZenossSecurity import *
from copy import deepcopy

class PassportDevice(Device):
    "A Nortel Device"

    chashwrevision = 0
    chasnumports = 0
    chastype = ''
    totalmem = 0
    chasbasemac = ''

    _properties = Device._properties + (
        {'id':'chashwrevision', 'type':'int', 'mode':''},
        {'id':'chasnumports', 'type':'int', 'mode':''},
        {'id':'chastype', 'type':'string', 'mode':''},
        {'id':'totalmem', 'type':'int', 'mode':''},
        {'id':'chasbasemac', 'type':'string', 'mode':''},
	)

    _relations = Device._relations + (
        ('PassportPower', ToManyCont(ToOne, 'ZenPacks.community.NortelMon.PassportPower', 'PassportDevPower')),
        ('PassportFan', ToManyCont(ToOne, 'ZenPacks.community.NortelMon.PassportFan', 'PassportDevFan')),
        ('PassportConPort', ToManyCont(ToOne, 'ZenPacks.community.NortelMon.PassportConPort', 'PassportDevConPort')),
        ('PassportTopology', ToManyCont(ToOne, 'ZenPacks.community.NortelMon.PassportTopology', 'PassportDevTopology')),
        ('PassportVlanTable', ToManyCont(ToOne, 'ZenPacks.community.NortelMon.PassportVlanTable', 'PassportDevVlanTable')),
        ('PassportVlanPort', ToManyCont(ToOne, 'ZenPacks.community.NortelMon.PassportVlanPort', 'PassportDevVlanPort')),
        ('PassportCardTable', ToManyCont(ToOne, 'ZenPacks.community.NortelMon.PassportCardTable', 'PassportDevCardTable')),
        )

    factory_type_information = deepcopy(Device.factory_type_information)
    factory_type_information[0]['actions'] += (
            { 'id'              : 'PassportDeviceInfo'
            , 'name'            : 'Nortel Information'
            , 'action'          : 'PassportDeviceDetail'
            , 'permissions'     : (ZEN_VIEW, ) },
            )


    def __init__(self, *args, **kw):
        Device.__init__(self, *args, **kw)
        self.buildRelations()

InitializeClass(PassportDevice)
