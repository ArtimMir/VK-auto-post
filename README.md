# Скрипт, который постит нужный текст с картинкой в нужную группу ВК после 6 вечера каждый день.

В my_token указываем Ваш токен страницы ВК.

Здесь пишем текст поста: f = "Текст поста"

В owner_id вписываем -ID группы (например, -31830609)
В attachments фото из ВК - можно сохранить в сохраненные (например, photo11111111_111111111)
vk.wall.post(owner_id = "-ID группы", message = f, attachments ="ФОТО")
