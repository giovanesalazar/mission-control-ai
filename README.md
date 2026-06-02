# Global Solution 1 - Pensamento Computacional e Automação com Python

## 🚀 Mission Control AI

## 📖 Descrição

O Mission Control AI é um sistema de monitoramento capaz de analisar dados simulados de uma missão espacial, identificar situações de risco, classificar o estado operacional dos sistemas, gerar recomendações automáticas e a produção de relatórios da missão assim auxiliando na tomada de decisão.

O projeto foi desenvolvido utilizando conceitos de matrizes, listas, dicionários, funções, estruturas condicionais e análise de dados.

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

Exemplo: [22, 95, 90, 98, 92]

Representando:

* Temperatura: 22°C
* Comunicação: 95%
* Energia: 90%
* Oxigênio: 98%
* Estabilidade: 92%

Para cada ciclo, o sistema analisa todos os parâmetros, classifica cada valor como: NORMAL / ATENÇÃO / CRÍTICO, calcula uma pontuação de risco, determina o status geral do ciclo e gera recomendações automáticas.

As funções presentes no código são:
* analisar_temperatura
* analisar_comunicacao
* analisar_bateria
* analisar_oxigenio
* analisar_estabilidade
* classificar_ciclo
* gerar_recomendacao_para_ciclo
* analisar_tendencia
* identificar_area_mais_afetada
* gerar_relatorio_final

---

## 🧠 Lógica de Classificação

Cada parâmetro recebe uma pontuação, o NORMAL recebe 0 pontos, o ATENÇÃO recebe 1 ponto e o CRÍTICO recebe 2 pontos. 

A soma dos pontos determina a situação do ciclo:


* 0 a 2: MISSÃO ESTÁVEL
* 3 a 5: MISSÃO EM ATENÇÃO
* Acima de 5: MISSÃO CRÍTICA

---

## 🔍 Análises Realizadas

Além da classificação individual dos ciclos, o sistema realiza:

* Cálculo das médias dos parâmetros
* Identificação do ciclo mais crítico
* Cálculo do risco médio da missão
* Contagem de ciclos críticos
* Análise de tendência da missão
* Identificação da área mais afetada
* Geração automática de recomendações
* Emissão de relatório final consolidado

---

## 📈 Exemplo de Recomendações

Dependendo dos problemas detectados, o sistema pode sugerir ações como:

* Verificar controle térmico da missão
* Restabelecer comunicação com a base
* Ativar modo de economia de energia
* Executar protocolos de suporte à vida
* Reduzir operações não essenciais

---

## 📋 Relatório Final

Ao final da execução, o sistema apresenta:

* Estatísticas gerais da missão
* Médias dos parâmetros
* Ciclo mais crítico
* Tendência da missão
* Área mais afetada
* Classificação final
* Conclusão operacional

---

## 🎬 Demonstração

Vídeo de demonstração prática do sistema: 
