from PIL import Image
# Открываем изображение
image=Image.open('image1_07.png')
# Поварачиваем изображение против часовой стрелки
image2_07=image.rotate(30, 0, expand=True)
# Сохраняем изображение
image2_07.save('image2_07.png')
# Выводим изображение
image2_07.show()