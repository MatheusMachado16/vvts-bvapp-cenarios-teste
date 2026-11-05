'''
UC008 - Exibir eventos em ordem cronologica decrescente

Objetivo: Verificar que, por padrao, a listagem de eventos mostra os mais
recentes primeiro.

Requisitos:
- RF23884 - Listagem e filtros de eventos (Epic 23766)
  - CA02 [24853]

Ator:
- Gestor

Autor: Matheus Yan Machado Santos
'''

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Pelo menos tres eventos com timestamps distintos, cadastrados fora de
#   ordem (ex.: 12/10/2026 08:00, 03/10/2026 14:30, 20/10/2026 09:15).


# [FP] - FLUXO PRINCIPAL
# ---------------------------------------------------------------

# O ator acessa a pagina de listagem de eventos, sem alterar nenhuma opcao
# de ordenacao.
#
# O sistema exibe os eventos em ordem cronologica decrescente. [RN1] [D12]
#
# O ator verifica que o primeiro evento e o mais recente
# (20/10/2026 09:15) e que cada evento seguinte e mais antigo que o anterior
# (12/10/2026 08:00, depois 03/10/2026 14:30).


# [A1] - ORDEM APOS APLICAR FILTRO
# ---------------------------------------------------------------

# O ator aplica um filtro (ex.: periodo 01/10/2026 a 31/10/2026).
#
# O sistema exibe os eventos filtrados.
#
# O ator verifica que a ordem decrescente se mantem nos resultados filtrados.


# [RN1] - ORDEM PADRAO (CA02)
# ---------------------------------------------------------------

# Os resultados sao apresentados em ordem cronologica decrescente por padrao.
# Qual timestamp define a ordem (ocorrencia ou registro) e se existe outra
# ordenacao possivel ("por padrao"): ver D12.


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Eventos do mais recente para o mais antigo.
#
# Duvidas relacionadas: D12 (ver DUVIDAS.md)
