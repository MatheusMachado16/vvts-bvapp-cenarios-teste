'''
UC005 - Exportar grafico de geracao (JPEG ou PDF)

Objetivo: Verificar que o Gestor exporta o grafico de geracao exibido como
imagem JPEG ou como arquivo PDF.

Requisitos:
- RF29677 - Visualizacao e Exportacao Grafica de Geracao por Periodo (Epic 23761)
  - CA08 [29685]

Ator:
- Gestor

Autor: Matheus Yan Machado Santos
'''

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Gestor autenticado, com o grafico de geracao de 2026 ja exibido
#   (usina selecionada, se houver mais de uma).


# [FP] - FLUXO PRINCIPAL (exportar como JPEG)
# ---------------------------------------------------------------

# O ator, com o grafico de geracao exibido, seleciona a opcao de exportar o
# grafico.
#
# O sistema oferece os formatos de exportacao: imagem (JPEG) e PDF. [RN1]
#
# O ator escolhe o formato JPEG.
#
# O sistema gera o arquivo de imagem JPEG com o grafico.
#
# O ator abre o arquivo e verifica que ele contem o grafico exibido na tela
# (ano e dados correspondentes ao que estava selecionado). [D08]


# [A1] - EXPORTAR COMO PDF
# ---------------------------------------------------------------

# O ator, com o grafico exibido, seleciona exportar e escolhe o formato PDF.
#
# O sistema gera o arquivo PDF com o grafico.
#
# O ator abre o arquivo e verifica que ele contem o grafico exibido. [D08]


# [A2] - FALHA NA EXPORTACAO
# ---------------------------------------------------------------

# O requisito NAO descreve o que acontece se a exportacao falhar (a
# exportacao de medicoes, em 25105, preve mensagem de erro; este criterio
# nao). Fluxo pendente de definicao. [D07]


# [RN1] - FORMATOS DE EXPORTACAO (CA08)
# ---------------------------------------------------------------

# O Gestor pode exportar o grafico como imagem (JPEG) ou como arquivo PDF.


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Arquivo .jpg gerado com o grafico (fluxo principal).
# - Arquivo .pdf gerado com o grafico (A1).
#
# Duvidas relacionadas: D07, D08 (ver DUVIDAS.md)
