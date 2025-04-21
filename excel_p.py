import openpyxl

# 打开 Excel 文件
workbook = openpyxl.load_workbook('C:\\Users\\lenovo\\Documents\\成.xlsx')  # 替换成你的 Excel 文件名
sheet = workbook.active  # 默认读取第一个工作表

# 读取前两行
first_row = [cell.value for cell in sheet[1]]
second_row = [cell.value for cell in sheet[2]]

# 打印成“键: 值”的格式
if __name__ == '__main__':
    for key, value in zip(first_row, second_row):
        print(f"{key}：{value}")