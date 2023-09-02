# Правила
#
# - ножиці ріжуть папір;
#
# - папір накриває камінь;
#
# - камінь ламає ножиці.
#
# Реалізувати перевірку хто виграв для 2-х гравців.
#
# Ножиці - 0, папір - 1, камінь - 2
#
# Перше число - вибір першого гравця, друге число - вибір другого гравця
#
# Варіанти відповідей: "Player 1 win", "Player 2 win", "Draw"

SCISSORS = 0
PAPER = 1
ROCK = 2

ALL_CHOICES = {
    (SCISSORS, PAPER): "Player 1 win",
    (PAPER, SCISSORS): "Player 2 win",
    (SCISSORS, ROCK): "Player 2 win",
    (ROCK, SCISSORS): "Player 1 win",
    (PAPER, ROCK): "Player 1 win",
    (ROCK, PAPER): "Player 2 win",
}


def solution(c1, c2):
    if c1 == c2:
        return "Draw"

    choice = (c1, c2)
    result = ALL_CHOICES[choice]
    return result


c1 = int(input("Введіть значення для гри: ножиці - 0, папір - 1, камінь - 2: "))
c2 = int(input("Введіть значення для гри: ножиці - 0, папір - 1, камінь - 2: "))
print(solution(c1, c2))