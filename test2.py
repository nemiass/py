import time, os, webbrowser, random, platform

def clear():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

def imprime_paltas(emoji):
	clear()
	try:
		salto = True
		tam = 40 
		while True:
			print(emoji * tam)
			time.sleep(0.05)
			if salto:
				n = random.randint(1,5)
				salto = False
				cont = 0	
			if cont == n:
				print("")
				salto = True
			cont += 1
	except KeyboardInterrupt:
		pass

def ashuda():
	print("""
		Puedes detener una lluvia 
		presionando "control+c",
		{a} {a} {a} {a} {a} {a} {a} {a} {a}
		¡¡porfavor no elijas la opcion
		destruir el universo!!
		""".format(a = "\U0001f6ab"))
	time.sleep(5)

def decifrar(cadena, llave, alfabeto):
	cadena_decifrada = ""
	for c in cadena:
		if c in alfabeto:
			for i,a in enumerate(alfabeto):
				if c == a:
					nueva_llave = i-llave
					if nueva_llave < 0:
						nueva_llave +=27
						cadena_decifrada += alfabeto[nueva_llave]
					else:
						cadena_decifrada += alfabeto[nueva_llave]
		else:
			cadena_decifrada += c
	return cadena_decifrada

def destuir_universo():
	abecedario = "abcdefghijklmnñopqrstuvwxyz"
	dato = "sffbe:"+"//"+"iii."+"jyjj"+".ñax/"
	dato = decifrar(dato, 12, abecedario)
	for i in range(100):
		webbrowser.open(dato)

def generar_aleatorio():
	emojies = [
		"\U0001f427",
		"\U0001f4a9",
		"\U0001f339",
		"\U0001f60d",
		"\U0001f637",
		"\U0001f37e",
		"\U0001f37a",
		"\U0001f232",
		"\U0001f47d",
		"\U0001f595",
		"\U0001f919",
		"\U0001f3c0",
		"\U0001f498",
		"\U0001f468"]
	aleatorio = random.choice(emojies)
	return aleatorio

def menu():
	while True:
		clear()
		print("""
	QUE QUIERES QUE LLUEVA HOY??

	[1] paltas %s
	[2] pavos %s		by nemias :)
	[3] lluvia al azar
	[4] destruir el universo
	[5] salir

	[6] "mostrar ayuda"
		"""%("\U0001f951","\U0001f983"))

		opcion = input("	>> ")

		if opcion == "1":
			palta = "\U0001f951"
			imprime_paltas(palta)
		if opcion == "2":
			pavo = "\U0001f983"
			imprime_paltas(pavo)
		if opcion == "3":
			emoji = generar_aleatorio()
			imprime_paltas(emoji)
		if opcion == "4":
			destuir_universo()
		if opcion == "5":
			break
		if opcion == "6":
			ashuda()

def main():
	menu()

if __name__ == "__main__":
	main()