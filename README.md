# gpb-corporate-application

Цифровой прорыв 2020

## Зависимости

- Poetry - инструмент для управления зависимостями в Python (https://python-poetry.org/).
- Yarn - менеджер пакетов (https://yarnpkg.com/).
- Make - вспомогательная утилита (https://chocolatey.org/packages/make).

## Основные команды упраления проектом

Установка зависимостей, выполение миграций, создание файла конфигурации

```sh
$ make install
```

Запуск серверов разработки (webpack, django)

```sh
$ make run
```

Django миграции

```sh
$ poetry run task makemigrations
$ poetry run task migrate
```

Создание супер пользовотеля

```sh
$ poetry run task createsuperuser
```
