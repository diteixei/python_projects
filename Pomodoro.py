import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style

# Alterando os tempos de trabalho e descanso
WORK_TIME = 30 * 60
SHORT_BREAK_TIME = 10 * 60
LONG_BREAK_TIME = 20 * 60
ADJUSTMENT_TIME = 5 * 60

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.title("Pomodoro Timer")
        self.style = Style(theme="simplex")
        self.style.theme_use()

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont"))
        self.timer_label.pack(pady=20)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.adjust_button = ttk.Button(self.root, text="Adiantar Descanso", command=self.adjust_break_time)
        self.adjust_button.pack(pady=5)

        self.add_five_button = ttk.Button(self.root, text="Adicionar 5 Minutos", command=self.add_five_minutes)
        self.add_five_button.pack(pady=5)

        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK_TIME
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def adjust_break_time(self):
        self.break_time -= ADJUSTMENT_TIME
        if self.break_time < 0:
            self.break_time = 0
        messagebox.showinfo("Ajuste de Descanso", f"Tempo de descanso adiantado em {ADJUSTMENT_TIME / 60} minutos!")

    def add_five_minutes(self):
        self.work_time += 5 * 60
        messagebox.showinfo("Adicionar 5 Minutos", "Tempo de trabalho aumentado em 5 minutos!")

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoros_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Bom trabalho!" if self.pomodoros_completed % 4 == 0
                                        else "Bom trabalho!", "Faça uma pausa demorada e descanse o cérebro"
                                        if self.pomodoros_completed % 4 == 0
                                        else "Faça uma pequena pausa e estique as pernas!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("Hora de trabalhar", "Volte ao trabalho!")
            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)

PomodoroTimer()
