"""Шаг 2. Переписываем на asyncio.

Задание 2а:
  1. Сделайте work корутиной (async def).
  2. Замените time.sleep на await asyncio.sleep.
  3. Сделайте main корутиной и вызовите в ней work через await в цикле.
  4. Запустите через asyncio.run.

Замерьте время. Изменилось ли оно по сравнению с шагом 1? Почему?

Задание 2б:
  Перепишите main так, чтобы все 10 задач ждали одновременно.
  Подсказка: asyncio.gather. Что изменилось в порядке вывода?
"""

import argparse
import asyncio

from timer import print_time


async def work(n: int) -> None:
    print(f"start {n}")
    await asyncio.sleep(1)
    print(f"done {n}")


async def main(concurrent: bool = False) -> None:
    if concurrent:
        await asyncio.gather(*(work(n) for n in range(1, 11)))
        return

    for n in range(1, 11):
        await work(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Сравнить последовательное и конкурентное ожидание.")
    parser.add_argument(
        "--concurrent",
        action="store_true",
        help="запустить все десять корутин конкурентно (шаг 2б)",
    )
    args = parser.parse_args()

    with print_time():
        asyncio.run(main(concurrent=args.concurrent))
