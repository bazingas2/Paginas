import tkinter as tk
from tkinter import simpledialog, filedialog
import time
from math import pi, sin, cos
import threading
import pygame


class RelogioAlarme:
    def __init__(self, root):
        self.root = root
        self.root.title("Relógio Analógico e Digital com Alarme")

        self.canvas = tk.Canvas(root, width=300, height=350, bg="white")
        self.canvas.pack()

        self.botao_alarme = tk.Button(root, text="Configurar Alarme", command=self.configurar_alarme)
        self.botao_alarme.pack()

        self.alarme_horas = None
        self.alarme_minutos = None
        self.alarme_som = None

        self.desenhar_moldura_relogio()
        self.atualizar_relogio()
        threading.Thread(target=self.verificar_alarme, daemon=True).start()

    def configurar_alarme(self):
        self.alarme_horas = simpledialog.askinteger("Configurar Alarme", "Horas (0-23):", minvalue=0, maxvalue=23)
        self.alarme_minutos = simpledialog.askinteger("Configurar Alarme", "Minutos (0-59):", minvalue=0, maxvalue=59)
        self.alarme_som = filedialog.askopenfilename(title="Selecione o som do alarme",
                                                     filetypes=[("Arquivos de Áudio", "*.mp3 *.wav")])

    def verificar_alarme(self):
        while True:
            hora_atual = time.localtime()
            if self.alarme_horas == hora_atual.tm_hour and self.alarme_minutos == hora_atual.tm_min:
                if self.alarme_som:
                    pygame.mixer.init()
                    pygame.mixer.music.load(self.alarme_som)
                    pygame.mixer.music.play()
                    print("Alarme! Hora de acordar!")
                else:
                    print("Alarme! Hora de acordar! (Sem som configurado)")
                break
            time.sleep(1)

    def atualizar_relogio(self):
        self.canvas.delete("ponteiros", "horario_digital")
        hora, minuto, segundo = time.localtime().tm_hour % 12, time.localtime().tm_min, time.localtime().tm_sec

        angulos = {
            'horas': pi / 2 - 2 * pi * (hora + minuto / 60) / 12,
            'minutos': pi / 2 - 2 * pi * minuto / 60,
            'segundos': pi / 2 - 2 * pi * segundo / 60
        }

        tamanhos = {'horas': 50, 'minutos': 70, 'segundos': 90}
        cores = {'horas': "black", 'minutos': "blue", 'segundos': "red"}
        larguras = {'horas': 6, 'minutos': 4, 'segundos': 2}

        for tipo in ['horas', 'minutos', 'segundos']:
            x = 150 + tamanhos[tipo] * cos(angulos[tipo])
            y = 150 - tamanhos[tipo] * sin(angulos[tipo])
            self.canvas.create_line(150, 150, x, y, width=larguras[tipo], fill=cores[tipo], tags="ponteiros")

        horario_atual = time.strftime("%H:%M:%S")
        self.canvas.create_text(150, 280, text=horario_atual, font=("Arial", 16, "bold"), fill="black",
                                tags="horario_digital")

        self.root.after(1000, self.atualizar_relogio)

    def desenhar_moldura_relogio(self):
        self.canvas.create_oval(50, 50, 250, 250, outline="black", width=3)
        for i in range(12):
            angulo = pi / 2 - 2 * pi * i / 12
            x_inicio, y_inicio = 150 + 85 * cos(angulo), 150 - 85 * sin(angulo)
            x_fim, y_fim = 150 + 95 * cos(angulo), 150 - 95 * sin(angulo)
            self.canvas.create_line(x_inicio, y_inicio, x_fim, y_fim, width=3)


if __name__ == "__main__":
    root = tk.Tk()
    RelogioAlarme(root)
    root.mainloop()
