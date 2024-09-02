#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import tkinter as tk
import subprocess
import signal
import os


class Gui(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("gui") # MODIFY NAME

        self.crearVentana()

    def usar_webcam(self):
        comandoWebcam = 'ros2 launch parcial1 parcial1_camara.launch.py'
        self.get_logger().info("Ejecutando comando para usar la webcam")

        self.resultado = subprocess.Popen([comandoWebcam], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, preexec_fn=os.setsid)

               

    def seleccionar_video(self):
        comandoVideo = 'ros2 launch parcial1 parcial1_video.launch.py'
        self.get_logger().info("Ejecutando comando para seleccionar un video")

        self.resultado = subprocess.Popen([comandoVideo], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, preexec_fn=os.setsid)

       
    def salir(self):
        os.killpg(os.getpgid(self.resultado.pid), signal.SIGINT)
        


    def crearVentana(self):
        ventana = tk.Tk()
        ventana.title("Sistema de Percepción")

        # Texto superior
        etiqueta_superior = tk.Label(ventana, text="Parcial 1 Percepción robótica Jhon Edward Gonzalez - Juan Sebastian Burbano")
        etiqueta_superior.pack(pady=10)


        ventana.geometry("600x400")

        canvas = tk.Canvas(ventana, height=400, width=600)
        canvas.pack()

        btn_usar_webcam = tk.Button(canvas, text="Usar Webcam", command=self.usar_webcam, height=5, width=20)
        btn_seleccionar_video = tk.Button(canvas, text="Seleccionar Video", command=self.seleccionar_video, height=5, width=20)
        btn_salir = tk.Button(canvas, text="Terminar proceso", command=self.salir, height=5, width=20)

        canvas.create_window(150, 150, window=btn_usar_webcam)
        canvas.create_window(450, 150, window=btn_seleccionar_video)
        canvas.create_window(300, 300, window=btn_salir)

        # Agregar texto en la parte inferior
        #texto = tk.Label(ventana, text="Parcial 1 Percepción robótica Jhon Edward Gonzalez - Juan Sebastian Burbano")
        #texto.pack(side="bottom")

        ventana.mainloop()





    


def main(args=None):
    rclpy.init(args=args)
    node = Gui() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
