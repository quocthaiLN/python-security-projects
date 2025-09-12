from src import Packet
from src import Rule
from src.logger import logger

def match_packet(packet : Packet, rules : list[Rule], default='DENY'):
    
    for rule in rules:
        try: 
            if rule.matches(packet):
                logger.info(f'{rule.action} from IP: {packet.src_ip}, port: {packet.src_port} to IP: {packet.dst_ip}, port: {packet.dst_port} by protocol {packet.protocol}')
                return rule.action
        except Exception as e:
            return default
    return default