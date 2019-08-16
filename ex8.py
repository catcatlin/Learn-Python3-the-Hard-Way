print('\n\n')

formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False ,True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Mayb a poem",
    "Or a song about fear."
))

formatter = "{}{}{}{}"
print(formatter.format(
    "敲代码老报错那个,",
    "你特么不会是个",
    "傻子",
    "吧？"
))

print('\n\n')
