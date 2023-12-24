from PIL import Image, ImageFilter
# Открываем изображение
image=Image.open('image3_07.png')
# Применяем фильтр к изображению
image4_07=image.filter(ImageFilter.GaussianBlur(radius=2))
# Сохраняем первое изображение
image4_07.save('image4_07.png')
# Применяем добавочно ещё 1 фильтр
image44_07=image4_07.filter(ImageFilter.EMBOSS)
# Сохраняем второе изображение
image44_07.save('image44_07.png')
# Выводим оба изображения
image4_07.show()
image44_07.show()
