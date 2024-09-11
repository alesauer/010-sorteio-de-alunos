"""
Programa para ler um arquivo CSV de alunos e sortear 10 nomes aleatórios.
Versão: 1.97
Autor: Prof. Sauer
Site: www.sauer.pro.br
Email: sauer@simplificatreinamentos.com.br
Instagram: https://www.instagram.com/prof.alesauer/
Facebook: https://www.facebook.com/prof.alesauer
YouTube:  https://www.youtube.com/@prof.alesauer
LinkedIn: www.linkedin.com/in/alesauer
"""

import csv
import random

def ler_alunos_csv(nome_arquivo):
    """
    Lê um arquivo CSV contendo uma coluna de nomes de alunos.
    
    Args:
    nome_arquivo (str): Caminho para o arquivo CSV a ser lido.
    
    Returns:
    list: Lista com os nomes dos alunos.
    """
    alunos = []
    
    # Abrindo o arquivo CSV
    with open(nome_arquivo, mode='r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        
        # Itera sobre cada linha e adiciona o nome à lista
        for linha in leitor_csv:
            alunos.append(linha['alunos'])
    
    return alunos

def sortear_alunos(alunos, quantidade=10):
    """
    Sorteia uma quantidade especificada de alunos da lista.
    
    Args:
    alunos (list): Lista de nomes de alunos.
    quantidade (int): Número de alunos a serem sorteados.
    
    Returns:
    list: Lista com os nomes dos alunos sorteados.
    """
    return random.sample(alunos, quantidade)

# Executando o programa
if __name__ == "__main__":
    nome_arquivo = 'alunos.csv'
    
    # Lendo o arquivo CSV para obter a lista de alunos
    lista_alunos = ler_alunos_csv(nome_arquivo)
    
    # Sorteando 10 alunos aleatoriamente
    alunos_sorteados = sortear_alunos(lista_alunos, 10)
    
    # Exibindo os alunos sorteados
    print("Alunos sorteados:")
    for aluno in alunos_sorteados:
        print(aluno)
