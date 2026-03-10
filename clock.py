"""
带UI界面的Python时钟
- 浅灰色背景
- 蛋黄色字体
- 显示年月日和具体时间
"""

import tkinter as tk
from datetime import datetime


def update_time():
    """更新时钟显示"""
    now = datetime.now()
    date_str = now.strftime("%Y年%m月%d日")
    time_str = now.strftime("%H:%M:%S")
    weekday_names = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    weekday_str = weekday_names[now.weekday()]

    date_label.config(text=date_str)
    time_label.config(text=time_str)
    weekday_label.config(text=weekday_str)
    root.after(1000, update_time)  # 每秒更新一次


# 创建主窗口
root = tk.Tk()
root.title("桌面时钟")

# 柠檬黄背景
root.configure(bg="black")

# 灰色字体
font_color = "white"
accent_color = "pink"

# 设置窗口大小
root.geometry("500x300")
root.resizable(True, True)

# 主框架
main_frame = tk.Frame(root, bg="#FFF44F", padx=40, pady=40)
main_frame.pack(expand=True, fill="both")

# 日期标签 - 大字体
date_label = tk.Label(
    main_frame,
    font=("Microsoft YaHei UI", 32, "bold"),
    fg=font_color,
    bg="#FFF44F",
)
date_label.pack(pady=(0, 10))

# 星期标签
weekday_label = tk.Label(
    main_frame,
    font=("Microsoft YaHei UI", 20, "bold"),
    fg=font_color,
    bg="#FFF44F",
)
weekday_label.pack(pady=(0, 20))

# 时间标签 - 超大字体
time_label = tk.Label(
    main_frame,
    font=("Consolas", 48, "bold"),
    fg=accent_color,
    bg="#FFF44F",
)
time_label.pack(pady=10)

# 开始更新时间
update_time()

# 运行主循环
root.mainloop()
