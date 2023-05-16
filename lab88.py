from PIL import Image, ImageDraw, ImageFont
def lab1():
    filename = "stud.jpg"
    with Image.open(filename) as img:
        img.load()

    cropped_img = img.crop((150, 110, 600, 490))
    # cropped_img.show()
    cropped_img.save("cropped_stud.jpg")

lab1()

def lab2():
    d = {1: "stud.jpg", 2: "23f.jpg", 3: "8m.jpg", 4: "dr.jpg"}

    print("1 - Сессия\n"
          "2 - 23 февраля\n"
          "3 - 8 марта\n"
          "4 - День рождения")
    ans = int(input("Для получения открытки введите число - номер прадника : "))

    filename = d[ans]
    with Image.open(filename) as img:
        img.load()

    img.show()

lab2()

def lab3():
    name = input("Введите имя получателя: ")
    filename = "stud.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("arial_bold.ttf", 40)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 75, 20),
        name + ", поздравляю!",
        font=font,
        fill=('#2500ff')
    )
    img.show()
    img.save(name + "_stud.png")


lab3()