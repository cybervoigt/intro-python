"""
Exemplo de manipulação de arquivos CSV e planilha Excel com Python,
Autor Ricardo Voigt (https://github.com/cybervoigt)
Data 26/11/22
Versão 0.0.0.1

Minha ideia então, pegar o arquivo CSV disponível no site da 
Secretaria de Segurança Pública com dados de ocorrências policiais
(https://www.ssp.rs.gov.br/dados-abertos - acessado em 26/11/2022 08:00)
o arquivo 'SPJ_DADOS_ABERTOS_OCORRENCIAS_jan-out2022.csv' foi renomeado para 'ssp_dados.csv'

Pensei em ler os dados e criar uma planilha contendo um resumo tipo MATRIZ
somente da cidade de SANTA CRUZ DO SUL,
onde as LINHAS são os "Tipos de Enquadramento" (coluna E),
e as COLUNAS são os Bairros (coluna I)

OBS: os nomes dos bairros estão despadronizados e repetidos,
    provavelmente devido a necessidade de digitação,
    mas por enquanto não vou tratar isso,
    apenas testei se está em branco e apliquei uppercase.
"""

cidade = "SANTA CRUZ DO SUL"

import ler_csv
import processamento
import gravar_planilha


def main():
    
    # entrada-> ler dados do CSV

    #conta = lerdadoscsv.contador_cidade(cidade)
    #print(f"contador = {conta}")

    dados = ler_csv.lista_eixos(cidade)
    linhas = dados[0]
    colunas = dados[1]

    print(f"\nquantidade de TIPOS na lista: {len(linhas)}")
    print(f"\nquantidade de BAIRROS na lista: {len(colunas)}")

    # cria a matriz contando os tipos de ocorrencia em cada bairro
    matriz1 = ler_csv.contar_dados(cidade,linhas,colunas)
    # print(matriz)


    # processamento - totalizar linhas e colunas e inserir o título (coluna A) em cada linha

    # posição zero será a coluna A, então adiciona 
    # um item vazio para ser a primeira celula da coluna A
    colunas.insert(0,"")
    colunas.append("TOTAL")
    processamento.total_linhas(matriz1)

    linhas.append("TOTAL")
    processamento.total_colunas(matriz1)

    processamento.ajuste_titulo_coluna(matriz1,linhas)


    # saida
    nomearq = gravar_planilha.salvar_planilha(cidade,linhas,colunas,matriz1)

    print(f"FIM ! Planilha: {nomearq}")

if __name__ == "__main__":
    main()
