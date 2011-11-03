import Globals
import os.path
from Products.ZenModel.ZenPack import ZenPackBase

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

class ZenPack(ZenPackBase):
    """ ZenPack loader
"""
    def install(self, app):
        ZenPackBase.install(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()

    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()

    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects)
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()