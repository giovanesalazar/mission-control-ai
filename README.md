# Global Solution 1 - Pensamento Computacional e Automação com Python

## 🚀 Mission Control AI

## 📖 Descrição

O Mission Control AI é um sistema de monitoramento capaz de analisar dados simulados de uma missão espacial, identificar situações de risco, classificar o estado operacional dos sistemas, gerar recomendações automáticas e a produção de relatórios da missão assim auxiliando na tomada de decisão.

O projeto foi desenvolvido utilizando conceitos de matrizes, listas, dicionários, funções, estruturas condicionais e análise de dados.

---

## 🎯 Objetivo

Simular um centro de controle espacial capaz de:

Monitorar parâmetros críticos da missão
Detectar falhas e anomalias operacionais
Classificar níveis de risco
Gerar recomendações automáticas
Produzir relatórios consolidados da missão

---

## 📊 Parâmetros Monitorados

O sistema acompanha cinco áreas principais:

Parâmetros:	                         

* Temperatura Interna (Temperatura dentro da nave)        
* Comunicação com a Base (Qualidade do sinal de comunicação)	     
* Sistema de Energia (Nível de bateria disponível)
* Suporte de Oxigênio (Disponibilidade de oxigênio)
* Estabilidade Operacional (Funcionamento geral dos sistemas)	   

---

## ⚙️ Funcionamento

Os dados da missão são armazenados em uma matriz, onde cada linha representa um ciclo de monitoramento.

Exemplo:

[22, 95, 90, 98, 92]

Representando:

Temperatura: 22°C
Comunicação: 95%
Energia: 90%
Oxigênio: 98%
Estabilidade: 92%

Para cada ciclo, o sistema:

Analisa todos os parâmetros.
Classifica cada valor como:
NORMAL
ATENÇÃO
CRÍTICO
Calcula uma pontuação de risco.
Determina o status geral do ciclo.
Gera recomendações automáticas.

---

## 🧠 Lógica de Classificação

Cada parâmetro recebe uma pontuação:

Status	Pontos
NORMAL	0
ATENÇÃO	1
CRÍTICO	2

A soma dos pontos determina a situação do ciclo:

Pontuação Total	Classificação
0 a 2	MISSÃO ESTÁVEL
3 a 5	MISSÃO EM ATENÇÃO
Acima de 5	MISSÃO CRÍTICA


## 🔍 Análises Realizadas

Além da classificação individual dos ciclos, o sistema realiza:

Cálculo das médias dos parâmetros;
Identificação do ciclo mais crítico;
Cálculo do risco médio da missão;
Contagem de ciclos críticos;
Análise de tendência da missão;
Identificação da área mais afetada;
Geração automática de recomendações;
Emissão de relatório final consolidado.

---

## 📈 Exemplo de Recomendações

Dependendo dos problemas detectados, o sistema pode sugerir ações como:

Verificar controle térmico da missão;
Restabelecer comunicação com a base;
Ativar modo de economia de energia;
Executar protocolos de suporte à vida;
Reduzir operações não essenciais.

---

## 📋 Relatório Final

Ao final da execução, o sistema apresenta:

Estatísticas gerais da missão
Médias operacionais
Ciclo de maior risco
Tendência da missão
Área mais afetada
Classificação final
Conclusão operacional
