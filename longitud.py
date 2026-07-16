def es_palindromo(texto):
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter != " ":
            limpio += caracter
    
    # Retornamos ambos valores: el booleano y la cadena limpia
    return limpio == limpio[::-1], limpio

# El resto de tu código queda igual
entrada = input("Ingrese una frase: ")
resultado, cadena_limpia = es_palindromo(entrada)

if resultado:
    print("Es un palíndromo")
else:
    print("No es palíndromo")
print("Longitud de la cadena limpia:", len(cadena_limpia))