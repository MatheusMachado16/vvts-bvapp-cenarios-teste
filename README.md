# Cenarios de teste - BVapp (VVTS, IFPB)

Documentacao de cenarios de teste dos requisitos funcionais do meu modulo do BVapp.

| Epic | Feature | Cenarios |
|------|---------|----------|
| 23761 - Obtencao dos Valores Gerados nos Inversores | 29677 - Visualizacao e Exportacao Grafica de Geracao por Periodo | UC001 a UC006 |
| 23766 - Acompanhamento de Eventos Gerados nos Inversores | 23884 - Listagem e filtros de eventos | UC007 a UC010 |

- **Autor:** Matheus Yan Machado Santos - machado.matheus@academico.ifpb.edu.br
- **Disciplina:** Verificacao, Validacao e Testes de Software - IFPB, Campus Joao Pessoa
- **Escopo:** apenas documentacao e organizacao dos arquivos. Nao ha implementacao do sistema, interface nem execucao de testes.
- **Base:** backlog do OpenProject e planilha de walkthrough dos requisitos. Os cenarios seguem o texto do OpenProject; os pontos em aberto de cada requisito estao registrados em [DUVIDAS.md](DUVIDAS.md).

## Estrutura

```
bvapp-cenarios/
├── README.md                    # este arquivo
├── DUVIDAS.md                   # regras ausentes/contraditorias para os stakeholders
├── config/                      # reservado para a configuracao Django (etapas futuras)
└── functional_tests/
    ├── __init__.py
    ├── _modelo_cenario.py       # modelo a copiar para cada cenario
    └── test_rf<ID>_ucNNN_<nome>.py   # um cenario por arquivo
```

## Convencao de cada cenario

Cada arquivo traz: identificador e titulo, objetivo, requisitos (feature e CAs), ator, autoria, pre-condicoes e dados, fluxo principal (FP), fluxos alternativos (A), regras de negocio (RN) e resultado esperado (). Referencias `[A1]`, `[RN1]` e `[D01]` ligam os passos aos fluxos, regras e duvidas. Nenhuma das minhas features e CRUD (sao visualizacao, exportacao e consulta), entao a regra das quatro operacoes nao se aplica.

## Indice de cenarios

| ID | Titulo | Requisito (CAs) | Arquivo | Autor |
|----|--------|-----------------|---------|-------|
| UC001 | Visualizar grafico mensal de geracao por ano | RF29677 (CA01, CA02, CA06) | `test_rf29677_uc001_visualizar_grafico_geracao.py` | Matheus Yan Machado Santos |
| UC002 | Filtrar grafico de geracao por usina | RF29677 (CA03) | `test_rf29677_uc002_filtrar_grafico_por_usina.py` | Matheus Yan Machado Santos |
| UC003 | Exibir meses sem dados no grafico de geracao | RF29677 (CA05) | `test_rf29677_uc003_meses_sem_dados_no_grafico.py` | Matheus Yan Machado Santos |
| UC004 | Exibir linha de referencia com a media mensal | RF29677 (CA07) | `test_rf29677_uc004_linha_referencia_media_mensal.py` | Matheus Yan Machado Santos |
| UC005 | Exportar grafico de geracao (JPEG ou PDF) | RF29677 (CA08) | `test_rf29677_uc005_exportar_grafico_geracao.py` | Matheus Yan Machado Santos |
| UC006 | Controlar acesso a tela do grafico por perfil | RF29677 (CA04) | `test_rf29677_uc006_acesso_grafico_geracao_por_perfil.py` | Matheus Yan Machado Santos |
| UC007 | Listar e filtrar eventos dos inversores | RF23884 (CA01) | `test_rf23884_uc007_listar_e_filtrar_eventos.py` | Matheus Yan Machado Santos |
| UC008 | Exibir eventos em ordem cronologica decrescente | RF23884 (CA02) | `test_rf23884_uc008_ordem_cronologica_eventos.py` | Matheus Yan Machado Santos |
| UC009 | Informar ausencia de eventos para os filtros | RF23884 (CA03) | `test_rf23884_uc009_listagem_eventos_sem_resultado.py` | Matheus Yan Machado Santos |
| UC010 | Controlar acesso a listagem de eventos por perfil | RF23884 (CA04) | `test_rf23884_uc010_acesso_listagem_eventos_por_perfil.py` | Matheus Yan Machado Santos |

Cobertura: os 8 CAs da feature 29677 (Visualizacao e Exportacao Grafica de Geracao por Periodo) e os 4 CAs da feature 23884 (Listagem e filtros de eventos).
