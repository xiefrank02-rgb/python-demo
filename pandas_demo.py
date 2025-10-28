import pandas as pd

# 左表：包含"学生ID"和"姓名"
left = pd.DataFrame({
    "学生ID": [100,101, 102, 103],
    "姓名": ["sam","张三", "李四", "王五"]
})

# 右表：包含"学生ID"和"成绩"
right = pd.DataFrame({
    "学生ID": [102, 103, 104],
    "成绩": [90.01, None, 87.50]
})

if __name__ == "__main__":
    # 内连接：只保留两个表中"学生ID"匹配的行
    inner_join = pd.merge(left, right, on="学生ID", how="inner")
    print(inner_join)
    print("-----")
    print(inner_join["成绩"].sum())
