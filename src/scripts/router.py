import httpx

from src.settings import TEAM_TOKEN


BASE_URL = 'https://datsblack.datsteam.dev'
HEADERS = {'X-API-Key': TEAM_TOKEN}


def scan():
    '''Сканирование вокруг своих кораблей.'''
    url = f'{BASE_URL}/api/scan'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def long_scan():
    '''Сканирование удалённой точки на карте.'''
    url = f'{BASE_URL}/api/longScan'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def ship_command():
    '''Обработка команд контроля кораблей.'''
    url = f'{BASE_URL}/api/shipCommand'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def registration_death_match():
    '''Регистрация на death match.'''
    url = f'{BASE_URL}/api/deathMatch/registration'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def exit_death_match_battle():
    '''Выход из death match боя.'''
    url = f'{BASE_URL}/api/deathMatch/exitBattle'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result


def registration_royal_battle():
    '''Регистрация на королевскую битву.'''
    url = f'{BASE_URL}/api/royalBattle/registration'

    r = httpx.post(url, headers=HEADERS)
    result = r.json()

    return result
