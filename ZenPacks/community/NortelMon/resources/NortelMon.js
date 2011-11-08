(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.PassportPowerPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportPower',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'powersupplystatus'},
                {name: 'powersupplystatusText'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'powersupplystatus',
                dataIndex: 'powersupplystatus',
                header: _t('PowerSupply Status'),
                sortable: true,
                renderer: Zenoss.render.severity,
                width: 120
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{
                id: 'powersupplystatusText',
                dataIndex: 'powersupplystatusText',
                header: _t('Status'),
                sortable: true,
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.PassportPowerPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportPowerPanel', ZC.PassportPowerPanel);
ZC.registerName('PassportPower', _t('Power Supply'), _t('Power Supplies'));

ZC.PassportFanPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportFan',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'fanstatus'},
                {name: 'fanstatusText'},
                {name: 'fantemp'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'fanstatus',
                dataIndex: 'fanstatus',
                header: _t('Fan Status'),
                sortable: true,
                renderer: Zenoss.render.severity,
                width: 120,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name')
            },{
                id: 'fantemp',
                dataIndex: 'fantemp',
                header: _t('Temperature'),
                sortable: true,
                width: 120,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored')
            },{
                id: 'fanstatusText',
                dataIndex: 'fanstatusText',
                header: _t('Status'),
                sortable: true,
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.PassportFanPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportFanPanel', ZC.PassportFanPanel);
ZC.registerName('PassportFan', _t('Fan'), _t('Fans'));

ZC.PassportConPortPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportConPort',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'cpuethernetportdescr'},
                {name: 'ethernetportaddr'},
                {name: 'cpuethernetportmask'},
                {name: 'cpuethernetportnetwork'},
                {name: 'cpuethernetportgateway'},
                {name: 'portmgmtmacaddr'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
            },{

                id: 'cpuethernetportdescr',
                dataIndex: 'cpuethernetportdescr',
                header: _t('Description'),
                sortable: true,
                width: 120,
            },{
                id: 'ethernetportaddr',
                dataIndex: 'ethernetportaddr',
                header: _t('IP Address'),
                sortable: true,
                width: 120,
            },{
                id: 'cpuethernetportmask',
                dataIndex: 'cpuethernetportmask',
                header: _t('NetMask'),
                sortable: true,
            },{
                id: 'cpuethernetportgateway',
                dataIndex: 'cpuethernetportgateway',
                header: _t('Gateway'),
                sortable: true,
            },{
                id: 'cpuethernetportnetwork',
                dataIndex: 'cpuethernetportnetwork',
                header: _t('Network Filter'),
                sortable: true,
            },{
                id: 'portmgmtmacaddr',
                dataIndex: 'portmgmtmacaddr',
                header: _t('Mgmt Mac Address'),
                sortable: true,
                width: 120,
            }]
        });
        ZC.PassportConPortPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportConPortPanel', ZC.PassportConPortPanel);
ZC.registerName('PassportConPort', _t('Console Port'), _t('Console Ports'));

ZC.PassportTopologyPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportTopology',
            autoExpandColumn: 'sysname',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'localint'},
                {name: 'macaddr'},
                {name: 'chassistype'},
                {name: 'localseg'},
                {name: 'sysname'},
                {name: 'curstate'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'sysname',
                dataIndex: 'sysname',
                header: _t('Remote Device'),
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('IP Address'),
			},{
                id: 'macaddr',
                dataIndex: 'macaddr',
                header: _t('Mac Address'),
                sortable: true,
                width: 120,
			},{
                id: 'localint',
                dataIndex: 'localint',
                header: _t('Local Interface'),
                sortable: true,
                width: 120,
			},{
                id: 'chassistype',
                dataIndex: 'chassistype',
                header: _t('Chassis Type'),
                sortable: true,
                width: 160,
			},{
                id: 'localseg',
                dataIndex: 'localseg',
                header: _t('Local Segment'),
                sortable: true,
			},{
                id: 'curstate',
                dataIndex: 'curstate',
                header: _t('State'),
                sortable: true,
                width: 120,
            }]
        });
        ZC.PassportTopologyPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportTopologyPanel', ZC.PassportTopologyPanel);
ZC.registerName('PassportTopology', _t('Topology Table'), _t('Topology Tables'));

ZC.PassportVlanTablePanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportVlanTable',
            autoExpandColumn: 'vlanportmembers',
            sortInfo: {
                field: 'vlanid',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'vlanid'},
                {name: 'vlanmac'},
                {name: 'vlantype'},
                {name: 'vlanname'},
                {name: 'vlanstgid'},
                {name: 'vlanportmembers'},		
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 160,
			},{
                id: 'vlanid',
                dataIndex: 'vlanid',
                header: _t('Vlan ID'),
                sortable: true,
            },{
                id: 'vlanportmembers',
                dataIndex: 'vlanportmembers',
                header: _t('Port Members'),
                sortable: true,
			},{
                id: 'vlantype',
                dataIndex: 'vlantype',
                header: _t('Type'),
                sortable: true,
                width: 120,
            },{
                id: 'vlanmac',
                dataIndex: 'vlanmac',
                header: _t('Mac Address'),
                sortable: true,
                width: 160,
			},{
                id: 'vlanstgid',
                dataIndex: 'vlanstgid',
                header: _t('STG Id'),
                sortable: true,
                width: 120,
            }]
        });
        ZC.PassportVlanTablePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportVlanTablePanel', ZC.PassportVlanTablePanel);
ZC.registerName('PassportVlanTable', _t('Vlan Table'), _t('Vlan Tables'));

ZC.PassportVlanPortPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportVlanPort',
            autoExpandColumn: 'vlanportids',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'vlanportids'},
                {name: 'vlanporttype'},
                {name: 'vlanpvid'},
                {name: 'vlantag'},		
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 120,
			},{
                id: 'vlanportids',
                dataIndex: 'vlanportids',
                header: _t('Vlan Members'),
                sortable: true,
			},{
                id: 'vlanporttype',
                dataIndex: 'vlanporttype',
                header: _t('Port Type'),
                sortable: true,
                width: 120,
            },{
                id: 'vlanpvid',
                dataIndex: 'vlanpvid',
                header: _t('PvId'),
                sortable: true,
                width: 160,
			},{
                id: 'vlantag',
                dataIndex: 'vlantag',
                header: _t('Vlan Tag'),
                sortable: true,
            }]
        });
        ZC.PassportVlanPortPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportVlanPortPanel', ZC.PassportVlanPortPanel);
ZC.registerName('PassportVlanPort', _t('Ports Table'), _t('Ports Tables'));

ZC.PassportCardTablePanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'PassportCardTable',
            autoExpandColumn: 'description',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'cardtype'},
                {name: 'description'},
                {name: 'serialnumber'},
                {name: 'hwversion'},	
                {name: 'opstatus'},
                {name: 'admstatus'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 120,
			},{
                id: 'cardtype',
                dataIndex: 'cardtype',
                header: _t('Model'),
                sortable: true,
                width: 160,
			},{
                id: 'description',
                dataIndex: 'description',
                header: _t('Description'),
                sortable: true,
                width: 160,
            },{
                id: 'serialnumber',
                dataIndex: 'serialnumber',
                header: _t('Serial Number'),
                sortable: true,
                width: 160,
            },{
                id: 'admstatus',
                dataIndex: 'admstatus',
                header: _t('Admin Status'),
                sortable: true,
            },{
                id: 'opstatus',
                dataIndex: 'opstatus',
                header: _t('Oper Status'),
                sortable: true,
			},{
                id: 'hwversion',
                dataIndex: 'hwversion',
                header: _t('HW Version'),
                sortable: true,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.PassportCardTablePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('PassportCardTablePanel', ZC.PassportCardTablePanel);
ZC.registerName('PassportCardTable', _t('Card Table'), _t('Cards Tables'));

ZC.NortelTopologyPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelTopology',
            autoExpandColumn: 'sysname',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'unit'},
                {name: 'port'},
                {name: 'macaddr'},
                {name: 'chassistype'},
                {name: 'localseg'},
                {name: 'sysname'},
                {name: 'curstate'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'sysname',
                dataIndex: 'sysname',
                header: _t('Remote Device'),
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('IP Address'),
            },{
                id: 'macaddr',
                dataIndex: 'macaddr',
                header: _t('Mac Address'),
                sortable: true,
                width: 120,
            },{
                id: 'unit',
                dataIndex: 'unit',
                header: _t('Unit'),
                sortable: true,
            },{
                id: 'port',
                dataIndex: 'port',
                header: _t('Port'),
                sortable: true,
            },{
                id: 'chassistype',
                dataIndex: 'chassistype',
                header: _t('Chassis Type'),
                sortable: true,
                width: 160,
            },{
                id: 'localseg',
                dataIndex: 'localseg',
                header: _t('Local Segment'),
                sortable: true,
            },{
                id: 'curstate',
                dataIndex: 'curstate',
                header: _t('State'),
                sortable: true,
                width: 120,
            },{
                id: 'monitor',
                dataIndex: 'monitor',
                header: _t('Monitored')
            }]
        });
        ZC.NortelTopologyPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelTopologyPanel', ZC.NortelTopologyPanel);
ZC.registerName('NortelTopology', _t('Topology Table'), _t('Topology Table'));

ZC.NortelChassisPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelChassis',
            autoExpandColumn: 'desc',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'name'},
                {name: 'status'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'totalport'},
                {name: 'desc'},
                {name: 'chasstype'},
                {name: 'sernum'},
                {name: 'admstatus'},
                {name: 'operstatus'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Stack Members'),
            },{
                id: 'chasstype',
                dataIndex: 'chasstype',
                header: _t('Chassis Type'),
                sortable: true,
            },{
                id: 'desc',
                dataIndex: 'desc',
                header: _t('Description'),
                sortable: true,
            },{
                id: 'sernum',
                dataIndex: 'sernum',
                header: _t('Serial Number'),
                sortable: true,
                width: 120,            
            },{
                id: 'admstatus',
                dataIndex: 'admstatus',
                header: _t('Adm Status'),
                sortable: true,
            },{
                id: 'operstatus',
                dataIndex: 'operstatus',
                header: _t('Oper Status'),
                sortable: true,
            },{
                id: 'totalport',
                dataIndex: 'totalport',
                header: _t('Total Ports'),
                sortable: true,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
            },{ 
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                width: 72,
                renderer: Zenoss.render.locking_icons,
            }]
        });
        ZC.NortelChassisPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelChassisPanel', ZC.NortelChassisPanel);
ZC.registerName('NortelChassis', _t('Stack Status'), _t('Stack Status'));

ZC.NortelVlanTablePanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelVlanTable',
            autoExpandColumn: 'vlanportmembers',
            sortInfo: {
                field: 'vlanid',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'vlanid'},
                {name: 'vlanmac'},
                {name: 'vlantype'},
                {name: 'vlanname'},
                {name: 'vlanstgid'},
                {name: 'vlanportmembers'},		
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 160,
			},{
                id: 'vlanid',
                dataIndex: 'vlanid',
                header: _t('Vlan ID'),
                sortable: true,
            },{
                id: 'vlanportmembers',
                dataIndex: 'vlanportmembers',
                header: _t('Port Members'),
                sortable: true,
			},{
                id: 'vlantype',
                dataIndex: 'vlantype',
                header: _t('Type'),
                sortable: true,
                width: 120,
            },{
                id: 'vlanmac',
                dataIndex: 'vlanmac',
                header: _t('Mac Address'),
                sortable: true,
                width: 160,
			},{
                id: 'vlanstgid',
                dataIndex: 'vlanstgid',
                header: _t('STG Id'),
                sortable: true,
                width: 120,
            }]
        });
        ZC.NortelVlanTablePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelVlanTablePanel', ZC.NortelVlanTablePanel);
ZC.registerName('NortelVlanTable', _t('Vlan Table'), _t('Vlan Tables'));

ZC.NortelVlanPortPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'NortelVlanPort',
            autoExpandColumn: 'name',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
				{name: 'name'},
				{name: 'intname'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'vlanportids'},
                {name: 'vlanporttype'},
                {name: 'vlanpvid'},
                {name: 'vlantag'},		
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60,
            },{
                id: 'name',
                dataIndex: 'intname',
                header: _t('Name'),
                width: 120,
			},{
                id: 'vlanportids',
                dataIndex: 'vlanportids',
                header: _t('Vlan Members'),
                sortable: true,
                width: 180,
			},{
                id: 'vlanporttype',
                dataIndex: 'vlanporttype',
                header: _t('Port Type'),
                sortable: true,
                width: 120,
            },{
                id: 'vlanpvid',
                dataIndex: 'vlanpvid',
                header: _t('PvId'),
                sortable: true,
			},{
                id: 'vlantag',
                dataIndex: 'vlantag',
                header: _t('Vlan Tag'),
                sortable: true,
            }]
        });
        ZC.NortelVlanPortPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('NortelVlanPortPanel', ZC.NortelVlanPortPanel);
ZC.registerName('NortelVlanPort', _t('Ports Table'), _t('Ports Tables'));

})();
