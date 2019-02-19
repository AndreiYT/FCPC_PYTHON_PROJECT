foul_words = ['bobo', 'tanga', 'inutil', 'tarantado', 'gago', 'tangina', 'putangina', 'pakyu', 'fuck',
              'leche', 'ulol', 'bading', 'bakla', 'supot', 'hangal', 'barubal', 'nigga', 'yawa', 'pastilan']

sentence = input('Enter your sentence: ')

new = [x for x in sentence.lower().split()]

text = ''
for word in new:
    if word in foul_words:
        a = len(word)

        text += '*' * a + ' '

    else:
        text += word + ' '

print(text)
