﻿# -*- coding: utf-8 -*-
import re
#набор символов для замены
symb_dict = {
        #убираем неадекватное деление на абзацы
        '-\n':'',
        '\.\n':'.КОНЕЦ_АБЗАЦА.',
        '\n':' ',
        '.КОНЕЦ_АБЗАЦА.':'.\n',  
        '\r':'<p>',           
        }

#превращаем словарь с набором символов в два списка символов
orig_sym = list(symb_dict.keys())
repl_sym = list(symb_dict.values())

#вычисляем количество элементов в словаре символов (для цикла замены)
number_of_symbols = len(symb_dict)

#открываем файл, считываем и делаем преобразования
with open ('text.txt',  encoding='utf-8') as f:
        the_text = f.read ()
        the_text = ('<p>'+the_text+'<p>')
        #цикл замены символов через регулярные выражения
        for i in range (number_of_symbols):
                the_text = re.sub(orig_sym[i], repl_sym[i], the_text)
        #цикл замены начала и конца абзаца html-тегом абзаца через регулярные выражения
        for i in range (number_of_symbols):
                the_text = re.sub('\n', '</p><p>', the_text)
                
#открываем файл снова, теперь уже для записи нашего преобразованного текста
with open ('text.txt', 'w', encoding='utf-8') as f:
		f.write(the_text)
print ('ВСЁ ОК. ВАШ ФАЙЛ ПРЕОБРАЗОВАН.')
