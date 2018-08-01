#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Tong Miao (illemonati)'
__version__ = "0.0.1"
__status__ = 'Prototype'


from warframe_alerts_rss import WarframeAlertsRss, WarframeAlert

wa = WarframeAlertsRss()
alerts = wa.get_alerts()

for alert in alerts:
    print("title: {}\n type: {}\n\n\n".format(alert.title, alert.type))
