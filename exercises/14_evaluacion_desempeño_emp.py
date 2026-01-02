"""Una empresa evalúa su trimestre con base en:

Ingresos totales
Gastos totales
Número de nuevos clientes

Clasificación:

Si ingresos - gastos > $10,000 y más de 50 nuevos clientes → "Trimestre Excelente"
Si ingresos - gastos > $5,000 y al menos 20 clientes → "Trimestre Bueno"
Si ingresos - gastos > 0 → "Trimestre Regular"
Si ingresos - gastos ≤ 0 → "Trimestre Deficitario"""

Ingresos_totales = (int(input('Digite los ingresos totales: ')))
Gastos_totales = (int(input('Digite los gastos totales: ')))
Numero_clientes = (int(input('Digite el número de nuevos clientes: ')))

if Ingresos_totales and Gastos_totales > 10000 and Numero_clientes > 50: 
        print("Trimestre excelente")
elif Ingresos_totales and Gastos_totales > 10000 and Numero_clientes >= 20: 
        print ("Trimestre bueno")
elif  Ingresos_totales and Gastos_totales > 0:
        print("Trimestre regular")
else: 
    Ingresos_totales and Gastos_totales < -0
    print('Trimestre deficitario')