'''
from fnmatch import translate
from googletrans import Translator.translate as T
 
 text_to_translate = translator.translate(get_sentence,
                                                     src= from_lang,
                                                     dest= to_lang)
             
            # Storing the translated text in text
            # variable
            text = text_to_translate.text
'''
from googletrans import Translator
translator = Translator()
translator.translate('안녕하세요.')