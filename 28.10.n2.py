#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(
    # краткое описание программы
    description='Статистика для самых маленьких'
)

parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'values',
    # название параметров, которое будет отображено в справке
    metavar='VALUES',
    # сообщаем что ожидаются числа с плавающей запятой
    type=float,
    # параметров будет одного
    nargs='?',
    # краткое описание параметров
    help='входная последовательность чисел'
)

parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'values2',
    # название параметров, которое будет отображено в справке
    metavar='VALUES2',
    # сообщаем что ожидаются числа с плавающей запятой
    type=float,
    # параметров будет одного
    nargs='?',
    # краткое описание параметров
    help='входная последовательность чисел'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-a',
    # длинное название опции
    '--action',
    # парсер сохранит значение True, если встретит эту опцию
    action='store',
    # краткое описание опции
    help='вывести среднее значение',

    choices=['*', '/', '-', '+']
)

args = parser.parse_args()

print(args)

if args.action == '+':
    print(args.values + args.values2)
if args.action == '-':
    print(args.values - args.values2)
if args.action == '/':
    print(args.values / args.values2)
if args.action == '*':
    print(args.values * args.values2)


x = args.values
y = args.values2
z = args.action
z = x + z + y
z = eval(z)
print(z)