import re

# \d{1,}
# [A-ZА-ЯЁ]{1,}
# [а-яА-ЯёЁ]\d
# [A-ZА-ЯЁ]{1}[a-zа-яё]{1,}   /   \b[A-ZА-ЯЁ]{1}[a-zа-яё]{1,}\b
# \b[aeyuioAEYUIOуеэаяоыиУЕЫАОЭЯИёЁ]{1}[a-zа-яA-ZА-ЯёЁ]{1,}\b
# \b\d+[ ,./!?]
# .+[*]+.+\n