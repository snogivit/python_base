#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Папа', 'Мама', 'Дочь', 'Бабушка']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Артем', 176],
    ['Олеся', 165],
    ['Алиса', 95],
    ['Людмила', 163],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост: '+my_family[0]+' -', my_family_height[0][1],'см.')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum_height = 0
sum_height += my_family_height[0][1]
sum_height += my_family_height[1][1]
sum_height += my_family_height[2][1]
sum_height += my_family_height[3][1]

print('Общий рост моей семьи -', sum_height, 'см')