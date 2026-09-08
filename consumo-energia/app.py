aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (ex.: 1000.0): "))
tempo_uso = float(input("Digite o tempo de uso do aparelho em horas (ex.: 2.5): "))

consumo_mensal = (potencia * tempo_uso * 30) / 1000
valor_consumo = consumo_mensal * 0.75

print (f"\nAparelho: {aparelho}")
print (f"Consumo estimado: {consumo_mensal:.2f} kWh/mes.")
print (f"Valor estimado: R$ {valor_consumo:.2f}\n")
