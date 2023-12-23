import math
from typing import List, Dict, Tuple

import src.scripts.router as r


def read_file(file_path: str) -> str:  # TODO: Удалить, нужен для мока данных
    try:
        with open(file_path, 'r', encoding='utf-8') as content:
            return content.read()
    except OSError:
        print('Произошла ошибка')


def calculate_ship_next_coords(ship: Dict) -> Tuple[int, int]:
    '''Вычисляет следующие координаты корабля.'''
    current_x = ship['x']
    current_y = ship['y']
    match ship['direction']:
        case 'north':
            current_y -= ship['speed']
        case 'east':
            current_x += ship['speed']
        case 'south':
            current_y += ship['speed']
        case 'west':
            current_x -= ship['speed']
    return (current_x, current_y)


def is_belongs_to_circle(
    ship_1: Tuple[int, int],
    ship_2: Tuple[int, int],
    shot_radius: int = 20
) -> bool:
    '''
    Вычисляет, находится ли ship_2 в зоне досягаемости выстрела от ship_1.
    '''
    ship_1_x, ship_1_y = ship_1
    ship_2_x, ship_2_y = ship_2
    d = math.sqrt((ship_2_x - ship_1_x)**2 + (ship_2_y - ship_1_y)**2)
    return d <= shot_radius


def tick():
    '''Ход тика.'''
    response = r.scan()

    my_ships: List[Dict] = response['scan']['myShips']  # Мои корабли
    enemy_ships: List[Dict] = response['scan']['enemyShips']  # Чужие корабли

    # Мои задействованные корабли в следующем тике
    my_ships_involved_in_next_tick = []

    for enemy_ship in enemy_ships:
        # Здоровье корабля противника
        enemy_ship_hp = response['scan']['hp']

        # Координаты корабля противника в следующем тике
        enemy_next_coords = calculate_ship_next_coords(enemy_ship)

        # Мои корабли в пределах досягаемости
        my_ships_are_within_shooting_range = []

        for my_ship in my_ships:
            # Координаты моего корабля в следующем тике
            my_ship_next_coords = calculate_ship_next_coords(my_ship)

            # Проверяем корабль на досягаемость поражения противнику
            if is_belongs_to_circle(
                my_ship_next_coords,
                enemy_next_coords,
                my_ship['cannonRadius']
            ):
                my_ships_are_within_shooting_range.append(my_ship)

                # Проверяем наличие других вражеских кораблей вблизи
                other_enemy_ships = [
                    _ for _ in enemy_ships if _['id'] != enemy_ship['id']
                ]
                # Корабли противника в пределах досягаемости
                other_ships_are_within_shooting_range = []

                for other_enemy_ship in other_enemy_ships:
                    # Координаты противника в следующем тике
                    other_enemy_ship_next_coords = \
                        calculate_ship_next_coords(other_enemy_ship)

                    # Проверяем корабль противника на досягаемость поражения нам
                    if is_belongs_to_circle(
                        other_enemy_ship_next_coords,
                        my_ship_next_coords,
                    ):
                        other_ships_are_within_shooting_range.append(other_enemy_ship)

            # Оцениваем суммарное состояние флотов в зоне корабля противника
            FIGHT_READINESS_RATIO = 0.75  # Порог целостности корабля для вступления в бой (от 0 до 1)

            my_ships_flotilla = [
                _ for _ in my_ships_are_within_shooting_range \
                    if _['hp'] >= _['maxHp'] * FIGHT_READINESS_RATIO
            ]
            my_ships_flotilla_hp = sum([_['hp'] for _ in my_ships_flotilla])
            # vs
            enemy_ships_flotilla = [
                _ for _ in other_ships_are_within_shooting_range \
                    if _['hp'] >= _['maxHp']
            ]
            enemy_ships_flotilla_hp = sum([_['hp'] for _ in enemy_ships_flotilla]) + enemy_ship_hp

            if my_ships_flotilla_hp > enemy_ships_flotilla_hp:
                for my_ship in my_ships_flotilla:
                    if my_ship not in my_ships_involved_in_next_tick and enemy_ship_hp:
                        # Еще раз прицеливаемся
                        # Координаты моего корабля в следующем тике
                        my_ship_next_coords = calculate_ship_next_coords(my_ship)

                        # Проверяем корабль на досягаемость поражения противнику
                        if is_belongs_to_circle(
                            my_ship_next_coords,
                            enemy_next_coords,
                            my_ship['cannonRadius']
                        ):
                            my_ships_involved_in_next_tick.append(my_ship)
                            # TODO: ОГОНЬ! 💣
                            enemy_ship_hp -= 1
                if enemy_ship_hp:
                    pass
                    # TODO: Перенаправить корабли в сторону противника
                    my_ships_involved_in_next_tick.extend(
                        [_ for _ in my_ships_flotilla if _ not in my_ships_involved_in_next_tick]
                    )
            else:
                pass
                # TODO: Переопределить курс для всех кораблей во флотилии и отступить
