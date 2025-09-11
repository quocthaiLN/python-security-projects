from src import models
from src import parser

def match_packet(packet, rules, default='DENY'):
    for rule in rules:
        if rule.mathes(packet):
            return rule.ation
    return default