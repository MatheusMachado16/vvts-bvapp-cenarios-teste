'''
UC001 - Visualizar grafico mensal de geracao por ano

Objetivo: Verificar que o Gestor visualiza o grafico de barras com a energia
gerada mes a mes no ano selecionado, consulta o valor exato de cada mes e
troca de ano sem recarregar a pagina.

Requisitos:
- RF29677 - Visualizacao e Exportacao Grafica de Geracao por Periodo (Epic 23761)
  - CA01 [29679], CA02 [29680], CA06 [29683]

Ator:
- Gestor

Autor: Matheus Yan Machado Santos
'''

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Gestor autenticado, com acesso a uma unica usina (ver [D02]).
# - A usina tem energia gerada coletada em todos os meses de 2025 e 2026
#   (exemplo: janeiro/2026 = 1.250,40 kWh).


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a tela de visualizacao grafica de geracao por periodo.
#
# O sistema exibe um seletor de ano e um grafico de barras. O ator verifica
# qual ano esta selecionado ao abrir a tela [D03].
#
# O ator verifica que o grafico mostra uma barra por mes, de janeiro a
# dezembro, e que cada barra representa o total de energia gerada (kWh)
# no mes, dentro do ano selecionado. [RN1]
#
# O ator posiciona o cursor sobre a barra de janeiro.
#
# O sistema exibe um tooltip com o valor exato em kWh e o mes/ano
# correspondente (ex.: "1.250,40 kWh - 01/2026"). [RN3]
#
# O ator repete o passo anterior para outros meses e verifica que cada
# tooltip mostra o valor e o mes/ano da barra sob o cursor.
#
# O ator altera o ano no seletor. [A1]


# [A1] - ALTERAR O ANO VISUALIZADO
# ---------------------------------------------------------------

# O ator abre o seletor de ano e escolhe outro ano (ex.: 2025).
#
# O sistema atualiza o grafico automaticamente, sem recarregar a pagina. [RN2]
#
# O ator verifica que continuam existindo 12 barras (janeiro a dezembro) e
# que os valores agora correspondem ao ano 2025.
#
# O ator posiciona o cursor sobre uma barra e verifica que o tooltip exibe
# o mes/ano de 2025.


# [RN1] - UMA BARRA POR MES (CA01)
# ---------------------------------------------------------------

# O grafico compara o total de energia gerada (kWh) mes a mes dentro do ano
# selecionado, com uma barra por mes, de janeiro a dezembro.

# [RN2] - ATUALIZACAO AUTOMATICA AO TROCAR O ANO (CA02)
# ---------------------------------------------------------------

# Ao alterar o ano no seletor, o grafico e atualizado automaticamente,
# sem recarregar a pagina.

# [RN3] - TOOLTIP COM VALOR EXATO (CA06)
# ---------------------------------------------------------------

# Ao passar o cursor sobre uma barra, o sistema exibe o valor exato em kWh
# e o mes/ano correspondente.


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Grafico com 12 barras (jan a dez) do ano selecionado.
# - Tooltip de cada barra com valor exato (kWh) e mes/ano.
# - Troca de ano atualiza o grafico sem recarregar a pagina.
#
# Duvidas relacionadas: D02, D03 (ver DUVIDAS.md)
