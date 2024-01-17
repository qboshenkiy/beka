import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BusinessChartApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Business Chart App")

        self.file_path_label = tk.Label(master, text="Выберите файл с данными")
        self.file_path_label.pack()

        self.choose_file_button = tk.Button(master, text="Выбрать файл", command=self.choose_file)
        self.choose_file_button.pack()

        self.plot_button = tk.Button(master, text="Построить диаграмму", command=self.plot_income_chart)
        self.plot_button.pack()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack()

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.file_path_label.config(text=f"Выбранный файл: {file_path}")
            self.file_path = file_path

    def plot_income_chart(self):
        if not hasattr(self, 'file_path'):
            self.file_path_label.config(text="Выберите файл перед построением диаграммы.")
            return

        try:
            df = pd.read_csv(self.file_path, delimiter=';', encoding='windows-1251')
        except Exception as e:
            self.file_path_label.config(text=f"Ошибка чтения файла: {str(e)}")
            return

        if df.empty or 'Business' not in df.columns or 'Revenue' not in df.columns:
            self.file_path_label.config(text="Данные в файле недостаточны для построения диаграммы.")
            return

        self.ax.clear()
        df.plot(x='Business', y='Revenue', kind='bar', ax=self.ax, legend=False)
        self.ax.set_title('Диаграмма доходов')
        self.ax.set_xlabel('Категория бизнеса')
        self.ax.set_ylabel('Доход')

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = BusinessChartApp(root)
    root.mainloop()
