import re
from datetime import date

# 1. Validador de correo electrónico
class EmailInvalidoError(Exception):
    """Excepción lanzada cuando el formato del correo no es correcto."""
    pass
def validar_email(email):
    # lo necesario para un correo
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, email):
        raise EmailInvalidoError(f"El correo '{email}' no tiene un formato válido.") 
    return True
emails_a_probar = ["hola@mundo.com", "usuario_juanitoat-gmail.com", "tres_tristes_tigres@dominio", ""]

for correo in emails_a_probar:
    try:
        validar_email(correo)
        print(f"correo verificado {correo}: ¡Es válido!")
    except EmailInvalidoError as e:
        print(f"correo invalido {correo}: Error -> {e}")

# 2. Inventario de zapatos

inventario = {
    ("deportivo", "negro", 42): 5,
    ("formal",    "café",  40): 2,
    ("casual",    "blanco",38): 0,
}

def verificar_zapato(tipo, color, talla):
    try:
        cantidad = inventario.get((tipo, color, talla))
        if cantidad is None:
            raise KeyError("Combinación no existe en inventario.")
        if cantidad == 0:
            raise ValueError("Producto agotado.")
        print(f"producto Disponible ({cantidad} pares): {tipo}, {color} ,talla {talla}")
    except (KeyError, ValueError) as e:
        print(f"incorrecyo {e}")

verificar_zapato("deportivo", "negro", 42)
verificar_zapato("casual",    "blanco",38)
verificar_zapato("formal",    "rojo",  41)



# 3. Calculadora de edad

def calcular_edad(fecha):
    try:
        nacimiento = date.fromisoformat(fecha)   # "YYYY-MM-DD"
        if nacimiento > date.today():
            raise ValueError("La fecha no puede ser futura.")
        hoy = date.today()
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        print(f" Edad: {edad} años")
    except ValueError as e:
        print(f" Fecha inválida: {e}")

calcular_edad("1995-06-15")
calcular_edad("2030-01-01")

# 4. Cálculo de nómina (15 días + auxilio de transporte)
SMMLV= 1300000   
AUXILIO_TRANSP=   162000   

def calcular_nomina(sueldo_mensual):
    try:
        if sueldo_mensual <= 0:
            raise ValueError("El sueldo debe ser mayor a 0.")
        pago_15 = sueldo_mensual / 2
        auxilio = (AUXILIO_TRANSP / 2) if sueldo_mensual <= 2 * SMMLV else 0
        total   = pago_15 + auxilio
        print(f" Sueldo mensual  : ${sueldo_mensual:,.0f}")
        print(f"   Pago 15 días    : ${pago_15:,.0f}")
        print(f"   Auxilio transp. : ${auxilio:,.0f}")
        print(f"   TOTAL a pagar   : ${total:,.0f}")
    except ValueError as e:
        print(f"invalido {e}")

calcular_nomina(1300000)
calcular_nomina(-500)



# 5. Guardar diez palabras en un archivo .txt
palabras = ["python", "excepción", "archivo", "código", "función",
            "lista",  "diccionario","bucle",  "clase",  "módulo"]

def guardar_palabras(nombre_archivo, lista):
    try:
        if len(lista) != 10:
            raise ValueError(f"Se requieren exactamente 10 palabras, se dieron {len(lista)}.")
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write("\n".join(lista))
        print(f"✅ Palabras guardadas en '{nombre_archivo}'")
    except (ValueError, OSError) as e:
        print(f"❌ Error: {e}")

guardar_palabras("palabras.txt", palabras)
guardar_palabras("palabras.txt", palabras[:5])   




