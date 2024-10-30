import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta:")

lista_arquivos = os.listdir(caminho)

locais = {
    "Imagens": [".png", ".jpg"],
    "PDF": [".pdf"],
    "csv": [".csv"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.sliptext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename (f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            
