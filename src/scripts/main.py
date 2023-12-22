# !usr/bin/env python3

import httpx

from src.logger import logger
from src.settings import TEAM_TOKEN


def main(url: str = 'https://www.google.ru/') -> None:
    """Request checking script."""
    page = httpx.get(url)
    logger.info(f'Выполнен запрос на {url}')
    team_token = TEAM_TOKEN if all((
        len(TEAM_TOKEN) == 36,
        TEAM_TOKEN.startswith('a7217'),
        TEAM_TOKEN.endswith('81b2f')
    )) else ''
    if team_token:
        logger.info('Введен секретный токен.')
    else:
        logger.info(('Вы не ввели секретный токен! '
                    'Заполните его и повторите попытку.'))
        return
    if page.status_code:
        logger.info('К хакатону готовы!')
    else:
        logger.info(('Ответ на запрос не получен. '
                    'Убедитесь в корректности адреcа запрашиваемого ресурса.'))


if __name__ == '__main__':
    main()
