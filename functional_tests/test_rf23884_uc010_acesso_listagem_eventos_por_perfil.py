'''
UC010 - Controlar o acesso a listagem de eventos por perfil

Objetivo: Verificar que os perfis Gestor, Tecnico de Manutencao e Operador
de Usina acessam a listagem de eventos e que os demais perfis nao acessam.

Requisitos:
- RF23884 - Listagem e filtros de eventos (Epic 23766)
  - CA04 [24857]

Ator:
- Gestor
- Tecnico de Manutencao
- Operador de Usina
- Usuario de outro perfil (ex.: Tesoureiro)

Autor: Matheus Yan Machado Santos
'''

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Um usuario de cada perfil: Gestor, Tecnico de Manutencao, Operador de
#   Usina e Tesoureiro.


# [FP] - FLUXO PRINCIPAL (perfil Gestor)
# ---------------------------------------------------------------

# O ator, autenticado como Gestor, acessa a pagina de listagem de eventos.
# [RN1]
#
# O sistema exibe a listagem de eventos.


# [A1] - TECNICO DE MANUTENCAO
# ---------------------------------------------------------------

# O ator, autenticado como Tecnico de Manutencao, acessa a pagina de
# listagem de eventos.
#
# O sistema exibe a listagem de eventos. [RN1] [D15]


# [A2] - OPERADOR DE USINA
# ---------------------------------------------------------------

# O ator, autenticado como Operador de Usina, acessa a pagina de listagem
# de eventos.
#
# O sistema exibe a listagem de eventos. [RN1] [D15]


# [A3] - PERFIL SEM PERMISSAO
# ---------------------------------------------------------------

# O ator, autenticado como Tesoureiro, tenta acessar a pagina de listagem
# de eventos.
#
# O sistema nao exibe a listagem ao ator. [RN1]
# Como o bloqueio e apresentado (mensagem, redirecionamento, menu oculto)
# NAO esta definido. [D10]


# [RN1] - PERFIS COM ACESSO (CA04)
# ---------------------------------------------------------------

# Os perfis Gestor, Tecnico de Manutencao e Operador de Usina tem acesso a
# listagem de eventos. O requisito nao cita outros perfis; considera-se que
# eles nao tem acesso, o que deve ser confirmado. [D10]


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Gestor, Tecnico e Operador: listagem exibida.
# - Tesoureiro: listagem nao acessivel.
#
# Duvidas relacionadas: D10, D15 (ver DUVIDAS.md)
