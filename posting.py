from kivy.app import App
from kivy.uix.widget import Widget
import vk_api
import datetime 
import os
import time

my_token = 'ВАШ ТОКЕН'
vk_session = vk_api.VkApi(token = my_token)

vk = vk_session.get_api()

def PostProgram():
	now = datetime.datetime.now()
	tt = now.timetuple()
	print(tt)
	f = open('D:/Programs/posting/text.txt')
	if(os.stat('D:/Programs/posting/text.txt').st_size == 0):
		f = open('D:/Programs/posting/text.txt', 'w')
		for t in tt:
			f.write(str(t) + '\n')
		f.close()
	else:
		f = open('D:/Programs/posting/text.txt')
		with open('D:/Programs/posting/text.txt', 'r') as f:
			date = f.read().splitlines()
		day = date[2]
		hour = int(date[3])

		if(day != str(tt.tm_mday)):
			if(int(tt.tm_hour) > 16):
				f = open('D:/Programs/posting/text.txt', 'w')
				for t in tt:
					f.write(str(t) + '\n')
				f.close()

				f = "Текст поста"
				vk.wall.post(owner_id = "-ID группы", message = f, attachments ="ФОТО")

				exit()
			else:
				while(tt.tm_hour != 18):
					now = datetime.datetime.now()
					tt = now.timetuple()
					if(tt.tm_hour > 17):
						f = "Текст поста"
						vk.wall.post(owner_id = "-31830609", message = f, attachments ="photo11111111_111111111")

						exit()
					time.sleep(1800)
		f.close()
PostProgram()
