import glob
import re
import pandas as pd
import os
import shutil
files = glob.glob("fake_data\*.csv")
# files = glob.glob("fake_data\*[株式会社].csv")
# for file in files :
#     print(file)
#     print(os.path.split(file)[1])
#1リスト作成
# list = []
# for file in files:
#     row = [os.path.split(file)[1].replace(".csv","")]
#     list.append(row)
# df = pd.DataFrame(data=list, columns=["company"])
# df.to_csv("company.csv", encoding="shift_jis", index=False)

#山田derete
# for file in files:
#     file_name = os.path.split(file)[1]
#     if "山田" in file_name:
#         os.remove(file)

#とはいえ消すわけにも行かないのでにゃんこ変換
# for file in files:
#     file_name = os.path.split(file)[1]
#     if "山田" in file_name:
#         os.rename(file,file.replace("山田","にゃんこ"))

#既に存在してもOK：exist_ok=True
# os.makedirs("fake_data\株式会社", exist_ok=True)
# os.makedirs("fake_data\有限会社", exist_ok=True)
# os.makedirs("fake_data\合同会社", exist_ok=True)

# ふぉるだ分け
dirs = ["株式会社","有限会社","合同会社"]
for dir in dirs:
    if not os.path.isdir(r"fake_data\{}".format(dir)):
        os.mkdir(r"fake_data\{}".format(dir))
for file in files:
    file_name = os.path.split(file)[1]
    for dir in dirs:
        if dir in file_name:
            shutil.move(f"fake_data\{file_name}",f"fake_data\{dir}\{file_name}")

#戻しといて（めんどくさいからコピーしとこう）copy2はメタデータもコピー
# dirs = ["株式会社","有限会社","合同会社"]
# for dir in dirs:
#     new_files = glob.glob(r"fake_data\{}\*.csv".format(dir))
#     for file in new_files:
#         shutil.copy2(file,"fake_data")

#前株取得
# if not os.path.isdir("fake_data\前株大好き～"):
#     os.mkdir("fake_data\前株大好き～")
# import re
# for file in files:
#     file_name = os.path.split(file)[1]
#     #前方一致
#     if re.compile("^株式会社.*").search(file_name):
#         shutil.copy2(file,"fake_data\前株大好き～")





#データ読み込み
# data_path = files[0]
# data = pd.read_csv(data_path,encoding="shift_jis")
# print(data)