# -*- coding: utf-8 -*-
import os, shutil, time, sys, datetime, math, tqdm  
today = str (datetime.datetime.now())
print (today)
f_list = [today]
source_folder = r'C:\Users\Inet-USER\Desktop\Всяко разно\123\go\\'
destination_folder = r'C:\Users\Inet-USER\Desktop\Всяко разно\123\here\\'
log_exist_or_not = (source_folder + 'log.txt')
if os.path.exists(log_exist_or_not):
	os.remove(log_exist_or_not)
pb_i = 1
for root, dirs, files in os.walk(source_folder):
	dirs_i = len(dirs)
	files_i = len(files)
	dirfil = (dirs_i+files_i)
	print (dirfil)
	for i in range (dirs_i):
		folder_path = source_folder + dirs[i]
		dest_folder_path = destination_folder + dirs[i]
		if not os.path.exists(dest_folder_path):
			shutil.move(folder_path, destination_folder)
			msg = '\nКаталог "' + dirs[i] + '" успешно перемещен'
			print (msg)
			f_list.append(msg)
		else:
			shutil.rmtree(dest_folder_path,  ignore_errors=True)
			shutil.move(folder_path, destination_folder)
			msg = '\nКаталог "' + dirs[i] + '" существует. Осуществлена его перезапись.'
			print (msg)
			f_list.append(msg)
		percent_i = round((pb_i / dirfil)*100, 1)
		sys.stdout.write( "\n\r\rВыполнено " + str(percent_i) + "%    " + "[" + ("="*pb_i) + "]\n")		
		pb_i+=1
		time.sleep(.5)
	for i in range (files_i):
		src_file_path = source_folder + files[i]
		dest_file_path = destination_folder + files[i]
		if not os.path.isfile(dest_file_path):
			os.chmod (src_file_path, 0o777)
			shutil.move(src_file_path, destination_folder)
			msg = '\nФайл "' + files[i]  + '" успешно перемещен'
			print (msg)
			f_list.append(msg)
		else:
			os.chmod (dest_file_path, 0o777)
			os.remove(dest_file_path)
			shutil.move(src_file_path, destination_folder)
			msg = '\nФайл "' + files[i] + '" существует. Осуществлена его перезапись.'
			print (msg)
			f_list.append(msg)
		percent_i = round((pb_i / dirfil)*100, 1)
		sys.stdout.write( "\n\r\rВыполнено " + str(percent_i) + "%    " + "[" + ("="*pb_i) + "]\n")		
		pb_i+=1
		time.sleep(.5)
msg_full = ('\nПЕРЕМЕЩЕНО: ' + str(dirs_i) + ' КАТАЛОГОВ / ' + str(files_i) + 
' ФАЙЛОВ')
f_list.append(msg_full)
print (msg_full)
with open (source_folder+'log.txt', 'w', encoding='utf-8') as f:
		for index in f_list:
			f.write(index + '\n')
print ('\nЖурнал работы программы (log.txt) записан в исходном каталоге')
if dirs_i <= 4 and files_i <=4:
	time.sleep(3)
	sys.exit()
else:
	time.sleep(8)
	sys.exit()

