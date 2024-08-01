nombre = "Belen"
apellido = "Sanchez"
edad = 18
peso = 44.2

print(type(nombre))
print(type(edad))
print(type(peso))

# intentar el parsing
edad_en_string = str(edad)
print(f"""La edad anterior era {type(edad)},
      la edad parseada es de tipo 
      {type(edad_en_string)}""")