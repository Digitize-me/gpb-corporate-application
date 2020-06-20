![газпромбанк](https://holism.gpbdev.ru/static/media/logo-gpb-blue.1ac0c1e0.svg)

## Цифровой прорыв 2020

## Команда: Digitize-me

> Веб приложение для сотрудников GPB, позволяющее предлагать свои идеи по улучшению существующих бизнес-процессов и выносить на обсуждение темы, волнующие сотрудников, в формате голосования с элементами геймификации

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
