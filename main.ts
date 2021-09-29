function neustart () {
    Wert = 0
    keyTest = []
    sprite = game.createSprite(0, 0)
    sprite.set(LedSpriteProperty.Blink, 200)
}
// alternative, weil  anfangs key == keyTest -> false ??
function testKeyTest () {
    for (let Index = 0; Index <= 4; Index++) {
        if (key[Index] == keyTest[Index]) {
            Wert += 1
        }
    }
    if (Wert == 5) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
}
input.onButtonPressed(Button.A, function () {
    if (sprite.get(LedSpriteProperty.Y) == 4) {
        sprite.set(LedSpriteProperty.Y, 0)
    } else {
        sprite.change(LedSpriteProperty.Y, 1)
    }
})
input.onButtonPressed(Button.AB, function () {
    sprite.delete()
    neustart()
})
input.onButtonPressed(Button.B, function () {
    keyTest.push(sprite.get(LedSpriteProperty.Y))
    game.pause()
    if (sprite.get(LedSpriteProperty.X) == 4) {
        basic.pause(2000)
        game.resume()
        sprite.delete()
        testKeyTest()
        neustart()
    } else {
        basic.pause(500)
        game.resume()
        sprite.set(LedSpriteProperty.Y, 0)
        sprite.change(LedSpriteProperty.X, 1)
    }
})
let sprite: game.LedSprite = null
let keyTest: number[] = []
let Wert = 0
let key: number[] = []
key = [
0,
1,
2,
3,
4
]
neustart()
basic.forever(function () {
    if (game.isPaused()) {
        for (let Index = 0; Index <= keyTest.length - 1; Index++) {
            led.plot(Index, keyTest[Index])
        }
    }
})
