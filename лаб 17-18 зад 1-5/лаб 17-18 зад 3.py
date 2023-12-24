from PIL import Image
# Открываем изображение
image=Image.open('image1_07.png')
# Обрезаем изображение
image3_07=image.crop((10, 10, 300, 360 ))
# Сохраняем изображение
image3_07.save('image3_07.png')
# Выводим изображение
image3_07.show()