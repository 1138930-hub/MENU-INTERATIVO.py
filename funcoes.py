import os #ajuda a criar pastas ou arquivos se não existirem.
from datetime import datetime #serve para registrar data e hora nos logs.

# Caminhos dos arquivos 

ARQUIVOS_DADOS = "dados/estoque.csv"
ARQUIVO_LOG = "dados/log.txt"

# Lista de vai guardar os produtos em memória 
estoque = []  