meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL':'una respuesta a una broma',
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?

    print(word)
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print('Esa palabra no esta')
