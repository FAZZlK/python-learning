# 4️⃣ Напишіть скрипт, який за введеним користувачем числом від 1 до 12, 
# буде виводити на екран повідомлення у вигляді назви місяця і пори року.
# Якщо користувач введе неприпустиме число, 
# програма має видавати повідомлення про помилку 

months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"]
seasons = ["Зима", "Весна", "Літо", "Осінь"]
user_input = int(input("Введіть число від 1 до 12: "))
season_index = 0


if user_input == 12 or user_input == 1 or user_input == 2:
   month_name = months[user_input - 1]
   print(f"{month_name}, {seasons[season_index]}")
elif 2 < user_input < 6:
  month_name = months[user_input - 1]
  season_index = 1
  print(f"{month_name}, {seasons[season_index]}")
elif 5 < user_input < 9:
  month_name = months[user_input - 1]
  season_index = 2
  print(f"{month_name}, {seasons[season_index]}")
elif 8 < user_input < 12:
  month_name = months[user_input - 1]
  season_index = 3
  print(f"{month_name}, {seasons[season_index]}")
else:
        print("Помилка")
