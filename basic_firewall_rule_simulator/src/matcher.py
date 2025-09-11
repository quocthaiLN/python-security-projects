from src import Packet
from src import Rule

def match_packet(packet, rules, default='DENY'):
    for rule in rules:
        if rule.matches(packet):
            return rule.action
    return default