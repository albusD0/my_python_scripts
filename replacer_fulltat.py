﻿# -*- coding: utf-8 -*-
import re
#набор символов для замены
symb_dict = {
		'À':'А',
		'à':'а',
		'Á':'Б',
		'á':'б',
		'Â':'В',
		'â':'в',
		'Ã':'Г',
		'ã':'г',
		'Ä':'Д',
		'ä':'д',
		'Å':'Е',
		'å':'е',
		'Æ':'Ж',
		'æ':'ж',
		'Ç':'З',
		'ç':'з',
		'È':'И',
		'è':'и',
		'É':'Й',
		'é':'й',
		'Ê':'К',
		'ê':'к',
		'Ë':'Л',
		'ë':'л',
		'Ì':'М',
		'ì':'м',
		'Í':'Н',
		'í':'н',
		'Î':'О',
		'î':'о',
		'Ï':'П',
		'ï':'п',
		'Ð':'Р',
		'ð':'р',
		'Ñ':'С',
		'ñ':'с',
		'Ò':'Т',
		'ò':'т',
		'Ó':'У',
		'ó':'у',
		'Ô':'Ф',
		'ô':'ф',
		'Õ':'Х',
		'õ':'х',
		'Ö':'Ц',
		'ö':'ц',
		'×':'Ч',
		'÷':'ч',
		'Ø':'Ш',
		'ø':'ш',
		'ú':'ъ',
		'û':'ы',
		'Ü':'Ь',
		'ü':'ь',
		'Ý':'Э',
		'ý':'э',
		'Þ':'Ю',
		'þ':'ю',
		'ß':'Я',
		'ÿ':'я',
		'Û':'Ы',
		#чисто-татарские-знаки
        '¨':'Ә',
        '¸':'ә',
        '¯':'Ө',
        '¿':'ө',
        'ª':'Ү',
        'º':'ү',
        '«':'Ӊ',
        '»':'ӊ',
        '‰':'Җ',
        '¢':'җ',
        '³':'h',
        '²':'h',
         #убираем неадекватное деление на абзацы
        '-\n':'',
        '\.\n':'.КОНЕЦ_АБЗАЦА.',
        '\n':' ',
        '.КОНЕЦ_АБЗАЦА.':'.\n',     
        }

#превращаем словарь с набором символов в два списка символов
orig_sym = list(symb_dict.keys())
repl_sym = list(symb_dict.values())

#вычисляем количество элементов в словаре символов (для цикла замены)
number_of_symbols = len(symb_dict)

#открываем файл, считываем и делаем преобразования
with open ('text.txt',  encoding='utf-8') as f:
        the_text = f.read ()        
        #цикл замены символов через регулярные выражения
        for i in range (number_of_symbols):
                the_text = re.sub(orig_sym[i], repl_sym[i], the_text)
                
#открываем файл снова, теперь уже для записи нашего преобразованного текста
with open ('text.txt', 'w', encoding='utf-8') as f:
		f.write(the_text)
print ('ВСЁ ОК. ВАШ ФАЙЛ ПРЕОБРАЗОВАН.')
