#__________________________________________________________________#

'''


Programa de contabilidade de salário


'''
#__________________________________________________________________#


#                         BIBLIOTECAS

#__________________________________________________________________#

import tkinter as tk
from tkinter import *
import customtkinter as ctk
from customtkinter import *



#__________________________________________________________________#


#                          BACKEND

#__________________________________________________________________#


class Functions:


    def limpardados(self):
        self.entry_horas.delete(0,END)
        self.entry_salario.delete(0, END)
        self.entry_totais.delete(0, END)




    def apagartexto(self):
        self.text_comentario.configure(state="normal")
        self.text_comentario.delete("0.0", tk.END)
        self.text_comentario.configure(state=DISABLED)
        self.limparsaldo()
        


    def coletabotao(self):

        self.apagartexto()
        self.limparsaldo()

        self.cliquebotao_horas = str(self.entry_horas.get()).strip()
        if self.cliquebotao_horas.isdigit():
           self.horas_diarias = int(self.cliquebotao_horas)
           self.endpoint1 = True
           pass
        else:
            self.horas_diarias = 0
            print("erro horas diarias") #_________________________#
            self.endpoint1 = False



        self.cliquebotao_escala = self.comboboxescala.get()
        if self.cliquebotao_escala == "5x2":
            self.escala = 20
            pass
        elif self.cliquebotao_escala == "6x1":
             self.escala = 24
             pass
        else:
            print("erro")
        print(self.escala, self.cliquebotao_horas)


        self.horasregistradas = str(self.entry_totais.get()).strip()
        if self.horasregistradas.isdigit():
            self.horasregistradas = int(self.horasregistradas)
            self.endpoint2 = True
            pass
        else:
            self.horasregistradas = 0
            print("erro horas registradas") #_________________________#
            self.endpoint2 = False


        self.salariobase = str(self.entry_salario.get()).strip()
        if self.salariobase.isdigit():
            self.salariobase = int(self.salariobase)
            self.endpoint3 = True
            pass
        else:
            self.salariobase = 0
            print("erro salario") #_________________________#
            self.endpoint3 = False

        if self.endpoint1 is True and self.endpoint2 is True and self.endpoint3 is True:
            self.calculosalario()
            self.salariopadrao()
            self.salario_desconto()
            self.salario_extra()
            self.mostrartexto()
            self.atualizarvalor()
            self.limpardados()



    def atualizarvalor(self):

        self.saldoadd = (f"R$ {self.salario_final}")
        self.valortotal.configure(text=self.saldoadd)

    def limparsaldo(self):

        self.removesaldo = (f"R$ 0,00")
        self.valortotal.configure(text=self.removesaldo)



    def calculosalario(self):

        self.valor_hora = self.salariobase//(self.horas_diarias*self.escala)

        self.salario_final = self.horasregistradas * self.valor_hora

        self.horas_esperadas = self.escala*self.horas_diarias

        self.desconto_ativo = True if self.horasregistradas < self.horas_esperadas else False

        self.adicional_ativo = True if self.horasregistradas > self.horas_esperadas else False

    
    def salariopadrao(self):

        if self.adicional_ativo == False and self.desconto_ativo is False:

            self.textopadrao = (f"\n O salário este mês é de: {self.salariobase} Reias \n\nNão possuindo nenhuma alteração de valor no salário! \n\nCom o total de horas esperadas sendo de: {self.horas_esperadas}h. ")
        else:
            pass

    def salario_desconto(self):

        self.horas_perdidas = self.horas_esperadas - self.horasregistradas

        self.dinheiro_perdido = self.salariobase - self.salario_final

        if self.desconto_ativo == True:

            self.textodesconto = (f"\nO salário este mês é de: {self.salario_final} Reais \n\nTendo um desconto de {self.dinheiro_perdido} Reias pelas: {self.horas_perdidas}h perdidas! \n\nCom o total de horas esperadas sendo de: {self.horas_esperadas}h! ")
        else:
            pass
        


    def salario_extra(self):

        self.horas_adicionais = self.horasregistradas - self.horas_esperadas

        self.dinheiro_adicional = self.salario_final - self.salariobase

        if self.adicional_ativo == True:
            
            self.textoadicional = (f"\nO salário este mês é de: {self.salario_final} Reais \n\nTendo um adicional de {self.dinheiro_adicional} Reias pelas: {self.horas_adicionais}h extras! \n\nCom o total de horas base sendo de: {self.horas_esperadas}h. ")
        else:
            pass



    





    def mostrartexto(self):

        # SALARIO PADRAO

    
        

        if self.salario_final == self.salariobase:
            self.text_comentario.configure(state="normal")
            self.text_comentario.insert("0.0", self.textopadrao)
            self.text_comentario.configure(state=DISABLED)

        elif self.salario_final > self.salariobase:
            self.text_comentario.configure(state="normal")
            self.text_comentario.insert("0.0", self.textoadicional)
            self.text_comentario.configure(state=DISABLED)
        elif self.salario_final < self.salariobase:
            self.text_comentario.configure(state="normal")
            self.text_comentario.insert("0.0", self.textodesconto)
            self.text_comentario.configure(state=DISABLED)
        else:
            self.text_comentario.configure(state="normal")
            self.text_comentario.insert("0.0", "Erro! Tente Novamente!")
            self.text_comentario.configure(state=DISABLED)

        
        




class Application(Functions):



    def __init__(self):
        self.janela = ctk.CTk()
        self.janelaprincipal()
        self.frame1()
        self.frame2()
        self.entradahoras()
        self.botao()
        self.labels()



        self.janela.mainloop()
        
    


    def janelaprincipal(self):
        
        ctk.set_appearance_mode("dark")
        self.janela.title("Python Salarial")
        self.janela.resizable(False, False)   
        largura = 800
        altura = 600
        tela_largura = self.janela.winfo_screenwidth()
        tela_altura = self.janela.winfo_screenheight()
        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")
        self.janela.configure(bg="White")


    def frame1(self):

        self.frameesquerda = CTkFrame(
            self.janela,
            bg_color= "transparent",   
            fg_color="white",
            corner_radius=25
        )
        self.frameesquerda.place(relx=0.05, rely=0.05, relwidth=0.47, relheight=0.9)

    def frame2(self):
        self.framedireita = CTkFrame(
            self.janela,
            bg_color="transparent",
            fg_color="White",
            corner_radius=25
        )
        self.framedireita.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.9)


    def entradahoras(self):

        self.entry_horas = CTkEntry(
            self.frameesquerda,
            bg_color="white",
            fg_color="#e6e6e6",
            corner_radius=27,
            border_width=4,
            border_color="#e6e6e6",
            placeholder_text="Insira suas horas diárias",
            placeholder_text_color="#6d6d6d",
            text_color="#3f3f3f"

        )
        self.entry_horas.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.07)


        self.entry_totais = CTkEntry(
            self.frameesquerda,
            bg_color="white",
            fg_color="#e6e6e6",
            corner_radius=27,
            border_width=4,
            border_color="#e6e6e6",
            placeholder_text="Insira suas horas registradas",
            placeholder_text_color="#6d6d6d",
            text_color="#3f3f3f"

        )
        self.entry_totais.place(relx=0.2, rely=0.56, relwidth=0.6, relheight=0.07)



        self.entry_salario = CTkEntry(
            self.frameesquerda,
            bg_color="white",
            fg_color="#e6e6e6",
            corner_radius=27,
            border_width=4,
            border_color="#e6e6e6",
            placeholder_text="Insira seu salario base",
            placeholder_text_color="#6d6d6d",
            text_color="#3f3f3f"

        )
        self.entry_salario.place(relx=0.2, rely=0.70, relwidth=0.6, relheight=0.07)




    def botao(self):

        self.btn_entrada = CTkButton(
            self.frameesquerda,
            bg_color="white",
            fg_color="#585858",
            text=">",
            text_color="Black",
            corner_radius=30,
            border_color="#585858",
            hover_color= "#ececec",
            command=self.coletabotao
            

        )
        self.btn_entrada.place(relx=0.15, rely=0.82, relwidth=0.7, relheight=0.1)



        self.btn_apagar = CTkButton(
            self.framedireita,
            bg_color="white",
            fg_color="#585858",
            text="APAGAR",
            text_color="Black",
            corner_radius=30,
            border_color="#585858",
            hover_color= "#ececec",
            command=self.apagartexto
            

        )
        self.btn_apagar.place(relx=0.15, rely=0.82, relwidth=0.7, relheight=0.1)





        self.comboboxescala = CTkComboBox(
            self.frameesquerda, 
            values=["6x1", "5x2"],
            bg_color="white",
            fg_color="#e6e6e6",
            border_width=0,
            corner_radius=12,
            text_color="black"
        )
        self.comboboxescala.set("5x2")
        self.comboboxescala.place(relx=0.32, rely=0.41)
            



    def labels(self):

        self.label_horas = CTkLabel(
            self.frameesquerda,
            text="HORAS DIÁRIAS",
            font=("Segoe IU", 12, "bold"),
            text_color="black",
            bg_color="transparent"
        )
        self.label_horas.place(relx=0.39, rely=0.19)

        self.label_escala = CTkLabel(
            self.frameesquerda,
            text="ESCALA DE TRABALHO",
            font=("Segoe IU", 12, "bold"),
            text_color="black"
        )
        self.label_escala.place(relx=0.34, rely=0.35)

        self.label_totais = CTkLabel(
            self.frameesquerda,
            text="HORAS REGISTRADAS",
            font=("Segoe IU", 12, "bold"),
            text_color="black"
        )
        self.label_totais.place(relx=0.34, rely=0.5)

        self.label_salario = CTkLabel(
            self.frameesquerda,
            text="SALÁRIO",
            font=("Segoe IU", 12, "bold"),
            text_color="black"
        )
        self.label_salario.place(relx=0.43, rely=0.64)

        self.label_titulo = CTkLabel(
            self.frameesquerda,
            text="CALCULADORA DE SALÁRIO",
            font=("Segoe IU", 20, "bold"),
            text_color="black",
            bg_color="transparent"
        )
        self.label_titulo.place(relx=0.15, rely=0.07)

        self.text_comentario = CTkTextbox(
            self.framedireita,
            fg_color="#e6e6e6",
            text_color="black"
            
        )
        self.text_comentario.configure(state=DISABLED)
        self.text_comentario.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.3)

        self.label_titulo2 = CTkLabel(
            self.framedireita,
            text="RESULTADOS",
            font=("Segoe IU", 20, "bold"),
            text_color="black",
            bg_color="transparent"
        )
        self.label_titulo2.place(relx=0.29, rely=0.07)




        self.label_seusalario = CTkLabel(
            self.framedireita,
            text="SEU SALÁRIO:",
            font=("Segoe IU", 12, "bold"),
            text_color="black"
        )
        self.label_seusalario.place(relx=0.36, rely=0.18)


        self.valortotal = CTkLabel(
            self.framedireita,
            text="R$ 0,00",
            font=("Segoe IU", 12, "bold"),
            text_color="black"
        )
        self.valortotal.place(relx=0.40, rely=0.22)








    

















       
        

































Application()


