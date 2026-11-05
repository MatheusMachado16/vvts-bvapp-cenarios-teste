'''
UC003 - Exibir meses sem dados no grafico de geracao

Objetivo: Verificar que meses sem dados coletados aparecem no grafico como
barra zerada, com indicacao visual diferenciada e sem gerar erro.

Requisitos:
- RF29677 - Visualizacao e Exportacao Grafica de Geracao por Periodo (Epic 23761)
  - CA05 [29682]

Ator:
- Gestor

Autor: Matheus Yan Machado Santos
'''

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Gestor autenticado, com acesso a uma unica usina.
# - Ano de teste: 2026, com dados coletados de janeiro a junho e SEM nenhum
#   dado coletado de julho a dezembro.


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a tela de visualizacao grafica de geracao por periodo e
# seleciona o ano 2026.
#
# O sistema exibe o grafico sem mensagem de erro. [RN1]
#
# O ator verifica que janeiro a junho exibem barras com os valores gerados.
#
# O ator verifica que julho a dezembro aparecem como barra zerada, com
# indicacao visual diferenciada das barras com dados (cor ou hachura). [RN1] [D04]
#
# O ator posiciona o cursor sobre a barra de julho e verifica que o
# tooltip mostra 0 kWh e o mes/ano "07/2026".  [CA06 - ver UC001]


# [A1] - ANO SEM NENHUM DADO COLETADO
# ---------------------------------------------------------------

# O ator seleciona um ano em que nao ha dados coletados em nenhum mes.
# (A disponibilidade desse ano no seletor depende de [D03].)
#
# O sistema exibe os 12 meses como barra zerada com a indicacao diferenciada,
# sem gerar erro, conforme CA05 aplicado a cada mes.


# [RN1] - MESES SEM DADOS (CA05)
# ---------------------------------------------------------------

# Meses sem dados coletados sao exibidos com barra zerada, com indicacao
# visual diferenciada (ex.: cor ou hachura), e sem gerar erro.
# Qual e a indicacao visual nao esta definida: ver D04.


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Meses com dados: barras com o valor.
# - Meses sem dados: barra zerada, visualmente diferenciada.
# - Nenhuma mensagem de erro, nenhuma quebra do grafico.
#
# Duvidas relacionadas: D03, D04 (ver DUVIDAS.md)
