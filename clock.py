"""
带UI界面的Python时钟
- 浅灰色背景
- 蛋黄色字体
- 显示年月日和具体时间
"""

import tkinter as tk
from datetime import datetime


# 番茄钟相关变量
POMODORO_MINUTES = 25
remaining_seconds = POMODORO_MINUTES * 60
is_running = False
timer_id = None


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


def format_pomodoro(seconds):
    """将秒数格式化为 MM:SS"""
    m, s = divmod(seconds, 60)
    return f"{m:02d}:{s:02d}"


def update_pomodoro():
    """更新番茄钟倒计时"""
    global remaining_seconds, timer_id, is_running
    if remaining_seconds <= 0:
        is_running = False
        start_pause_btn.config(text="开始")
        return
    remaining_seconds -= 1
    pomodoro_label.config(text=format_pomodoro(remaining_seconds))
    timer_id = root.after(1000, update_pomodoro)


def toggle_pomodoro():
    """开始/暂停番茄钟"""
    global is_running, timer_id
    if is_running:
        is_running = False
        if timer_id:
            root.after_cancel(timer_id)
            timer_id = None
        start_pause_btn.config(text="开始")
    else:
        is_running = True
        start_pause_btn.config(text="暂停")
        update_pomodoro()


def reset_pomodoro():
    """重置番茄钟"""
    global remaining_seconds, is_running, timer_id
    is_running = False
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None
    remaining_seconds = POMODORO_MINUTES * 60
    pomodoro_label.config(text=format_pomodoro(remaining_seconds))
    start_pause_btn.config(text="开始")


# 创建主窗口
root = tk.Tk()
root.title("桌面时钟")

# 背景色
bg_color = "#89CFF0"  # baby blue
root.configure(bg=bg_color)

# 字体颜色（baby blue 背景下的深色便于阅读）
font_color = "#1e3a5f"
accent_color = "#d53f8c"  # 柔和粉色

# 设置窗口大小
root.geometry("500x400")
root.resizable(True, True)

# 主框架
main_frame = tk.Frame(root, bg=bg_color, padx=40, pady=40)
main_frame.pack(expand=True, fill="both")

# 日期标签 - 大字体
date_label = tk.Label(
    main_frame,
    font=("Microsoft YaHei UI", 32, "bold"),
    fg=font_color,
    bg=bg_color,
)
date_label.pack(pady=(0, 10))

# 星期标签
weekday_label = tk.Label(
    main_frame,
    font=("Microsoft YaHei UI", 20, "bold"),
    fg=font_color,
    bg=bg_color,
)
weekday_label.pack(pady=(0, 20))

# 时间标签 - 超大字体
time_label = tk.Label(
    main_frame,
    font=("Consolas", 48, "bold"),
    fg=accent_color,
    bg=bg_color,
)
time_label.pack(pady=10)

# 番茄钟区域
pomodoro_frame = tk.Frame(main_frame, bg=bg_color)
pomodoro_frame.pack(pady=(30, 10))

pomodoro_label = tk.Label(
    pomodoro_frame,
    text=format_pomodoro(remaining_seconds),
    font=("Consolas", 36, "bold"),
    fg=accent_color,
    bg=bg_color,
)
pomodoro_label.pack(pady=(0, 15))

btn_frame = tk.Frame(pomodoro_frame, bg=bg_color)
btn_frame.pack()
start_pause_btn = tk.Button(
    btn_frame,
    text="开始",
    font=("Microsoft YaHei UI", 12, "bold"),
    command=toggle_pomodoro,
    padx=20,
    pady=5,
    relief="flat",
    bg=accent_color,
    fg="white",
    activebackground="#ff8fa3",
    activeforeground="white",
    cursor="hand2",
)
start_pause_btn.pack(side="left", padx=5)
reset_btn = tk.Button(
    btn_frame,
    text="重置",
    font=("Microsoft YaHei UI", 12, "bold"),
    command=reset_pomodoro,
    padx=20,
    pady=5,
    relief="flat",
    bg=accent_color,
    fg="white",
    activebackground="#ff8fa3",
    activeforeground="white",
    cursor="hand2",
)
reset_btn.pack(side="left", padx=5)

# 开始更新时间
update_time()

# 运行主循环
root.mainloop()
