from pyrogram import Client, filters
from pytube import YouTube

# Настройки бота
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

app = Client("youtube_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Команда /watch для получения ссылки на видео
@app.on_message(filters.command("watch"))
def watch_video(client, message):
    # Проверяем, есть ли ID видео после команды
    if len(message.command) < 2:
        message.reply_text("Пожалуйста, введите ID видео после команды /watch")
        return

    video_id = message.command[1]  # Получаем ID видео из команды

    try:
        # Инициализируем YouTube объект
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")

        # Получаем поток с максимальным разрешением
        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

        if stream:
            video_url = stream.url  # Получаем прямую ссылку на Google Video
            # Генерируем ссылку для проигрывателя
            player_url = f"http://project-endlad.at.ua/projects/player.html?video={video_url}"
            # Отправляем ссылку на проигрыватель пользователю
            message.reply_text(f"Видео доступно для просмотра по ссылке: {player_url}")
        else:
            message.reply_text("К сожалению, видео недоступно для скачивания.")
    except Exception as e:
        message.reply_text(f"Произошла ошибка: {str(e)}")

# Запуск бота
app.run()
