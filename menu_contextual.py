import os
import sys
import ctypes
import winreg

def es_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def activar_menu_clasico():
    try:
        clave_path = r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32"
        clave = winreg.CreateKey(winreg.HKEY_CURRENT_USER, clave_path)
        winreg.SetValueEx(clave, None, 0, winreg.REG_SZ, "")
        winreg.CloseKey(clave)
        print("✅ Menú contextual clásico activado. Es posible que debas reiniciar el Explorador de Windows para ver los cambios.")
    except Exception as e:
        print(f"Error activando menú clásico: {e}")

def restaurar_menu_moderno():
    try:
        clave_path = r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}"
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, clave_path + r"\InprocServer32")
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, clave_path)
        print("✅ Menú contextual moderno restaurado.")
    except FileNotFoundError:
        print("El menú contextual ya estaba en modo moderno.")
    except Exception as e:
        print(f"Error restaurando menú moderno: {e}")

def reiniciar_explorador():
    print("Reiniciando el Explorador de Windows...")
    os.system("taskkill /f /im explorer.exe")
    os.system("start explorer.exe")

def main():
    if not es_admin():
        print("Este script requiere permisos de administrador.")
        # Re-ejecutar como admin
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

    print("¿Qué quieres hacer?\n")
    print("1) Activar menú contextual clásico (Windows 10)")
    print("2) Dejar menú contextual moderno (Windows 11 de serie)")
    print("3) No hacer nada y salir")

    opcion = input("\nIntroduce tu opción (1/2/3): ")

    if opcion == "1":
        activar_menu_clasico()
        reiniciar_explorador()
    elif opcion == "2":
        restaurar_menu_moderno()
        reiniciar_explorador()
    elif opcion == "3":
        print("No se realizó ningún cambio.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
