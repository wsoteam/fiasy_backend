from fatsecret import Fatsecret

fs = Fatsecret(
    '9587fc3b6c954855afbbcf2d2f5c4420',
    '7cda5c228b2a4be292af030eadacbc0b'
)

foods = fs.foods_get(44955)
print(foods)