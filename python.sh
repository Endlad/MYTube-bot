#!/bin/bash

# Обновление списка пакетов
echo "Обновление списка пакетов..."
sudo apt update

# Установка Python 3
echo "Установка Python 3..."
sudo apt install -y python3

# Установка pip для Python 3
echo "Установка pip для Python 3..."
sudo apt install -y python3-pip

# Проверка версии Python и pip
echo "Проверка установленных версий..."
python3 --version
pip3 --version

echo "Установка завершена!"