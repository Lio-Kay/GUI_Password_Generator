# Генератор паролей c GUI на основе Tkinter.TTK

## Описание
Генератор паролей через secrets.choice с возможностью выбора длинны пароля от 4 до 20 символов, опций 'Easy to read',
'Easy to say', возможностью выбора между комбинаций заглавных, строчных букв, чисел и символов.

## Пример работы программы
![usage_example_1.gif](readme_assets%2Fusage_example_1.gif)

## Описание структуры проекта
* readme_assets - Файлы для README.md
- logic_functions.py - Файл с функциями и логикой программы
- main.py - Файл с grid, объединяющий логику программы

## Технологии в проекте
Библиотеки:
* tkiner;
* ttkbootstrap;
* screeninfo;
* secrets.

Другие особенности:
* tk grid вместо frames;
* poetry вместо venv/pip.

## Возможные улучшения
* Переписать проект по парадигме ООП
* Добавить логгирование
