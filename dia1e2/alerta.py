"""
Alerma de temperatura

Faça um script que pergunta ao usuário quel a tempertura atual e o indice de umidade do ar sendo
que será exibida uma mensagem de alerta dependendo das condições:

temp maior 45: ALERTS!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp ente 0 e 10: Frio
temp < 0: ALERTS: Frio extremo
"""
import sys
import logging

log = logging.Logger('alerta')


# TODO: Mover para módulo de utilidades

def is_completely_filled(dict_of_inputs):
    """Retuns a boolan telling if a dict is completly filled."""
    info_size = len(dict_of_inputs)
    filled_size = len([value for value in dict_of_inputs.values() if value is not None])
    return info_size == filled_size


def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user inout."""
    for key in dict_of_info:
        if info[key] is not None:
            continue
        try:
            dict_of_info[key] = float(input(f'Qual a {key}? ').strip())
        except ValueError:
            log.error(f'{key.capitalize()} inválida')
            break


# PROGRAMA PRINCIPAL

info = {'temperatura': None, 'umidade': None}

while not is_completely_filled(info):
    read_inputs_for_dict(info)

temp, umidade = info.values()

if temp > 45:
    print('ALERTA!!! 🥵 Perigo de calor extemo')
elif temp < 0:
    print('ALERTA!!!🧊 Frio Extremo.')    
elif 10 <= temp <=30:
    print('😀 Normal')
elif 0 <= temp <= 10:
    print('🥶 Frio')   
elif temp * 3 >= umidade:
    print('ALERTA!!! 🥵 Perido de color úmido')
