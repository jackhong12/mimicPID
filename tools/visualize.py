#!python3
import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str, help='csv input file')
parser.add_argument('-o', type=str, default='', help='image name')
args = parser.parse_args()

df = pd.read_csv(args.input_file)
label = df.keys().values.tolist()
x = df[label[0]].values.tolist()
colors = ['c', 'r', 'b', 'g', 'm', 'y']
for i in range(1, len(label)):
    y = df[label[i]].values.tolist()
    plt.plot(x, y, label=label[i], color=colors[i % len(colors)])
plt.legend(loc='best', fontsize=20)
if args.o:
    plt.savefig(args.o)
plt.show()
