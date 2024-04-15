from CLASES import Personas
from CLASES import UNIVERSIDADES
from CLASES import NOTA
from CLASES import ASIGNATURAS


personam = Personas(True,True,True,True)
universidadm = UNIVERSIDADES(True,True,True,True)
notasm = NOTA(True,True,True,True)
asignaturasm = ASIGNATURAS(True,True,True,True)



while(True):
    print("Elija una de las opciones: ")
    print("PERSONAS(1)  \nUNIVERSIDADES(2) \nNOTAS(3)  \nASIGNATURAS(4)  \nFINALIZAR(5) ")
    
    OPCION = int(input("ingrese el numero de alguna de las opciones anteriores: "))
    
    
    if OPCION == 1:
        while(True):
            print("menu persona: ")
            print("CREAR(1)  \nLISTAR(2) \nELIMINAR(3) \nACTUALIZAR(4) \nATRAS(5) ")
        
            sopcion = int(input("elija una de las siguientes opciones: "))
            
            if sopcion == 1:
                personam.crear_p()
            if sopcion == 2:
                personam.listar_p()
            if sopcion == 3:
                personam.eliminar_p()
            if sopcion == 4:
                personam.ACTUALIZAR_p()
            if sopcion == 5:
                break
            
    if OPCION == 2:
            while(True):
             print("menu universidad: ")
             print("CREAR(1)  \nLISTAR(2) \nELIMINAR(3) \nACTUALIZAR(4) \nATRAS(5) ")
        
             uopcion = int(input("elija una de las siguientes opciones: "))
            
             if uopcion == 1:
                universidadm.crear_u()
             if uopcion == 2:
                universidadm.listar_u()
             if uopcion == 3:
                universidadm.eliminar_u()
             if uopcion == 4:
                universidadm.ACTUALIZAR_u()
             if uopcion == 5:
                break
            
    if OPCION == 3:
        while(True):
            print("menu NOTAS: ")
            print("CREAR(1)  \nLISTAR(2) \nELIMINAR(3) \nACTUALIZAR(4) \nATRAS(5) ")
        
            nopcion = int(input("elija una de las siguientes opciones: "))
            
            if nopcion == 1:
                notasm.crear_n()
            if nopcion == 2:
                notasm.listar_n()
            if nopcion == 3:
                notasm.eliminar_n()
            if nopcion == 4:
                notasm.ACTUALIZAR_n()
            if nopcion == 5:
                break
            
    if OPCION == 4:
            while(True):
             print("menu ASIGNATURAS: ")
             print("CREAR(1)  \nLISTAR(2) \nELIMINAR(3) \nACTUALIZAR(4) \nATRAS(5) ")
        
             aopcion = int(input("elija una de las siguientes opciones: "))
            
             if aopcion == 1:
                asignaturasm.crear_a()
             if aopcion == 2:
                asignaturasm.listar_a()
             if aopcion == 3:
                asignaturasm.eliminar_a()
             if aopcion == 4:
                asignaturasm.ACTUALIZAR_a()
             if aopcion == 5:
                break
            
    if OPCION == 5:
        break
          
            
            
                
       
          
           
           
        
           
