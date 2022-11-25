from time import sleep
import pymysql
import platform
import os
import sys
import getpass

class Data:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sistemtravel'
        )
        self.cursor = self.connection.cursor()
        self.ususario = []
    
    #inicio 
    def inicio(self):
        platform.system() == 'Windows'
        os.system('cls')
        print("sistemtravel\n")
        user = input("usuario: ")
        clave=getpass.getpass("clave: ")
        conta=self.exist_user(user)
        if(conta!=0):
            self.verif_user(user,clave)
        else:
            print("usuario no valido")
            os.system("Pause")
            self.inicio()
    #menu invitado
    def menu_invi(self):
        sys.stdout.flush()
        platform.system() == 'Windows'
        os.system('cls')
        print()
        menu=[
            ['listas'],
            ['1. menu consultas'],
            ['2. menu listas'],
            ['3. Salir']
        ]
        for x in range(4):
            print(menu[x][0])
        opc=int(input("Introduzca opcion: "))
    
        if opc==1:
            self.menu_consult()
        elif opc==2:
            self.menu_listas()
        elif opc==3:
            platform.system() == 'Windows'
            os.system('cls')
            print("Saliendo...")
            self.close()
            os.system('pause')
            exit()
        self.menu_invi()
    #menu admin
    def menu_admin(self):
        platform.system() == 'Windows'
        os.system('cls')
        print()
        menu=[
            ['adiminstrador'],
            ['1. ingresar cliente'],
            ['2. ingresar hotel'],
            ['3. ingresar sucursal'],
            ['4. ingresar vuelo'],
            ['5. ingresar contrato'],
            ['6. modificar cliente'],
            ['7. modificar hotel'],
            ['8. modificar sucursal'],
            ['9. modificar vuelo'],
            ['10. Salir']
        ]
        for x in range(11):
            print(menu[x][0])
        opcion=int(input("Introduzca opcion: "))
        if opcion==1:
            self.insert_client()
        elif opcion==2:
            self.insert_hotel()
        elif opcion==3:
            self.insert_sucur()
        elif opcion==4:
            self.insert_vuel()
        elif opcion==5:
            self.insert_contra()
        elif opcion==6:
            self.updat_client()
        elif opcion==7:
            self.updat_hotel()
        elif opcion==8:
            self.updat_sucursal()
        elif opcion==9:
            self.updat_vuelo()
        elif opcion==10:
            platform.system() == 'Windows'
            os.system('cls')
            print("Saliendo...")
            self.close()
            os.system('pause')
            exit()
        self.menu_admin()
    #menu listas
    def menu_listas(self):
        platform.system() == 'Windows'
        os.system('cls')
        print()
        menu=[
            ['consultas'],
            ['1.listar clientes'],
            ['2.listar sucursales'],
            ['3.listar hoteles'],
            ['4.listar vuelos'],
            ['5.listar contratos'],
            ['6.volver']
        ]
        for x in range(7):
            print(menu[x][0])
        opcion2=int(input("Introduzca opcion: "))
        if opcion2==1:
            self.obtener_clientes()
        elif opcion2==2:
            self.obtener_sucursal()
        elif opcion2==3:
            self.obtener_hoteles()
        elif opcion2==4:
            self.obtener_vuelos()
        elif opcion2==5:
            self.obtener_contrartos()
        elif opcion2==6:
            self.menu_invi()
        self.menu_listas()
    #menu consultas
    def menu_consult(self):
        platform.system() == 'Windows'
        os.system('cls')
        print()
        menu=[
            ['consultas'],
            ['1. consultar sucursal del cliente'],
            ['2. volver'],
            ['3. '],
            ['4. '],
            ['5. ']
        ]
        for x in range(3):
            print(menu[x][0])
        opcion2=int(input("Introduzca opcion: "))
        if opcion2==1:
            self.consl_sucur_clien() 
        elif opcion2==2:
            self.menu_invi()
        self.menu_consult()

    #insertar usuario
    def insert_user(self,nombre,clave):
        sql = "INSERT INTO usuarios (usuario, clave) VALUES ('{0}' ,aes_encrypt('{1}','clave'))".format(nombre,clave)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("usuario creado")
        except Exception as e:
            raise
    #ingreso ususario
    def verif_user(self,usuario,clave):
        sql = "SELECT usuario,CONVERT(aes_decrypt(clave,'clave')USING utf8) AS clave FROM usuarios WHERE usuario = '{}'".format(usuario)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            contrase = user[1]
            if(user[1]==clave):
                if(usuario=="administrador"):
                    self.menu_admin()
                elif(usuario=="usuario1"):
                    self.menu_invi()
            else:
                print("clave incorrecta")
                self.inicio()
        except Exception as e:
            raise
           
    #consultar existencia usuario
    def exist_user(self,usuario):
        sql = "SELECT COUNT(*) FROM usuarios WHERE usuario = '{}'".format(usuario)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        cuentas = (result[0])
        return cuentas
    #validar cliente
    def exist_client(self,cliente):
        sql = "SELECT COUNT(*) FROM clientes WHERE codigo = '{}'".format(cliente)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        dato = (result[0])
        return dato
    #validar hotel
    def exist_hotel(self,hotel):
        sql = "SELECT COUNT(*) FROM hoteles WHERE codigohot = '{}'".format(hotel)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        dato = (result[0])
        return dato
    #validar sucursal
    def exist_suc(self,suc):
        sql = "SELECT COUNT(*) FROM sucursal WHERE codigosu = '{}'".format(suc)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        dato = (result[0])
        return dato
    #validar vuelo
    def exist_vuelo(self,vuelo):
        sql = "SELECT COUNT(*) FROM vuelos WHERE numvue = '{}'".format(vuelo)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        dato = (result[0])
        return dato

    #lista de clientes
    def obtener_clientes(self):
        platform.system() == 'Windows'
        os.system('cls')
        sql = "SELECT * FROM clientes"
        try:
            self.cursor.execute(sql)
            clientes = self.cursor.fetchall()
            for user in clientes:
                print("codigo: ",user[0])
                print("nombre: ",user[1])
                print("apellido: ",user[2])
                print("direccion: ",user[3])
                print("telefono: ",user[4])
                print("___________________\n")
            os.system("pause")
        except:
            print("error")
    
    #lista hoteles
    def obtener_hoteles(self):
        platform.system() == 'Windows'
        os.system('cls')
        sql = "SELECT * FROM hoteles"
        try:
            self.cursor.execute(sql)
            hoteles = self.cursor.fetchall()
            for hot in hoteles:
                print("codigo: ",hot[0])
                print("nombre hotel: ",hot[1])
                print("direccion: ",hot[2])
                print("ciudad: ",hot[3])
                print("telefono: ",hot[4])
                print("plazas disponibles:",hot[5])
                print("________________________\n")
            os.system("pause")
        except:
            print("error")
    #listar sucursal
    def obtener_sucursal(self):
        platform.system() == 'Windows'
        os.system('cls')
        sql = "SELECT * FROM sucursal"
        try:
            self.cursor.execute(sql)
            sucursales = self.cursor.fetchall()
            for suc in sucursales:
                print("codigo: ",suc[0])
                print("direccion: ",suc[1])
                print("telefono: ",suc[2])
                print("_______________________\n")
            os.system("pause")
        except:
            print("error")
    #lista vuelos
    def obtener_vuelos(self):
        platform.system() == 'Windows'
        os.system('cls')
        sql = "SELECT * FROM vuelos"
        try:
            self.cursor.execute(sql)
            vuelos = self.cursor.fetchall()
            for vue in vuelos:
                print("numero de vuelo: ",vue[0])
                print("fecha: ",vue[1])
                print("origen: ",vue[2])
                print("destino: ",vue[3])
                print("plazas totales: ",vue[4])
                print("plazas clase turista: ",vue[5])
                print("_____________________________\n")
            os.system("pause")
        except:
            print("error")
    
    #listar contratos
    def obtener_contrartos(self):
        platform.system() == 'Windows'
        os.system('cls')
        sql = "SELECT * FROM contrato_clien"
        try:
            self.cursor.execute(sql)
            vuelos = self.cursor.fetchall()
            for vue in vuelos:
                print("numero contrato: ",vue[0])
                print("codigo cliente: ",vue[1])
                print("codigo sucursal: ",vue[2])
                print("codigo vuelo: ",vue[3])
                print("clase: ",vue[4])
                print("codigo hotel: ",vue[5])
                print("regimen: ",vue[6])
                print("fecha llegada: ",vue[7])
                print("fecha partida: ",vue[8])
                print("_____________________________\n")
            os.system("pause")
        except:
            print("error")

    #insertar cliente 
    def insert_client(self):
        platform.system() == 'Windows'
        os.system('cls')
        platform.system() == 'Windows'
        os.system('cls')
        codigo = int(input("codigo: "))
        nombre = input("nombre: ")
        apellido = input("apellido: ")
        direccion = input("direccion: ")
        telefono = input("telefono: ")
        sql = "INSERT INTO clientes (codigo,nombre,apellido,direccion,telefono) VALUES ({0},'{1}','{2}','{3}','{4}')".format(codigo,nombre,apellido,direccion,telefono)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("cliente creado")
            os.system('pause')
        except:
            print("error")
            os.system('pause')
    #insertar sucursal
    def insert_sucur(self):
        platform.system() == 'Windows'
        os.system('cls')
        codigo = int(input("codigo: "))
        direccion = input("direccion: ")
        telefono = input("telefono: ")
        sql = "INSERT INTO sucursal (codigosu,direccion,telefono) VALUES ({0},'{1}','{2}')".format(codigo,direccion,telefono)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("sucursal creada")
            os.system('pause')
        except:
            print("error")
            os.system('pause')
    #insertar hotel
    def insert_hotel(self):
        platform.system() == 'Windows'
        os.system('cls')
        codigo = int(input("codigo: "))
        nombre = input("nombre hotel: ")
        direccion = input("direccion: ")
        ciudad = input("ciudad: ")
        telefono = input("telefono: ")
        numero_plazaa = int(input("plazas disponibles: "))
        sql = "INSERT INTO hoteles (codigohot,nombre,direccion,ciudad,telefono,numplazadis) VALUES ({0},'{1}','{2}','{3}','{4}',{5})".format(codigo,nombre,direccion,ciudad,telefono,numero_plazaa)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("hotel creado")
            os.system('pause')
        except:
            print("error")
            os.system('pause')
    #insertar vuelo
    def insert_vuel(self):
        platform.system() == 'Windows'
        os.system('cls')
        codigo = int(input("numero de vuelo: "))
        fecha = input("fecha (yyyy-mm-dd):")
        hora = input("hora (hh:mm:ss):")
        origen = input("origen: ")
        destino = input("destino: ")
        plazas_to = input("plazas totales: ")
        plazas_tu = input("plazas clase turista: ")
        sql = "INSERT INTO vuelos (numvue,fecha,hora,origen,destino,plazastotales,plazasturis) VALUES ({0},'{1}','{2}','{3}','{4}',{5},{6})".format(codigo,fecha,hora,origen,destino,plazas_to,plazas_tu)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("vuelo creado")
            os.system("pause")
        except:
            print("error")
            os.system('pause')
    #insertar contrarto
    def insert_contra(self):
        platform.system() == 'Windows'
        os.system('cls')
        resul = 0
        while resul<1:
            cliente = int(input("codigo cliente: "))
            resul=self.exist_client(cliente)
            if(resul!=1):
                print("cliente invalido")
        resul = 0
        while resul<1:
            sucursal = int(input("codigo sucursal: "))
            resul=self.exist_suc(sucursal)
            if(resul!=1):
                print("sucursal invalida")
        resul = 0
        while resul<1:
            vuelo = int(input("codigo vuelo: "))
            resul=self.exist_vuelo(vuelo)
            if(resul!=1):
                print("vuelo invalido")
        clase = input("clase (turista o primera): ")
        resul = 0
        while resul<1:
            hotel = int(input("codigo hotel: "))
            resul=self.exist_hotel(hotel)
            if(resul!=1):
                print("hotel invalido")
        regimen = input("regimen (media pensión o pensión completa): ")
        fecha_LL= input("fecha llegada (yyyy-mm-dd):")
        fecha_PAR= input("fecha llegada (yyyy-mm-dd):")
        sql = "INSERT INTO contrato_clien (codclien,codsucursal,codvuelo,clase,codhotel,regimen,fechallegada,fechapartida) VALUES ({0},{1},{2},'{3}',{4},'{5}','{6}','{7}')".format(cliente,sucursal,vuelo,clase,hotel,regimen,fecha_LL,fecha_PAR)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("contrato creado ")
            os.system("pause")
        except:
            print("error")
            os.system('pause')
    #conslutar sucursales contratadas
    def consl_sucur_clien(self):
        platform.system() == 'Windows'
        os.system('cls')
        cliente = int(input("ingrese codigo de cliente:"))
        sql="SELECT * FROM sucursal WHERE codigosu = (SELECT CODSUCURSAL FROM contrato_clien WHERE CODCLIEN = {})".format(cliente)
        try:
            self.cursor.execute(sql)
            clientes = self.cursor.fetchall()
            for user in clientes:
                print("codigo: ",user[0])
                print("direccion: ",user[1])
                print("telefono: ",user[2])
                print("___________________\n")
            os.system("Pause")
        except:
            print("error")

    #modificar cliente
    def updat_client(self):
        platform.system() == 'Windows'
        os.system('cls')
        resul = 0
        while resul<1:
            cliente = int(input("codigo cliente: "))
            resul=self.exist_client(cliente)
            if(resul!=1):
                print("cliente no valido")
        sql = "SELECT * FROM clientes WHERE codigo = {}".format(cliente)
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        opcion=1
        while(opcion>0 and opcion<7):
            print("1.codigo: ",user[0])
            print("2.nombre: ",user[1])
            print("3.apellido: ",user[2])
            print("4.direccion: ",user[3])
            print("5.telefono: ",user[4])
            print("6.cancelar")
            opcion = int(input("que desea midificar: "))
            if opcion == 1:
                newcod=int(input("ingrese el nuevo codigo: "))
                self.update_clien_contra(cliente,newcod)
                sql= "UPDATE clientes SET codigo='{0}' WHERE codigo = {1}".format(newcod,cliente)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 2:
                newnom=input("ingrese el nuevo nombre: ")
                sql= "UPDATE clientes SET nombre='{0}' WHERE codigo = {1}".format(newnom,cliente)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 3:
                newapell=("ingrese el nuevo apellido: ")
                sql= "UPDATE clientes SET apellido='{0}' WHERE codigo = {1}".format(newapell,cliente)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 4:
                newdirecc=("ingrese la nuevo direccion: ")
                sql= "UPDATE clientes SET direccion='{0}' WHERE codigo = {1}".format(newdirecc,cliente)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 5:
                newtel=("ingrese el nuevo telefono: ")
                sql= "UPDATE clientes SET telefono='{0}' WHERE codigo = {1}".format(newtel,cliente)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 6:
                print("saliendo...")
                os.system('pause')
                break
    
    #modificar cliente contrato
    def update_clien_contra(self,codigo,newcod):
        sql = "UPDATE contrato_clien SET codclien='{0}' WHERE codclien = {1}".format(newcod,codigo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            #print("dato actualizado")
            #os.system('pause')
        except:
            print("error")
    #modificar suscursal
    def updat_sucursal(self):
        platform.system() == 'Windows'
        os.system('cls')
        resul = 0
        while resul<1:
            sucursal = int(input("codigo sucursal: "))
            resul=self.exist_suc(sucursal)
            if(resul!=1):
                print("sucursal no valida")
        sql = "SELECT * FROM sucursal WHERE codigosu = {}".format(sucursal)
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        opcion=1
        while(opcion>0 and opcion<5):
            print("1.codigo: ",user[0])
            print("2.direccion: ",user[1])
            print("3.telefono: ",user[2])
            print("4.cancelar")
            opcion = int(input("que desea midificar: "))
            if opcion == 1:
                newcod=int(input("ingrese el nuevo codigo: "))
                self.update_sucur_contra(sucursal,newcod)
                sql= "UPDATE sucursal SET codigosu='{0}' WHERE codigosu = {1}".format(newcod,sucursal)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 2:
                newdir=("ingrese la nueva direccion: ")
                sql= "UPDATE sucursal SET direccion='{0}' WHERE codigosu = {1}".format(newdir,sucursal)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 3:
                newtel=("ingrese el nuevo telefono: ")
                sql= "UPDATE sucursal SET telefono='{0}' WHERE codigosu = {1}".format(newtel,sucursal)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 4:
                print("saliendo...")
                os.system('pause')
                break
    #modificar sucursal contrato
    def update_sucur_contra(self,codigo,newcod):
        sql = "UPDATE contrato_clien SET codsucursal='{0}' WHERE codsucursal = {1}".format(newcod,codigo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            #print("dato actualizado")
            #os.system('pause')
        except:
            print("error")
    
    #modificar hotel
    def updat_hotel(self):
        platform.system() == 'Windows'
        os.system('cls')
        resul = 0
        while resul<1:
            hotel = int(input("codigo hotel: "))
            resul=self.exist_hotel(hotel)
            if(resul!=1):
                print("hotel no valido")
        sql = "SELECT * FROM hoteles WHERE codigohot = {}".format(hotel)
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        opcion=1
        while(opcion>0 and opcion<8):
            print("1.codigo: ",user[0])
            print("2.nombre: ",user[1])
            print("3.direccion: ",user[2])
            print("4.ciudad: ",user[3])
            print("5.telefono: ",user[4])
            print("6.numero de plazas: ",user[5])
            print("7.cancelar")
            opcion = int(input("que desea midificar: "))
            if opcion == 1:
                newcod=int(input("ingrese el nuevo codigo: "))
                self.update_hotel_contra(hotel,newcod)
                sql= "UPDATE hoteles SET codigohot='{0}' WHERE codigohot = {1}".format(newcod,hotel)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 2:
                newnom=("ingrese el nuevo nombre: ")
                sql= "UPDATE hoteles SET nombre='{0}' WHERE codigohot = {1}".format(newnom,hotel)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 3:
                newdir=("ingrese la nueva direccion: ")
                sql= "UPDATE hoteles SET direccion='{0}' WHERE codigohot = {1}".format(newdir,hotel)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 4:
                newciu=("ingrese la nueva ciudad: ")
                sql= "UPDATE hoteles SET ciudad='{0}' WHERE codigohot = {1}".format(newciu,hotel)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 5:
                newtel=("ingrese el nuevo telefono: ")
                sql= "UPDATE hoteles SET telefono='{0}' WHERE codigohot = {1}".format(newtel,hotel)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 6:
                newplaz=("ingrese el nuevo numero de plazas: ")
                sql= "UPDATE hoteles SET numplazadis='{0}' WHERE codigohot = {1}".format(newplaz,hotel)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 7:
                print("saliendo...")
                os.system('pause')
                break
    #modificar hotel contrarto
    def update_hotel_contra(self,codigo,newcod):
        sql = "UPDATE contrato_clien SET codhotel='{0}' WHERE codhotel = {1}".format(newcod,codigo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            #print("dato actualizado")
            #os.system('pause')
        except:
            print("error")
    
    #modificar vuelos
    def updat_vuelo(self):
        platform.system() == 'Windows'
        os.system('cls')
        resul = 0
        while resul<1:
            vuelo = int(input("codigo vuelo: "))
            resul=self.exist_vuelo(vuelo)
            if(resul!=1):
                print("hotel no valido")
        sql = "SELECT * FROM vuelos WHERE numvue = {}".format(vuelo)
        self.cursor.execute(sql)
        user = self.cursor.fetchone()
        opcion=1
        while(opcion>0 and opcion<9):
            print("1.codigo: ",user[0])
            print("2.fecha: ",user[1])
            print("3.horan: ",user[2])
            print("4.origen: ",user[3])
            print("5.destino: ",user[4])
            print("6.numero de plazas: ",user[5])
            print("7.numero de plazas clase turista: ",user[5])
            print("8.cancelar")
            opcion = int(input("que desea midificar: "))
            if opcion == 1:
                newcod=int(input("ingrese el nuevo codigo: "))
                self.update_vuelo_contra(vuelo,newcod)
                sql= "UPDATE vuelos SET numvue='{0}' WHERE numvue = {1}".format(newcod,vuelo)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 2:
                newdate=input("ingrese la nueva fecha(yyyy-mm-dd): ")
                sql= "UPDATE vuelos SET fecha='{0}' WHERE numvue = {1}".format(newdate,vuelo)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 3:
                newtime=input("ingrese la nueva hora(hh:mm:ss): ")
                sql= "UPDATE vuelos SET hora='{0}' WHERE numvue = {1}".format(newtime,vuelo)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 4:
                newori=input("ingrese el nuevo origen: ")
                sql= "UPDATE vuelos SET origen='{0}' WHERE numvue = {1}".format(newori,vuelo)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 5:
                newdes=input("ingrese el nuevo destino: ")
                sql= "UPDATE vuelos SET destino='{0}' WHERE numvue = {1}".format(newdes,vuelo)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 6:
                newpla=int(input("ingrese el nuevo numero de plazas: "))
                sql= "UPDATE vuelos SET plazastotales='{0}' WHERE numvue = {1}".format(newpla,vuelo)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 7:
                newplatu=int(input("ingrese el nuevo numero de plazas clase turista: "))
                sql= "UPDATE vuelos SET plazasturis='{0}' WHERE numvue = {1}".format(newplatu,vuelo)
                try:
                    self.cursor.execute(sql)
                    self.connection.commit()
                    print("dato actualizado")
                    os.system('pause')
                    break
                except:
                    print("error")
                    break
            elif opcion == 8:
                print("saliendo...")
                os.system('pause')
                break
    #modificar vuelos contrato
    def update_vuelo_contra(self,codigo,newcod):
        sql = "UPDATE contrato_clien SET codvuelo='{0}' WHERE codvuelo = {1}".format(newcod,codigo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            #print("dato actualizado")
            #os.system('pause')
        except:
            print("error")
    #cerrar conexion
    def close(self):
        self.connection.close()
        print("conexion cerrada")
data = Data()
data.inicio()



