# ==============================================================================
# NortelMltStatus object class
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

__doc__="""NortelMltStatus object class"""
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

class NortelMltStatus(DeviceComponent, ManagedEntity):

    portal_type = meta_type = 'NortelMltStatus'
    
    nmltid = 0
    nmltname = ''
    nmltvlans = ''
    nmltenable = ''
    nmltstatus = ''

    _properties = (
        {'id':'nmltid', 'type':'int', 'mode':''},
        {'id':'nmltname', 'type':'string', 'mode':''},
        {'id':'nmltvlans', 'type':'string', 'mode':''},
        {'id':'nmltenable', 'type':'string', 'mode':''},
        {'id':'nmltstatus', 'type':'string', 'mode':''},
        )
    
    _relations = (
        ("NortelMltDevStatus", ToOne(ToManyCont,
            "ZenPacks.community.NortelMon.NortelDevice", "NortelMltStatus")),
        )


    factory_type_information = ( 
        { 
            'id'             : 'NortelMltStatus',
            'meta_type'      : 'NortelMltStatus',
            'description'    : """NortelMltStatus info""",
            'product'        : 'NortelMon',
            'immediate_view' : 'viewNortelMltStatus',
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
        return self.NortelMltDevStatus()
    
    def manage_deleteComponent(self, REQUEST=None):
        """Delete NortelMltStatus component takes from Jane Curry"""
        url = None
        if REQUEST is not None:
            url = self.device().NortelMltStatus.absolute_url()
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
    
InitializeClass(NortelMltStatus)
