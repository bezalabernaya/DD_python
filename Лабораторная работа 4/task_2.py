# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as file: # TODO считать содержимое csv файла
        data = csv.DictReader(file, delimiter=',', quotechar='\n')
        with open(OUTPUT_FILENAME, "w") as f: # TODO Сериализовать в файл с отступами равными 4
            List = [row for row in data]
            json.dump(List, f, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
