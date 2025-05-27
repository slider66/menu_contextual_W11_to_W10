# Cambia el Menú Contextual Clásico en Windows 11 / Change to Classic Context Menu in Windows 11

[Versión en español abajo / Spanish version below]

## ENGLISH

**This Python script lets you quickly enable the classic (Windows 10 style) right-click context menu in Windows 11, restore the modern menu, or do nothing (exit).**  
It automates the required Windows registry changes and restarts Explorer for you.

### Features
- Activate the classic context menu with one click.
- Restore the Windows 11 default modern context menu.
- Only basic Python knowledge needed: just run, choose and go.
- Explorer restarts automatically to apply changes.
- Asks for administrator privileges if not launched as admin.

### Requirements
- Windows 11
- Python 3.x installed
- Administrator privileges

### How to Use

1. **Download or clone the repository:**
    ```bash
    git clone https://github.com/your-user/menu-contextual-windows11.git
    cd menu-contextual-windows11
    ```
2. **Run the script as administrator:**
    ```bash
    python menu_contextual.py
    ```
    If not started as admin, the script will prompt for it automatically.

3. **Choose the desired option:**
    - `1` → Enable classic context menu (Windows 10 style)
    - `2` → Restore default modern context menu (Windows 11)
    - `3` → Do nothing and exit

4. **Explorer will restart** to apply changes.

### How it works

The script adds or removes this registry key:

HKEY_CURRENT_USER\Software\Classes\CLSID{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32


- **Classic menu:** Key present, default value empty
- **Modern menu:** Key removed

> **Warning:** Changing the Windows registry can affect system configuration. Use responsibly.

### License

MIT License

---

## ESPAÑOL

**Este script en Python permite activar el menú contextual clásico (estilo Windows 10) en Windows 11, restaurar el menú moderno, o salir sin hacer cambios.**  
Automatiza los cambios en el registro y reinicia el Explorador automáticamente.

### Características

- Activa el menú contextual clásico con un solo clic.
- Restaura el menú contextual moderno por defecto de Windows 11.
- Solo necesitas Python: ejecuta, elige y listo.
- Reinicia el Explorador de Windows automáticamente.
- Solicita permisos de administrador si no los tiene.

### Requisitos

- Windows 11
- Python 3.x instalado
- Permisos de administrador

### Uso

1. **Descarga o clona este repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/menu-contextual-windows11.git
    cd menu-contextual-windows11
    ```
2. **Ejecuta el script como administrador:**
    ```bash
    python menu_contextual.py
    ```
    Si no tienes permisos de admin, el propio script lo pedirá automáticamente.

3. **Elige la opción deseada:**
    - `1` → Activar menú contextual clásico (estilo Windows 10)
    - `2` → Restaurar menú contextual moderno (Windows 11)
    - `3` → No hacer nada y salir

4. **El Explorador de Windows se reiniciará** para aplicar los cambios.

### ¿Cómo funciona?

El script añade o elimina la siguiente clave de registro:

HKEY_CURRENT_USER\Software\Classes\CLSID{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32


- **Menú clásico:** Clave presente, valor predeterminado vacío
- **Menú moderno:** Clave eliminada

> **Nota:** Modificar el registro puede afectar a la configuración del sistema. Úsalo bajo tu responsabilidad.

### Licencia

MIT License

---

### Autor

slider66

Basado en guías de [Softzone](https://www.softzone.es/windows/como-se-hace/usar-menu-contextual-clasico-windows-11/)

---

