#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = list(range(1, 34))
    selected_balls = np.random.choice(red_balls, 6,replace = False)
    selected_balls = sorted(selected_balls)
    selected_balls.append(np.random.randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
