import requests
import os

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(from_file, to_file, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param from_file: из какого файла взять текст
    :param to_file: в какой файл записать перевод
    :param from_lang: с какого языка перевести
    :param to_lang: на какой язык перевести
    """

    # Получить текст для перевода
    try:
        with open(from_file, encoding='utf-8') as f:
            text = f.read()
    except OSError:
        print("Файл не найден")
        return

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang)
    }

    response = requests.get(URL, params=params)
    json = response.json()

    # Записать перевод
    with open(to_file, encoding='utf-8', mode='w') as f:
        f.write(''.join(json['text']))


dest_dir = os.path.dirname(os.path.abspath(__file__))

translate_it(os.path.join(dest_dir, 'FR.txt'), os.path.join(dest_dir, 'FR_tr.txt'), 'fr', 'ru')
translate_it(os.path.join(dest_dir, 'DE.txt'), os.path.join(dest_dir, 'DE_tr.txt'), 'de', 'ru')
translate_it(os.path.join(dest_dir, 'ES.txt'), os.path.join(dest_dir, 'ES_tr.txt'), 'es', 'ru')
