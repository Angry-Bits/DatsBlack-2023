# !usr/bin/env python3

import httpx

from src.logger import logger
from src.settings import TEAM_TOKEN
import router as r


def main():
    # Регистрируемся на игру
    r.registration_death_match()


if __name__ == '__main__':
    main()
