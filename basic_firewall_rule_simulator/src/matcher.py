from src import Packet
from src import Rule
from src.logger import logger
from ipaddress import AddressValueError
from ipaddress import NetmaskValueError

def match_packet(packet : Packet, rules : list[Rule], default='DENY'):
    try: 
        for rule in rules:
            check = rule.matches(packet)
            if check:
                logger.info(f'{rule.action} from IP: {packet.src_ip}, port: {packet.src_port} to IP: {packet.dst_ip}, port: {packet.dst_port} by protocol {packet.protocol}')
                return rule.action
            elif check == None:
                return False
        return default
    except Exception as e:
        logger.info(f'Unexpected error while matching packet: {e}')
        return default