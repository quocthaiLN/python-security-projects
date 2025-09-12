import logging

logger = logging.getLogger('basic_firewal_simulator_logger')
logger.setLevel(logging.DEBUG)

formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

file_handler = logging.FileHandler('log/basic_firewal_simulator.log')
file_handler.setFormatter(formater)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG) 

logger.addHandler(file_handler)
logger.addHandler(console_handler)