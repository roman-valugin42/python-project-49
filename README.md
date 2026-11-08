# Brain Games

[![hexlet-check](https://github.com/roman-valugin42/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/roman-valugin42/python-project-49/actions)

Набор из пяти мини-игр для тренировки мозга. Работает в терминале через CLI.

## Доступные игры

| Игра | Описание | Команда |
|------|----------|---------|
| **brain-even** | Определить, чётное число или нет | `brain-even` |
| **brain-prime** | Определить, простое число или нет | `brain-prime` |
| **brain-calc** | Вычислить результат выражения (+, −, ×) | `brain-calc` |
| **brain-gcd** | Найти НОД двух чисел | `brain-gcd` |
| **brain-progression** | Найти пропущенное число в прогрессии | `brain-progression` |

## Требования

- Python >= 3.10
- [uv](https://github.com/astral-sh/uv) — менеджер пакетов

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/roman-valugin42/python-project-49.git
cd python-project-49
```

Собрать и установить пакет:

```bash
make build
make package-install
```

После установки команды доступны напрямую, без `uv run`:

```bash
brain-calc
brain-even
brain-prime
brain-gcd
brain-progression
```

## Использование

Запуск любой игры — просто введите название команды:

```bash
brain-calc
```

Игра задаст вопрос, вы ответите. Для победы нужно дать 3 правильных ответа подряд.

### brain-even

<details>
<summary>Успешная игра</summary>

[![asciicast](https://asciinema.org/a/LdCB9YV2IKUx3Nqj.svg)](https://asciinema.org/a/LdCB9YV2IKUx3Nqj)

</details>

### brain-calc

<details>
<summary>Успешная игра</summary>

[![asciicast](https://asciinema.org/a/z4ke30urLam9FpoA.svg)](https://asciinema.org/a/z4ke30urLam9FpoA)

</details>

<details>
<summary>Неудачная игра (неверный ответ)</summary>

[![asciicast](https://asciinema.org/a/z4ke30urLam9FpoA.svg)](https://asciinema.org/a/z4ke30urLam9FpoA)

</details>

### brain-gcd

<details>
<summary>Игровой процесс</summary>

[![asciicast](https://asciinema.org/a/Qt7KoDPqp3vzlL8U.svg)](https://asciinema.org/a/Qt7KoDPqp3vzlL8U)

</details>

### brain-progression

<details>
<summary>Игровой процесс</summary>

[![asciicast](https://asciinema.org/a/7lTkutvtXys3e05c.svg)](https://asciinema.org/a/7lTkutvtXys3e05c)

</details>

## Автоматические тесты

Проверка кода запускается на каждый коммит через GitHub Actions.
Файл `.github/workflows/hexlet-check.yml` отвечает за запуск — не удаляйте и не переименовывайте его.

## О проекте

[Хекслет](https://ru.hexlet.io/) — школа программирования. Это учебный проект программы [Программист](https://ru.hexlet.io/programs/python).
