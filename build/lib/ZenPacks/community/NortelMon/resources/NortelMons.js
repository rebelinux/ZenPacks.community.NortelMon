(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.NortelTopologyPanel = Ext.extend(ZC.ComponentGridPanel, {
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

})();
