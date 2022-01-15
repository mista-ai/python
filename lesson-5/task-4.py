from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='ru')
with open("text_4.txt", 'r', encoding='utf-8') as f:
    with open("result_4.txt", 'w', encoding='utf-8') as result_file:
        result_file.write(translator.translate(f.read()))
