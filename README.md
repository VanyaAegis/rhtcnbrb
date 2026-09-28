[README.md](https://github.com/user-attachments/files/32772432/README.md)
# Tic-Tac-Toe Android — Build APK

Это готовый GitHub-проект для сборки Android APK через GitHub Actions.

## Как получить APK

1. Создай новый **пустой** репозиторий на GitHub.
2. Загрузи в него все файлы этого проекта.
3. Открой вкладку **Actions**.
4. Выбери workflow **Build APK**.
5. Нажми **Run workflow**.
6. Дождись зелёной галочки.
7. Открой завершённый запуск и скачай artifact **TicTacToe-APK**.
8. Внутри ZIP будет готовый `.apk`.

Workflow также запускается автоматически при push в ветку `main`.

## Важно

Первая сборка может занять заметное время: Buildozer скачивает Android SDK/NDK и собирает зависимости.

Проект рассчитан на debug APK. Для публикации в Google Play понадобится отдельная release/AAB-сборка и подпись приложения.
