
devices = [] #lista
sectors = [] #lista

def show_devices():     #mostrar listas
    if len(devices) > 0:
        print("Dispositivos en la red:")
        for device in devices:
            print(f"{device['ip']} ({device['name']})")
    else:
        print("No se encontraron dispositivos en la red.")

def add_device():     #agregar dispocitivo
    ip = input("Ingrese la dirección IP del nuevo dispositivo: ")
    name = input("Ingrese el nombre del nuevo dispositivo: ")
    vlan = input("Ingrese la VLAN o VLANS configuradas en el dispositivo: ")
    compromised_services = input("Ingrese los servicios de red comprometidos (separados por comas): ")
    sector_name = input("Ingrese el nombre del sector al que pertenece este dispositivo: ")
    sector = None
    for s in sectors:
        if s['name'] == sector_name:
            sector = s
            break
    if not sector:
        print("El sector especificado no existe. Por favor, agregue el sector primero.")
        return
    devices.append({
        'ip': ip,
        'name': name,
        'vlan': vlan,
        'compromised_services': compromised_services.split(","),
        'sector': sector
    })
    print(f"El dispositivo {name} ha sido agregado a la red.")

def add_sector():            #para agregar sectores
    sector_name = input("Ingrese el nombre del nuevo sector: ")
    sector_address = input("Ingrese la dirección del nuevo sector: ")
    sectors.append({
        'name': sector_name,
        'address': sector_address
    })
    print(f"El sector {sector_name} ha sido agregado.")

def show_sectors():    #para mostrar los sectores
    if len(sectors) > 0:
        print("Sectores de la red:")
        for sector in sectors:
            print(f"{sector['name']} ({sector['address']})")
    else:
        print("No se encontraron sectores en la red.")

def show_sector_devices():   #para mostrar dispocitivos del sector
    sector_name = input("Ingrese el nombre del sector para mostrar sus dispositivos: ")
    sector = None
    for s in sectors:
        if s['name'] == sector_name:
            sector = s
            break
    if not sector:
        print("El sector especificado no existe.")
        return
    devices_in_sector = [device for device in devices if device['sector'] == sector]
    if len(devices_in_sector) > 0:
        print(f"Dispositivos en el sector {sector_name}:")
        for device in devices_in_sector:
            print(f"{device['name']} ({device['ip']})")
    else:
        print(f"No se encontraron dispositivos en el sector {sector_name}.")

while True:
    print("\nOpciones:")
    print("1. Agregar dispositivo")
    print("2. Agregar sector")
    print("3. Mostrar dispositivos")
    print("4. Mostrar sectores")
    print("5. Salir")

    option = input("Selecciona una opción: ")

    if option == "1":
        ip = input("Ingresa la dirección IP del dispositivo: ")
        name = input("Ingresa el nombre del dispositivo: ")
        vlan = input("Ingresa la VLAN o VLANs configuradas: ")
        services = input("Ingresa los servicios de red comprometidos: ")
        sector = input("Ingresa el sector al que pertenece: ")
        device = {
            "ip": ip,
            "name": name,
            "vlan": vlan,
            "services": services,
            "sector": sector
        }
        devices.append(device)
        print(f"Dispositivo {name} ({ip}) agregado correctamente.")

    elif option == "2":
        sector_name = input("Ingrese el nombre del nuevo sector: ")
        sector_address = input("Ingrese la dirección del nuevo sector: ")
        sectors.append({
        'name': sector_name,
        'address': sector_address
        })
        print(f"El sector {sector_name} ha sido agregado.")
    
    elif option == "3":
        show_devices()

    elif option == "4":
        show_sectors()

    elif option == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")

#device es una lista con las variables ip, name, vlan, services y sector
#sectors solo tiene la variable de name
#option es una variable para almacenar las opciones del menu
#ip, name,vlan,services, sector son mis variables para almacenar la informacion ingresada por el tecnico
#sector name es mi variable para los nombres de los sectores