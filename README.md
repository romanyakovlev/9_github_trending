# 9_github_trending

Скрипт предназначен для отображения новых популярных проектов на гитхабе, обладающих самым большим количеством проблем(issue). Он выбирает 20 самых популярных проектов, созданных за неделю, и выводит на экран список ссылок с проблемами для каждого репозитория отдельно.

# Запуск

Устанавливаем необходимую для работы приложения библиотеку requests:

```sh
pip install -r requirements.txt
```

Запускаем сам скрипт

```sh
python3 github_trending.py
```
