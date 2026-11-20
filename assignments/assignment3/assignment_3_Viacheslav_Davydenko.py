"""
ASSIGNMENT #3 — API DATA & TRADING ALGORITHM

ЗАГАЛЬНА ОЦІНКА: 14 БАЛІВ

Цей assignment складається з двох частин:

PART 1 — Weather API & Data Analysis — 7 балів
PART 2 — Trading Algorithm — 7 балів


ФОРМАТ ЗДАЧІ:
- Завантажте один готовий .py файл у відповідний Assignment на платформі.
- Назва файлу має бути у форматі:
  assignment_3_firstname_lastname.py
- firstname та lastname мають відповідати імені та прізвищу студента
  саме так, як вони записані на платформі.
- Обидві частини завдання мають бути виконані в одному файлі.


====================================================================
PART 1 — WEATHER API & DATA ANALYSIS
====================================================================

Мета:
Навчитися надсилати та обробляти API-запити, працювати з JSON-відповідями
та перетворювати отримані дані у структурований формат за допомогою
pandas DataFrame.

ОЦІНЮВАННЯ: 7 БАЛІВ

1. Отримання прогнозу погоди — 2 бали
2. Перетворення даних у DataFrame — 2 бали
3. Базовий дослідницький аналіз даних (EDA) — 3 бали


ЗАВДАННЯ:

1. Отримайте прогноз погоди
   - Використайте будь-який API погоди.
   - Отримайте погодинні дані на наступні 7 днів.
   - Дані повинні містити щонайменше:
       * температуру;
       * швидкість вітру.

2. Перетворіть дані
   - Перетворіть отримані дані у pandas DataFrame.
   - Переконайтеся, що дані мають зручну для аналізу структуру.

3. Виконайте базовий EDA
   - Знайдіть мінімальну температуру за наступні 3 дні.
   - Знайдіть максимальну температуру за наступні 3 дні.
   - Знайдіть середню температуру за наступні 3 дні.
   - Обчисліть середню швидкість вітру по всьому DataFrame.
   - Порахуйте, скільки годин швидкість вітру перевищує
     середню швидкість вітру по DataFrame.

4. Виведіть результати
   - Виведіть отриманий DataFrame або його частину.
   - Виведіть результати всіх розрахунків у зрозумілому форматі.
"""

# TODO: реалізуйте PART 1 нижче
import requests
import pandas as pd

API_URL = "https://api.open-meteo.com/v1/forecast"
FORECAST_DAYS = 7
LATITUDE = 50.45466
LONGITUDE = 30.5233

params = dict(
    latitude=LATITUDE,
    longitude=LONGITUDE,
    hourly="temperature_2m,wind_speed_10m",
    forecast_days=FORECAST_DAYS
)

response = requests.get(API_URL, params=params)
response.raise_for_status()

data = response.json()

df = pd.DataFrame({
    "time": pd.to_datetime(data["hourly"]["time"]),
    "temperature": data["hourly"]["temperature_2m"],
    "wind_speed": data["hourly"]["wind_speed_10m"],
})
print(df)

first_three_days = df[df["time"] < df["time"].iloc[0].normalize() + pd.Timedelta(days=3)]

print("Мінімальна температура за наступні 3 дні:", first_three_days["temperature"].min())
print("Максимальна температура за наступні 3 дні:", first_three_days["temperature"].max())
print("Середня температура за наступні 3 дні:", round(first_three_days["temperature"].mean(), 2))
avg_wind_speed = df["wind_speed"].mean()
print("Середня швидкість вітру по всьому DataFrame:", round(avg_wind_speed, 2))
print("Кількість годин, коли швидкість "
      "вітру перевищує середню швидкість вітру по DataFrame:",
      df[df["wind_speed"] > avg_wind_speed]["temperature"].count())



"""
====================================================================
PART 2 — TRADING ALGORITHM
====================================================================

Мета:
Познайомитися з базовими принципами алгоритмічної торгівлі:
отриманням фінансових даних, підготовкою даних, аналізом ринкових
тенденцій та створенням простої торгової стратегії на основі правил.

ОЦІНЮВАННЯ: 7 БАЛІВ

1. Збір і підготовка даних — 2 бали
2. Розробка торгової моделі — 2 бали
3. Генерація торгових сигналів — 1 бал
4. Розрахунок ефективності моделі — 2 бали


ЗАВДАННЯ:

1. Збір даних
   - Оберіть один фінансовий інструмент:
       * акцію;
       * криптовалюту;
       * індекс;
       * або інший ринковий інструмент.
   - Отримайте історичні ринкові дані.
   - Дані повинні містити щонайменше:
       * Open;
       * Close;
       * High;
       * Low;
       * Volume.

2. Підготовка даних
   - Організуйте дані у pandas DataFrame.
   - Перевірте дані на пропущені або некоректні значення.
   - Підготуйте дані до подальшого аналізу.

3. Розробка моделі
   Реалізуйте просту стратегію перетину ковзних середніх
   (Moving Average Crossover).

   Потрібно:
   - розрахувати короткострокове ковзне середнє;
   - розрахувати довгострокове ковзне середнє;
   - визначити моменти, коли коротке середнє перетинає довге.

   Періоди ковзних середніх ви можете обрати самостійно.

4. Генерація сигналів
   Створіть торгові сигнали на основі вашої стратегії.

   Наприклад:
   - BUY — сигнал купівлі;
   - SELL — сигнал продажу;
   - HOLD — відсутність торгової дії.

5. Розрахунок ефективності моделі
   - Розрахуйте прибуток або збиток на основі згенерованих сигналів.
   - Виведіть фінальний результат роботи стратегії.
   - Результат має дозволяти зрозуміти, чи була стратегія
     прибутковою на вибраному історичному періоді.

6. Виведення результатів
   Покажіть щонайменше:
   - частину DataFrame з фінансовими даними;
   - значення короткого та довгого moving average;
   - торгові сигнали;
   - фінальний прибуток / збиток.
"""

# TODO: реалізуйте PART 2 нижче
import time
from datetime import datetime, timezone
 
import requests
import pandas as pd
 
API_URL = "https://api.binance.com/api/v3/klines"

SYMBOL = "BTCUSDT"
INTERVAL = "1h"
LIMIT=10

params = dict(
    symbol=SYMBOL,
    interval=INTERVAL,
    limit=LIMIT,
)

response = requests.get(API_URL, params=params)
response.raise_for_status()

data = response.json()

columns = ["Open time", "Open", "High", "Low", "Close", "Volume",
           "Close time", "Quote volume", "Trades",
           "Taker base volume", "Taker quote volume", "Ignore"]
df = pd.DataFrame(data, columns=columns)


df["Date"] = pd.to_datetime(df["Open time"], unit="ms", utc=True)
df = df.set_index("Date")

required_columns = ["Open", "High", "Low", "Close", "Volume"]
df = df[required_columns].astype(float)

print(df)
