'''
UC009 - Informar ausencia de eventos para os filtros aplicados

Objetivo: Verificar que o sistema exibe mensagem informativa quando nenhum
evento e encontrado para os filtros aplicados.

Requisitos:
- RF23884 - Listagem e filtros de eventos (Epic 23766)
  - CA03 [24855]

Ator:
- Gestor

Autor: Matheus Yan Machado Santos
'''

# ATENCAO: o texto da mensagem nao esta definido no requisito. O resultado
# esperado registra apenas que uma mensagem informativa e exibida. [D13]

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Existem eventos cadastrados, mas nenhum no periodo 01/01/2020 a 31/01/2020.


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a pagina de listagem de eventos.
#
# O ator informa data de inicio 01/01/2020 e data de fim 31/01/2020 e
# aplica o filtro.
#
# O sistema exibe uma mensagem informativa indicando que nenhum evento foi
# encontrado para os filtros aplicados. [RN1] [D13]
#
# O ator verifica que nenhum evento e listado.


# [A1] - AJUSTAR O FILTRO APOS A MENSAGEM
# ---------------------------------------------------------------

# O ator altera o periodo para um intervalo que contem eventos
# (ex.: 01/10/2026 a 31/10/2026) e aplica o filtro.
#
# O sistema exibe os eventos correspondentes e a mensagem informativa
# deixa de ser exibida.


# [RN1] - MENSAGEM SEM RESULTADO (CA03)
# ---------------------------------------------------------------

# Quando nenhum evento e encontrado para os filtros aplicados, o sistema
# exibe mensagem informativa.


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Nenhum evento listado e mensagem informativa visivel.
# - Apos filtro com resultados, a mensagem some.
#
# Duvidas relacionadas: D13 (ver DUVIDAS.md)
