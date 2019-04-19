#! python3

import shutil,os

from datetime import *
today = datetime.today()
today = today.strftime('%d_%m_%y') 

sb_files = ('sign42TB.3pf', 'sign42TB.024', 'sign42TB.025')
arm = ('C:\\ARM_GSU\\', 'C:\\ARM_OEB\\', 'C:\\ARM_ORU\\', 'C:\\ARM_UKO\\', 'C:\\ARM_UOD\\', 'C:\\ARM_UUR\\')

work_dir = ('C:\\SBERBANK\\anet\\archive\\IN\\')
work_dir_list = os.listdir(work_dir)
for x in work_dir_list:
    if x == today:
        work_dir = work_dir + today + '\\'
        if os.path.exists(work_dir+sb_files[0]) and \
           os.path.exists(work_dir+sb_files[1]) and \
           os.path.exists(work_dir+sb_files[2]):
            for y in arm:
                shutil.copy2(work_dir+sb_files[0], y)
                shutil.copy2(work_dir+sb_files[1], y)
                shutil.copy2(work_dir+sb_files[2], y)
            print('%s: в рабочие каталоги пользователей внесены изменения' %today)
        else:
            print('Файлы для обновления в каталоге <%s> не найдены!' %today )


