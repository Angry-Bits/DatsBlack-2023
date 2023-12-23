from typing import Dict

import httpx

from src.settings import TEAM_TOKEN


BASE_URL = 'https://datsblack.datsteam.dev'
HEADERS = {'X-API-Key': TEAM_TOKEN}


def scan() -> Dict:
    '''Сканирование вокруг своих кораблей.'''
    url = f'{BASE_URL}/api/scan'

    r = httpx.get(url, headers=HEADERS)
    result = r.json()

    return result


def long_scan() -> Dict:
    '''Сканирование удалённой точки на карте.'''
    url = f'{BASE_URL}/api/longScan'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def ship_command() -> Dict:
    '''Обработка команд контроля кораблей.'''
    url = f'{BASE_URL}/api/shipCommand'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def registration_death_match() -> Dict:
    '''Регистрация на death match.'''
    url = f'{BASE_URL}/api/deathMatch/registration'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def exit_death_match_battle() -> Dict:
    '''Выход из death match боя.'''
    url = f'{BASE_URL}/api/deathMatch/exitBattle'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def registration_royal_battle() -> Dict:
    '''Регистрация на королевскую битву.'''
    url = f'{BASE_URL}/api/royalBattle/registration'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result
