# Currency Converter

Это простое приложение для конвертации валют, созданное на фреймворке Django.

## Функционал
- Конвертация валюты из одной в другую

## Установка
Чтобы запустить это приложение, вам нужно иметь Python и Django установленные на вашем компьютере. Следуйте инструкциям ниже, чтобы начать работу:

1. Клонируйте этот репозиторий:
   ```
   git clone https://github.com/Ivan-k35/Currency-convertor.git
   ```
2. Перейдите в директорию проекта:
   ```
   cd Currency-convertor/currency_convertor
   ```
3. Установите необходимые пакеты:
   ```
   pip install -r requirements.txt
   ```
4. Запустите сервер разработки Django:
   ```
   python manage.py runserver
   ```
5. Откройте веб-браузер и перейдите по адресу http://localhost:8000/ для использования приложения.

## Использование
1. Введите сумму и валюту, которую вы хотите конвертировать.
2. Выберите валюту, в которую вы хотите конвертировать.
3. Нажмите кнопку "Конвертировать", чтобы увидеть конвертированную сумму.

## Использованные API
Это приложение использует [Exchange Rates API](https://api.exchangerate.host) для получения последних курсов обмена валют.

## Авторы
- [Иван Кошкин](https://github.com/Ivan-k35)