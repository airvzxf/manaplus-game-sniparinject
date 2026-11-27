#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Mana Plus - Game: Intercept and read the network packets
to find information about the game.
"""
from pathlib import Path

from sniparinject.network_sniffer import NetworkSniffer

if __name__ == '__main__':
    SETTINGS_PATH = Path(__file__).resolve().parent / 'settings.yml'
    NetworkSniffer(str(SETTINGS_PATH)).start()
