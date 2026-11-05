'''
UC007 - Listar e filtrar eventos dos inversores

Objetivo: Verificar que o usuario aplica filtros por periodo, nivel de
severidade, inversor e/ou usina e visualiza apenas os eventos correspondentes.

Requisitos:
- RF23884 - Listagem e filtros de eventos (Epic 23766)
  - CA01 [24852]

Ator:
- Gestor (os demais perfis de acesso estao no UC010)

Autor: Matheus Yan Machado Santos
'''

# ATENCAO: os niveis de severidade nao sao definidos no requisito e o
# atributo nao consta no registro do evento (24842). Os passos que usam
# severidade ficam pendentes de [D11].

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Eventos registrados em duas usinas ("Usina A", "Usina B"), com mais de um
#   inversor cada, em datas diferentes (ex.: 05/10/2026 e 20/10/2026).
# - Eventos com tipos/descricoes variados (campos de 24842: ID do inversor,
#   usina, timestamp de ocorrencia, tipo e descricao).


# [FP] - FLUXO PRINCIPAL (filtros combinados)
# ---------------------------------------------------------------

# O ator acessa a pagina de listagem de eventos.
#
# O sistema exibe a listagem e os campos de filtro: data de inicio, data de
# fim, nivel de severidade, inversor e usina.
#
# O ator informa data de inicio 01/10/2026 e data de fim 15/10/2026, a
# "Usina A" e um dos inversores dessa usina, e um nivel de severidade [D11],
# e aplica o filtro.
#
# O sistema exibe somente os eventos que atendem a todos os filtros
# informados. [RN1]
#
# O ator verifica que cada evento listado esta dentro do periodo, pertence
# a usina e ao inversor escolhidos e ao nivel de severidade informado.


# [A1] - FILTRAR SOMENTE POR PERIODO
# ---------------------------------------------------------------

# O ator informa so a data de inicio e a data de fim e aplica o filtro.
#
# O sistema exibe todos os eventos do periodo, de qualquer usina e inversor.


# [A2] - FILTRAR SOMENTE POR USINA
# ---------------------------------------------------------------

# O ator seleciona a "Usina B" e aplica o filtro.
#
# O sistema exibe somente eventos da Usina B.


# [A3] - FILTRAR SOMENTE POR INVERSOR
# ---------------------------------------------------------------

# O ator seleciona um inversor e aplica o filtro.
#
# O sistema exibe somente eventos desse inversor.


# [A4] - FILTRAR SOMENTE POR NIVEL DE SEVERIDADE
# ---------------------------------------------------------------

# O ator seleciona um nivel de severidade e aplica o filtro.
#
# O sistema exibe somente eventos desse nivel. Pendente: niveis nao definidos. [D11]


# [RN1] - FILTROS DA LISTAGEM (CA01)
# ---------------------------------------------------------------

# O usuario pode filtrar por periodo (data inicio/fim), nivel de severidade,
# inversor e/ou usina, e visualiza os eventos correspondentes.
# Se os filtros sao opcionais, valores padrao e datas inconsistentes
# (inicio > fim): ver D14.


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Listagem contem apenas eventos que atendem aos filtros aplicados.
#
# Duvidas relacionadas: D11, D14 (ver DUVIDAS.md)
