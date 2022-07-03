import pandas as pd
import requests

tabela = pd.read_csv("vinhos.csv")

#@title Seleção de Vinhos {run:'auto'}
Opcao = "Ano da colheita" #@param ["", "Rotulo", "Ano da colheita", "Tipo"] {allow-input: true}

if Opcao == "Rotulo" :
  tabela_ordem = tabela.sort_values('rotulo')
  print("A opção escolhida foi rótulo.\n",tabela_ordem)
  
elif Opcao == "Ano da colheita" :
  tabela_ordem = tabela.sort_values('ano_colheita')
  print("A opção escolhida foi ano da colheita.\n",tabela_ordem)

elif Opcao == "Tipo" :
  tabela_ordem = tabela.sort_values('tipo')
  print("A opção escolhida foi tipo.\n\n",tabela_ordem)

else :
  print("\nVocê não escolheu nenhuma opção válida.")

tabela_ordem.to_csv('Vinhos.csv')