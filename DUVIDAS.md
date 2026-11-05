# Duvidas para esclarecimento com os stakeholders

Regras ausentes ou contraditorias encontradas nos requisitos (backlog do OpenProject exportado em 30/10/2026). Nenhuma regra foi inventada nos cenarios: cada ponto abaixo aguarda esclarecimento.

**Origem:** `walkthrough` = problema ja registrado na planilha de walkthrough da equipe (aba "Problemas e revisoes"). `adicional` = observacao feita ao escrever os cenarios, ainda nao registrada no walkthrough.

| ID | Cenario | Requisito (CA) | Duvida | Sugestao de revisao | Origem | Status |
|----|---------|----------------|--------|---------------------|--------|--------|
| D01 | UC002 | RF29677 CA03 [29681] | O criterio diz que o filtro "(periodo)" e obrigatorio, mas trata de usina; o periodo ja e escolhido pelo seletor de ano (CA02). O obrigatorio e a usina? | "... quando possui acesso a mais de uma usina, a selecao da usina e obrigatoria antes de exibir o grafico." | walkthrough | Aberta |
| D02 | UC001, UC002 | RF29677 CA03 [29681] | O que acontece quando o Gestor tem acesso a uma unica usina? O grafico e exibido direto? | Explicitar o comportamento com uma so usina. | adicional | Aberta |
| D03 | UC001, UC003 | RF29677 CA02 [29680] | Qual ano aparece ao abrir a tela e quais anos o seletor oferece (a partir do primeiro dado coletado?) | Definir ano inicial (ex.: corrente) e anos disponiveis. | walkthrough | Aberta |
| D04 | UC003 | RF29677 CA05 [29682] | Qual e a indicacao visual dos meses sem dados? O criterio so da exemplos ("cor ou hachura"), e "diferenciada" nao e verificavel. | Definir a indicacao (ex.: cor X e legenda "Sem dados"). | walkthrough | Aberta |
| D05 | UC004 | RF29677 CA07 [29684] | "Linha de referencia ou indicador visual": qual dos dois? "Esperado" e a media mensal? Como a media e calculada? "Rapidamente" e subjetivo. | "O grafico exibe uma linha de referencia com a media mensal de geracao do ano selecionado; meses com barra abaixo da linha estao abaixo da media." | walkthrough | Aberta |
| D06 | UC004 | RF29677 CA07 [29684] | Meses sem dados contam como zero na media ou ficam fora dela? | Definir o tratamento de meses sem dados. | walkthrough | Aberta |
| D07 | UC005 | RF29677 CA08 [29685] | O que ocorre se a exportacao falhar? A exportacao de medicoes preve mensagem de erro (25105); este criterio nao. | Acrescentar "Caso a exportacao falhe, o sistema exibe mensagem de erro.", alinhado a 25105. | walkthrough | Aberta |
| D08 | UC005 | RF29677 CA08 [29685] | O que o arquivo exportado contem alem do grafico (titulo, ano, usina, legenda) e qual o nome do arquivo? | Definir o conteudo minimo do arquivo exportado. | adicional | Aberta |
| D09 | UC006 | RF29677 CA04 [29686] | "Administrador" e um perfil distinto de "Gestor"? O criterio usa "Gestor/Administrador"; os demais usam "Gestor". A numeracao (CA04 depois de CA08) esta fora de ordem. | Padronizar o nome do perfil em todos os criterios e reordenar a numeracao. | walkthrough | Aberta |
| D10 | UC006, UC010 | RF29677 CA04 [29686]; RF23884 CA04 [24857] | Como o acesso e negado aos perfis sem permissao (mensagem, redirecionamento, item de menu oculto)? Perfis nao citados nos criterios (ex.: Tesoureiro) nao tem acesso? | Definir o comportamento de bloqueio e declarar que os perfis nao listados nao tem acesso. | adicional | Aberta |
| D11 | UC007 | RF23884 CA01 [24852] | Quais sao os niveis de severidade? O atributo nao existe no registro do evento (24842). | Definir os niveis e incluir a severidade em 24842. | walkthrough | Aberta |
| D12 | UC008 | RF23884 CA02 [24853] | "Ordem cronologica" usa o timestamp de ocorrencia ou o de registro? "Por padrao" indica que ha outra ordenacao disponivel? | Especificar que a ordenacao usa o timestamp de ocorrencia (se for o caso). | walkthrough | Aberta |
| D13 | UC009 | RF23884 CA03 [24855] | Qual e o texto da "mensagem informativa" quando nao ha eventos? | "... o sistema exibe a mensagem '[texto definido]'." (mesmo padrao de 24996 e 24917). | walkthrough | Aberta |
| D14 | UC007 | RF23884 CA01 [24852] | Os filtros sao opcionais? Sem filtros, a listagem mostra todos os eventos? Qual o comportamento com data de inicio maior que a de fim ou com so uma das datas preenchida? | Definir obrigatoriedade, valor padrao e validacao das datas. | adicional | Aberta |
| D15 | UC010 | RF23884 CA04 [24857] | Tecnico de Manutencao e Operador de Usina veem eventos de todas as usinas ou so das usinas as quais tem acesso? | Declarar o escopo de usinas de cada perfil. | adicional | Aberta |
