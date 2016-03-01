#!/usr/bin/env python
from rqt_gui_py.plugin import Plugin

from rqt_launchtree.launchtree_widget import LaunchtreeWidget


class LaunchtreePlugin(Plugin):

    def __init__(self, context):
        super(LaunchtreePlugin, self).__init__(context)

        self._widget = LaunchtreeWidget(context)
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() +
                                        (' (%d)' % context.serial_number()))
        context.add_widget(self._widget)

    def shutdown_plugin(self):
        self._widget.shutdown()

    def save_settings(self, plugin_settings, instance_settings):
        self._widget.save_settings(plugin_settings, instance_settings)

    def restore_settings(self, plugin_settings, instance_settings):
        self._widget.restore_settings(plugin_settings, instance_settings)