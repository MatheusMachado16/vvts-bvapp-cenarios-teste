'''
UC002 - Filtrar grafico de geracao por usina

Objetivo: Verificar que o Gestor com acesso a mais de uma usina precisa
escolher a usina antes de o grafico de geracao ser exibido.

Requisitos:
- RF29677 - Visualizacao e Exportacao Grafica de Geracao por Periodo (Epic 23761)
  - CA03 [29681]

Ator:
- Gestor com acesso a mais de uma usina

Autor: Matheus Yan Machado Santos
'''

# ATENCAO: o texto do CA03 diz que "o filtro (periodo) e obrigatorio", mas
# o criterio trata de filtro por usina. Este cenario usa a leitura provisoria
# "a selecao da usina e obrigatoria" e fica pendente de [D01].

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Gestor autenticado com acesso as usinas "Usina A" e "Usina B".
# - Ambas com energia gerada coletada em 2026.


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a tela de visualizacao grafica de geracao por periodo.
#
# O sistema exibe o filtro de usina com as usinas as quais o ator tem acesso
# (Usina A e Usina B).
#
# O ator verifica que o grafico NAO e exibido enquanto nenhuma usina foi
# selecionada. [RN1] [D01]
#
# O ator seleciona "Usina A" no filtro.
#
# O sistema exibe o grafico de barras com a geracao mensal da Usina A.
#
# O ator seleciona "Usina B" no filtro. [A1]
#
# O sistema exibe o grafico com a geracao mensal da Usina B.
#
# O ator verifica que os valores das barras mudaram em relacao a Usina A.


# [A1] - ACESSO A UMA UNICA USINA
# ---------------------------------------------------------------

# O ator e um Gestor com acesso a apenas uma usina e acessa a tela de
# visualizacao grafica.
#
# O comportamento do sistema neste caso (exibir o grafico direto ou tambem
# pedir a selecao) NAO esta descrito no requisito. [D02]
# O CA03 so impoe o filtro "quando possui acesso a mais de uma usina".


# [RN1] - SELECAO OBRIGATORIA COM MAIS DE UMA USINA (CA03)
# ---------------------------------------------------------------

# Quando o Gestor possui acesso a mais de uma usina, o filtro e obrigatorio
# antes de exibir o grafico. (Termo "periodo" no texto original: ver D01.)


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Sem usina selecionada: grafico nao exibido.
# - Com usina selecionada: grafico exibe apenas os dados dessa usina.
#
# Duvidas relacionadas: D01, D02 (ver DUVIDAS.md)
