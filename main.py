import csv
import re
import os

APPNAME = "CodeWarrior MapFile to CSV"
APPVERSION = 1.0
DEVELOPER = "ReaZ0n23"
print(APPNAME, "Version", APPVERSION, "\nMade by", DEVELOPER, "\n/*------------------------------------*/")

input_file_name = input("入力するファイル名を入力してください。\n>>>")
output_file_name = input("出力するファイル名を入力してください。\n未指定の場合、入力ファイルと同じファイル名で出力します。\n>>>")
if not (output_file_name):
    output_file_name = input_file_name
if (output_file_name[-4:] != ".csv"):
    output_file_name += ".csv"
input_file_path = os.path.dirname(__file__) + "\\" + input_file_name
output_file_path = os.path.dirname(__file__) + "\\" + output_file_name

# 正規表現(セクション名、データ行)
section_pattern = re.compile(r"^([\.\w]+)\s+section layout")
data_pattern = re.compile(
    r"^\s*([0-9a-fA-F]{8})\s+([0-9a-fA-F]{6,8})\s+([0-9a-fA-F]{8})\s+[0-9a-fA-F]{8}\s+(?:\d+\s+)?(.*?)\s{2,}(.+)$"
)

rows = []
section_name = None

with open(input_file_path, "r", encoding="utf-8") as f:
    for line in f:
        # Extract section name
        section_match = section_pattern.match(line)
        if section_match:
            section_name = section_match.group(1)
            continue

        # Extract datas
        data_match = data_pattern.match(line)
        if data_match and section_name:
            address     = data_match.group(1)
            size_hex    = data_match.group(2)
            virt_addr   = data_match.group(3)
            symbol      = data_match.group(4).strip()
            obj_file    = data_match.group(5).strip()

            rows.append([
                section_name,
                f"0x{address}",
                f"0x{virt_addr}",
                symbol,
                obj_file,
                int(size_hex, 16)
            ])

# CSVに出力
with open(output_file_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Section", "Address", "VirtualAddress", "Symbol", "ObjectFile", "Size(Bytes)"])
    writer.writerows(rows)
    
print("正常に出力しました。")
