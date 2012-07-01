# ==============================================================================
# PassportMltStatus object class
#
# Zenoss community Zenpack for Avaya (Nortel) Nortel Devices
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

__doc__="""PassportMltStatus object class"""
__author__ = "Jonathan Colon"
__copyright__ = "(C) Copyright Jonathan Colon. 2011. All Rights Reserved."
__license__ = "GPL"
__version__ = "1.0.0"

from Globals import DTMLFile
from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity

class PassportMltStatus(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'PassportMltStatus'
    
    mltid = 0
    mltname = ''
    mlttype = ''
    mltruntype = ''
    mltvlans = ''
    mltenable = ''
    mltstatus = ''

    _properties = (
        {'id':'mltid', 'type':'int', 'mode':''},
        {'id':'mltname', 'type':'string', 'mode':''},
        {'id':'mlttype', 'type':'string', 'mode':''},
        {'id':'mltruntype', 'type':'string', 'mode':''},
        {'id':'mltvlans', 'type':'string', 'mode':''},
        {'id':'mltenable', 'type':'string', 'mode':''},
        {'id':'mltstatus', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("PassportMltDevStatus", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.PassportDevice", "PassportMltStatus")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'PassportMltStatus',
            'meta_type'      : 'PassportMltStatus',
            'description'    : """PassportMltStatus info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewPassportMltStatus',
            'actions'        :
            ( 
                { 'id'            : 'viewHistory'
                , 'name'          : 'Modifications'
                , 'action'        : 'viewHistory'
                , 'permissions'   : (ZEN_VIEW, )
                },
            )
          },
        ) 

    def viewName(self):
        """Pretty version human readable version of this object"""
        return self.id
    
    titleOrId = name = viewName


    def device(self):
        return self.PassportMltDevStatus()
    
    def manage_deleteComponent(self, REQUEST=None):
        """Delete PassportMltStatus component takes from Jane Curry"""
        url = None
        if REQUEST is not None:
            url = self.device().PassportMltStatus.absolute_url()
        self.getPrimaryParent()._delObject(self.id)

        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(url)
    
    def getRRDTemplates(self):
        """
        Return the RRD Templates list
        """
        templates = []
        for tname in [self.__class__.__name__]:
            templ = self.getRRDTemplateByName(tname)
            if templ: templates.append(templ)
        return templates
    
InitializeClass(PassportMltStatus)
