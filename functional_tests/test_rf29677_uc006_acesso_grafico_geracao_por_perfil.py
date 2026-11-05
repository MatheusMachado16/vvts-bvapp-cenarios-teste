'''
UC006 - Controlar o acesso a tela do grafico de geracao por perfil

Objetivo: Verificar que somente o perfil Gestor/Administrador acessa a tela
de visualizacao grafica de geracao.

Requisitos:
- RF29677 - Visualizacao e Exportacao Grafica de Geracao por Periodo (Epic 23761)
  - CA04 [29686]

Ator:
- Gestor
- Usuario de outro perfil (ex.: Operador de Usina, Tecnico de Manutencao, Tesoureiro)

Autor: Matheus Yan Machado Santos
'''

# PRE-CONDICOES E DADOS (exemplos de teste)
# ---------------------------------------------------------------

# - Um usuario Gestor e um usuario Operador de Usina cadastrados.


# [FP] - FLUXO PRINCIPAL (perfil Gestor)
# ---------------------------------------------------------------

# O ator, autenticado como Gestor, acessa a tela de visualizacao grafica de
# geracao por periodo. [RN1] [D09]
#
# O sistema exibe a tela de visualizacao grafica.


# [A1] - USUARIO DE OUTRO PERFIL
# ---------------------------------------------------------------

# O ator, autenticado como Operador de Usina, tenta acessar a tela de
# visualizacao grafica de geracao por periodo.
#
# O sistema nao permite o acesso do ator a tela. [RN1]
# Como o acesso e bloqueado (mensagem, redirecionamento, item de menu
# oculto) NAO esta definido. [D10]
#
# O mesmo roteiro se repete para os perfis Tecnico de Manutencao e Tesoureiro.


# [A2] - PERFIL "ADMINISTRADOR"
# ---------------------------------------------------------------

# O CA04 cita "Gestor/Administrador", enquanto os demais criterios citam so
# "Gestor". Se "Administrador" e um perfil distinto, e necessario um roteiro
# proprio. Pendente. [D09]


# [RN1] - ACESSO RESTRITO (CA04)
# ---------------------------------------------------------------

# Somente o perfil Gestor/Administrador tem acesso a tela de visualizacao
# grafica.


# RESULTADO ESPERADO
# ---------------------------------------------------------------

# - Gestor: tela exibida.
# - Demais perfis: tela nao acessivel.
#
# Duvidas relacionadas: D09, D10 (ver DUVIDAS.md)
