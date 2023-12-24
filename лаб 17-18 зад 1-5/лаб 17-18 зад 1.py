from PIL import Image
# Открываем изображение
image=Image.open('моаи.png')
image1_07=image
# Выводим информацию о нём
print(image1_07.size, image1_07.format, image1_07.mode)
# Сохраняем изображение
image1_07.save('image1_07.png')
# Выводим изображение
image1_07.show()