import requests


url = "https://dummy.restapiexample.com/api/v1/employees"


response = requests.get(url)


if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    data = response.json()

    # Número de empleados
    numero_empleados = len(data["data"])

    # Promedio de salario
    salarios = [empleado["employee_salary"] for empleado in data["data"]]
    promedio_salario = sum(salarios) / numero_empleados

    # Promedio de edad
    edades = [empleado["employee_age"] for empleado in data["data"]]
    promedio_edad = sum(edades) / numero_empleados

    # Salario mínimo y máximo
    salario_minimo = min(salarios)
    salario_maximo = max(salarios)

    # Edad menor y mayor
    edad_menor = min(edades)
    edad_mayor = max(edades)

    # Mostrar resultados
    print("Número de empleados:", numero_empleados)
    print("Promedio de salario:", promedio_salario)
    print("Promedio de edad:", promedio_edad)
    print("Salario mínimo:", salario_minimo)
    print("Salario máximo:", salario_maximo)
    print("Edad menor:", edad_menor)
    print("Edad mayor:", edad_mayor)

else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
