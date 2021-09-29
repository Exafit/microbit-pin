def testKeyTest():
    global keyTest, sprite
    if key == keyTest:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
    keyTest = []
    sprite = game.create_sprite(0, 0)
    sprite.set(LedSpriteProperty.BLINK, 200)
def testKeyTest3():
    global Wert, keyTest, sprite
    for Index in range(5):
        if key[Index] == keyTest[Index]:
            Wert += 1
    if Wert == 5:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
    Wert = 0
    keyTest = []
    sprite = game.create_sprite(0, 0)
    sprite.set(LedSpriteProperty.BLINK, 200)

def on_button_pressed_a():
    if sprite.get(LedSpriteProperty.Y) == 4:
        sprite.set(LedSpriteProperty.Y, 0)
    else:
        sprite.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    keyTest.append(sprite.get(LedSpriteProperty.Y))
    if sprite.get(LedSpriteProperty.X) == 4:
        sprite.delete()
        testKeyTest3()
    else:
        sprite.set(LedSpriteProperty.Y, 0)
        sprite.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
keyTest: List[number] = []
Wert = 0
key: List[number] = []
key = [0, 1, 2, 3, 4]
Wert = 0
keyTest = []
sprite = game.create_sprite(0, 0)
sprite.set(LedSpriteProperty.BLINK, 200)

def on_forever():
    pass
basic.forever(on_forever)
