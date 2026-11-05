'''
UC004 - Exibir linha de referencia com a media mensal de geracao

Objetivo: Verificar que o grafico exibe uma referencia visual com a media
mensal de geracao do ano selecionado, permitindo identificar os meses
abaixo do esperado.

Requisitos:
- RF29677 - Visualizacao e Exportacao Grafica de Geracao por Periodo (Epic 23761)
  - CA07 [29684]

Ator:
- Gestor

Autor: Matheus Yan Machado Santos
'''

# ATENCAO: o CA07 nao define o calculo da media, a forma da referencia
# ("linha ... ou indicador visual") nem o que e "esperado". Os passos abaixo
# seguem o texto do criterio; os valores exatos ficam pendentes de [D05] e [D06].

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Gestor autenticado, com acesso a uma unica usina.
# - Ano 2026 com dados em todos os meses; um mes (ex.: marco) com geracao
#   claramente menor que os demais.


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a tela de visualizacao grafica de geracao por periodo e
# seleciona o ano 2026.
#
# O sistema exibe o grafico de barras com uma linha de referencia ou
# indicador visual com a media mensal de geracao de 2026. [RN1] [D05]
#
# O ator verifica que a referencia esta posicionada no valor da media
# mensal do ano (valor a ser conferido conforme o calculo definido em D05/D06).
#
# O ator compara cada barra com a referencia e identifica que a barra de
# marco esta abaixo dela.  [RN1]


# [A1] - ALTERAR O ANO
# ---------------------------------------------------------------

# O ator seleciona outro ano no seletor.
#
# O sistema atualiza o grafico e a referencia passa a mostrar a media
# mensal do novo ano selecionado. [RN1]


# [A2] - ANO COM MESES SEM DADOS
# ---------------------------------------------------------------

# O ator seleciona um ano com meses sem dados coletados (ver UC003).
#
# O sistema exibe a referencia. Se os meses sem dados entram na media como
# zero ou ficam fora dela NAO esta definido. [D06]


# [RN1] - REFERENCIA DA MEDIA MENSAL (CA07)
# ---------------------------------------------------------------

# O grafico exibe linha de referencia ou indicador visual com a media mensal
# de geracao do ano selecionado, para identificar rapidamente os meses
# abaixo do esperado. Calculo da media e definicao de "esperado": ver D05, D06.


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Referencia visivel no grafico, relativa ao ano selecionado.
# - Barras abaixo da referencia identificaveis visualmente.
# - Ao trocar o ano, a referencia acompanha o novo ano.
#
# Duvidas relacionadas: D05, D06 (ver DUVIDAS.md)
