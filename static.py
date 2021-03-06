from bokeh.plotting import figure, output_file, show
import numpy as np

# Anzahl der Datenpunkte
N = 5
# Daten für X-Achse als lineare Abfolge zwischen 1 und 3
x = np.linspace(1,3,N)
# Daten der Y-Achse, als Sinus der x-Stützstellen
y = np.sin(x)

# Der Ausgabe-File und dessen Titel
output_file("lines.html", title="line plot example")

# Der Plot 
plot = figure(title="line example", x_axis_label='x', y_axis_label='y')
# Die Datenreihe
plot.line(x, y, legend="Temp.", line_width=2)

# Kommando um den Browser automatisch zu öffnen und "lines.html" anzuzeigen
show(plot)