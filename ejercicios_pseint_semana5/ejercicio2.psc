Algoritmo sin_titulo
	definir dia, mes, year Como Entero
	definir dia_act, mes_act, year_act Como Entero
	dia_act = 22
	mes_act = 4
	year_act = 2025
	leer dia
	leer mes
	leer year
	definir dias_transc Como Entero
	definir mes_transc Como Entero
	definir year_transc Como Entero
	
	definir suma_dias Como Entero
	year_transc = year_act - year
	mes_transc = mes_act - mes
	dias_transc = dia_act - dia
	si year_transc > 0 Entonces
		suma_dias = 365* year_transc
	FinSi
	si mes_transc > 0 Entonces
		suma_dias = suma_dias + (30 + mes_transc)		
	FinSi
	si dias_transc > 0 Entonces
		suma_dias = suma_dias + dias_transc
	FinSi
	Escribir dias_transc
	Escribir mes_transc
	Escribir year_transc
	Escribir suma_dias
	si suma_dias <= 30 Entonces
		Escribir "Ok"
	FinSi
FinAlgoritmo
