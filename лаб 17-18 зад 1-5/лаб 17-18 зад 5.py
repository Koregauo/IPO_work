from PIL import Image, ImageDraw, ImageFont
# Открываем старое изображение
image5_07 = Image.open('image1_07.png')
# Создаём объект ImageDraw для рисования
draw = ImageDraw.Draw(image5_07)
# Задайте шрифт и размер (вы можете выбрать свой шрифт)
font = ImageFont.truetype('arial.ttf', 16)
# Задаём текст и его позицию
text = 'Жилинский'
text_position = (280, 10)
# Добавляем текст на изображение
draw.text(text_position, text, fill='black', font=font)
# Сохраняем изображение
image5_07.save('image5_07.png')
# Выводим изображение
image5_07.show()

