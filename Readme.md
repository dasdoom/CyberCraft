# GitSearch

Даний проект був створений за допомогою мікрофреймворку **Flask** та мови програмування **Python** [Застосунок](https://quiet-reaches-25909.herokuapp.com/)

# Usage

Користуватись застосунком дуже просто, достатньо ввести Github login і вам відобразиться наявні репозиторії за цим логіном та ім'я акаунту.
Якщо такого акаунту не існує, система не відобразить цього(з обміркувань безпеки). Якщо за цим акаунтом не має імені, то ім'я буде відображатись як _None_

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Коривтування сервісом")

# Functions

Дані застосунок отримує за допомогою двох функції _run_query_ та  _findGitData_ .
У функції _findGitData_ задано запит до GraphQL API, який робить запит **query**, за допомогою функції _run_query_. Ця функція повертає нам ім'я та репозиторії за заданим логіном.

Функція _run_query_ робить post запит до GraphQL API, та повертає результат запиту.

# Tests

Протестовано систему за допомогою бібліотеки _unittest_ та _vcr.py_ .
_vcr.py_ використано для запису отриманих даних з API для швидшого доступу в майбутньому та для роботи тестів в автономному режимі. Протестовано коректну роботу сторінки, коректну роботу завантаження сторінки, коректність виведення даних за логіном, правильна реакція системи на запит з пустим полем вводу, коректність імені та репозиторіїв (порівняно дані з REST API), реакція системи на введеня іншого посилання. 
За допомогою _vcr.py_ дані записано в файли: VCR.yaml, VCR1.yaml, VCR2.yaml.

# Linter

Для перевірки "чистоти" коду використано лінтер **Flake8** з його базовими правилами.