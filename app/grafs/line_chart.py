import matplotlib.ticker as ticker
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import io


class LineChart:
    colors = {'s1': 'limegreen', 's2': 'yellowgreen', 's3': 'gold', 's4': 'darkorange', 'LT': 'red', 's5': 'black'}
    zones = {'s2':133, 's3':149, 's4':160, 'LT':165, 's5':170, 'HRmax':180}

    def __init__(self, title: str):
        self.fig, self.ax = plt.subplots()
        self.title = title

    def show(self):
        self.fig.show()
        plt.show(block=True)

    def save_to_file(self, file_path):
        self.fig.savefig(file_path)

    def save_to_buffer(self):
        buffer = io.BytesIO()
        self.fig.savefig(buffer, format='jpg')
        buffer.seek(0)
        return buffer

    def plot(self, hr: list[int]):
        self.ax.set_title(self.title)
        self.ax.set_xlim(0, len(hr))    # powoduje, że wykres będzie idealnie zaczynał się i kończył dla X

        x = range(len(hr))
        self._draw_line(x, hr)

        self._set_x_labels(x)
        self._set_horizontal_lines()

    def _draw_line(self, x, hr):
        # Rysowanie linii z kolorami według stref tętna
        for i in range(len(x) - 1):
            # Określanie koloru dla segmentu linii na podstawie średniej wartości tętna
            avg_hr = (hr[i] + hr[i + 1]) / 2
            
            if avg_hr < self.zones['s2']:
                color = self.colors['s1']
            elif avg_hr < self.zones['s3']:
                color = self.colors['s2']
            elif avg_hr < self.zones['s4']:
                color = self.colors['s3']
            elif avg_hr < self.zones['LT']:
                color = self.colors['s4']
            elif avg_hr < self.zones['s5']:
                color = self.colors['LT']
            else:
                color = self.colors['s5']
            
            self.ax.plot(x[i:i + 2], hr[i:i + 2], color=color, linewidth=1.2)

    @staticmethod
    def _calc_x_ticks(x):
        steps = 10

        result = [x[0]]
        x_max = x[-1]
        minute_steps = [1, 2, 5, 10, 15, 20, 30, 60]
        for step in minute_steps:
            x_step = step * 60
            calc = x_max / x_step
            # decide if additional step needed
            if calc % 1 > 0.4:
                calc = int(calc) + 1
            else:
                calc = int(calc)
            if calc <= steps:
                result.extend(range(x_step, x_step*calc, x_step))
                break
        result.append(x_max)
        return result

    def _set_x_labels(self, x):
        x_step = self._calc_x_ticks(x)
        self.ax.set_xticks(x_step)
        self.ax.xaxis.set_major_formatter(ticker.FuncFormatter(self._format_func))
        for label in self.ax.get_xticklabels():
            label.set_fontsize(8)
        labels = self.ax.get_xticklabels()

    def _set_ahline_with_text(self, zone, color='k', linewidth=0.2, text_above_line=1, increase_fontsize=0):
        label_start_x = 46
        label_font_size = 6

        self.ax.axhline(y=self.zones[zone], color=color, linestyle='-', linewidth=linewidth)
        label_text = str(self.zones[zone]) + ': ' + zone.replace('s', 'Zone ')
        self.ax.text(x=label_start_x, y=self.zones[zone] + text_above_line, s=label_text, color=color, fontsize=label_font_size + increase_fontsize, alpha=0.8)

    def _set_horizontal_lines(self):
        self._set_ahline_with_text('LT', color='r', linewidth=0.8, increase_fontsize=2)
        self._set_ahline_with_text('HRmax', linewidth=0.7, text_above_line=0.5, increase_fontsize=2)    
        self._set_ahline_with_text('s5') 
        self._set_ahline_with_text('s4') 
        self._set_ahline_with_text('s3') 
        self._set_ahline_with_text('s2') 

    @staticmethod
    def _format_func(value, tick_number):
        minutes = int(value // 60)
        seconds = int(value % 60)
        return f'{minutes:02d}:{seconds:02d}'