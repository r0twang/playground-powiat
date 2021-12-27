import random
from log import log_info
from turn import play_turn
from independence_turn import play_independence_turn

def load_values():
    with open('map-data/status.txt', 'r') as f:
        powiaty_left = int(f.readline())
        last_powiat = f.readline().rstrip()

    return powiaty_left, last_powiat

def get_last_powiat_value(powiaty_left):
    x = 167 - powiaty_left
    return (((3.5 * 0.49) * 10**-6) * x**2) + (0.125*0.49)

def get_biggest_powiat_value(powiaty_left):
    x = 167 - powiaty_left
    return 0.0075 * x - 1.9275

def select_turn_type():
    powiaty_left, last_powiat = load_values()

    if (last_powiat == '0'):
        return play_turn('regular')

    independence_random_val = random.random()
    info = 'Independence_random_val = {}'.format(independence_random_val)
    independence_probability = 1/110
    log_info(info)
    independence_info = 'Independence probability = {}'.format(independence_probability)
    log_info(independence_info)
    if (independence_random_val < independence_probability):
        # print('[INFO] Playing independence round.')
        info = '[INFO] Playing independence round.'.format()
        log_info(info)
        return play_independence_turn()

    random_val = random.random()
    info = 'random_val = {}'.format(random_val)
    log_info(info)
    last_powiat_value = get_last_powiat_value(powiaty_left)
    last_powiat_value_info = 'powiaty_left = {}'.format(last_powiat_value)
    log_info(last_powiat_value_info)
    if (random_val < last_powiat_value):
        # print('[INFO] Region conquering previously will be conquering.')
        info = '[INFO] Region conquering previously will be conquering.'.format()
        log_info(info)
        return play_turn('last')

    return play_turn('regular')
