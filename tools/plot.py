import os
import re
import matplotlib.pyplot as plt
import mplcursors

def extract_float_numbers(line):
    """
    从包含"AP: "后的第一个浮点数的行中提取浮点数。
    """
    match = re.search(r'AP: (\d+\.\d+)', line)
    if match:
        return float(match.group(1))
    else:
        return None

def read_log_file(file_path):
    """
    读取日志文件，并提取浮点数。
    """
    float_numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            if "Epoch(val)" in line:
                number = extract_float_numbers(line)
                if number is not None:
                    float_numbers.append(number)
    return float_numbers

def plot_line_chart(float_numbers):
    """
    绘制折线图。
    """
    _, ax = plt.subplots()
    ax.plot(range(len(float_numbers)), float_numbers)
    ax.set(xlabel='Index', ylabel='Value', title='Line Chart')
    ax.set_xlim(0, 25)
    ax.set_ylim(0.4, 0.75)

    # 标注数据点
    for i, value in enumerate(float_numbers):
        ax.annotate(f'{value:.2f}', (i, value), textcoords="offset points", xytext=(0,10), ha='center', fontsize=2)

    # 添加交互式标签

colorss = ['g', 'r', 'c', 'm', 'y', 'k', 'b']
offs = -20
def main():
    # 获取当前目录下的.log文件
    log_files = [f for f in os.listdir() if f.endswith('.log')]

    _, ax = plt.subplots()
    ax.set(xlabel='epoch/10', ylabel='AP', title='Line Chart')
    ax.set_xlim(0, 25)
    ax.set_ylim(0.5, 0.75)

    for j, pa in enumerate(log_files):
        log_file_path = pa
        float_numbers = read_log_file(log_file_path)
        ax.plot(range(len(float_numbers)), float_numbers, color=colorss[j % len(colorss)])
        for i, value in enumerate(float_numbers):
            ax.annotate(f'{value:.3f}', (i, value), textcoords="offset points", xytext=(0, offs + 40 * j), ha='center')


    mplcursors.cursor(hover=True)

    plt.show()

if __name__ == "__main__":
    main()
