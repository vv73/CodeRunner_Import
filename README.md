# CodeRunner_Import

Скрипт для импорта "обычных" задач 
(тесты входных и выходных данных, проверка по точному соответствию) в CodeRunner

# Использование

Каждая задача должна располагаться в отдельной папке и содержать в своем корне 

1. условие в файле statement.html
2. подпапку tests с тестами (все файлы тестов должны иметь имена только из цифр без расширения, а ответы к ним - такие же названия и расширение .a, например 01 и 01.a соответственно.)

Первых два теста будутавтосматически отображаются в условии как примеры.

Расположите maketests.py в папке с задачами и запустите.
Скрипт создаст файл questions.xml в формату Moodle XML

Потом задачи мпортируются в любой курс.
