# Генератор паролей c GUI на основе Tkinter.TTK

## Описание
Генератор паролей через secrets.choice с возможностью выбора длины пароля от
4 до 20 символов, опций 'Easy to read', 'Easy to say', возможностью выбора 
между комбинациями заглавных, строчных букв, чисел, и символов.

## Пример работы программы
![usage_example_1.gif](readme_assets%2Fusage_example_1.gif)

## Инициализация проекта
Введите в консоль (UNIX):
  ```sh
  git clone https://github.com/Lio-Kay/GUI_Password_Generator
  cd GUI_Password_Generator/
  poetry shell
  poetry install
  python main.py
  ```

## Описание структуры проекта
* readme_assets - Файлы для README.md
* logic_functions.py - Файл с функциями и логикой программы
* main.py - Точка входа и файл с фреймами, объединяющий логику программы

## Технологии в проекте
Библиотеки:
* tkiner
* ttkbootstrap
* screeninfo
* secrets
* flake8

Другие особенности:
* tk grid вместо frames
* poetry вместо venv/pip
