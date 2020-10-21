import re
import os

DIRECTORY = "D:\\RECOVER_PLURALSIGHT"
filenames = os.listdir(DIRECTORY)
count = 0

# for item in filenames:
#     # if '     ' in item:
#     #     count += 1
#     #     print(count, item)


#     if item[0:item.rfind('.')] != item[0:item.rfind('.')].strip():
#         count+=1
#         print(count, item)

    # if len(item.split('  ')) > 1:
    #     count+=1
    #     print(count, item.split('  ')) 

with open("C:\\Users\\srvsaha\\Desktop\\deleted_files_2.txt", encoding="utf8") as f:
    with open("C:\\Users\\srvsaha\\Desktop\\actual_mapping.tsv",'w', encoding="utf8") as fout:
        for line in f:
            splitted = re.split(r'\s{2,}', line.strip())
            if len(splitted) == 3:
                fout.write(splitted[0]+'\t'+splitted[1]+ '\t' + splitted[2]+'\n')
 # TODO: CHECK FOR 83 CASES WHERE LENGTH IS 4. Issue is with spaces