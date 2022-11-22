#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 2:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = list(range(1, 36))
    selected_balls = []
    selected_balls = sample(red_balls, 5)
    selected_balls.sort()
    selected_balls.extend(sorted(sample(range(1, 13), 2)))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
