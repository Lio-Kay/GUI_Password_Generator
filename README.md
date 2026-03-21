# GUI Password Generator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Poetry](https://img.shields.io/badge/Dependency-Poetry-blueviolet)

## Overview

A desktop password generator application built with **Python** using the **Tkinter/TTK GUI toolkit**.

The application allows users to generate secure passwords using Python’s `secrets` module. Users can customize password length and select which character sets should be used during generation.

The project demonstrates building **desktop graphical interfaces in Python**, implementing **secure random generation**, and organizing application logic separately from the UI layer.

---

## Application Demo

![usage_example_1.gif](readme_assets%2Fusage_example_1.gif?)

## Installation
### Requirements

- Python 3.x
- Poetry
Clone the repository and install dependencies:
  ```sh
  git clone https://github.com/Lio-Kay/GUI_Password_Generator
  cd GUI_Password_Generator/
  poetry shell
  poetry install
  python main.py
  ```

## Project Structure
* readme_assets - Images and GIFs used in README
* logic_functions.py - Password generation logic and helper functions
* main.py

## Technologies Used
* tkiner
* ttkbootstrap
* screeninfo
* secrets
* flake8

## Additional Features
* The interface layout uses the Tkinter grid system for flexible widget positioning
* Password generation logic is isolated from GUI components
* Secure randomness is implemented using Python's cryptographically secure secrets module
* Dependencies are managed using Poetry instead of pip/venv
