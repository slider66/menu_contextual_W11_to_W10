# Windows 11 Classic Context Menu (win11-classic-context-menu)

[Versión en español abajo / Spanish version below]

## ENGLISH

**Restore the classic Windows 10 right-click menu in Windows 11 with a single click.**
This tool fixes the annoyance of the "Show more options" menu by enabling the classic full context menu permanently.

### 🚀 Download / Descarga

**[Download the latest executable (v1.0.0)](https://github.com/your-user/win11-classic-context-menu/releases/latest)**
_(No installation required. Just download and run)_

> [!IMPORTANT] > **Antivirus Warning:** Since this is a new, unsigned executable that modifies the system registry, some antivirus software (like Windows Defender) might flag it as suspicious. This is a false positive. You can review the open-source code below to verify its safety.

### Features

- **Instant Fix:** Switch between Classic (W10) and Modern (W11) menus instantly.
- **No Dependencies:** The `.exe` works on any Windows 11 PC without installing Python.
- **Automatic:** Restarts Windows Explorer automatically to apply changes.
- **Safe:** You can revert to the default Windows 11 menu at any time.

### Screenshots

|                         Before (Modern W11)                          |                          After (Classic W10)                           |
| :------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| ![Modern Menu](https://via.placeholder.com/300x400?text=Modern+Menu) | ![Classic Menu](https://via.placeholder.com/300x400?text=Classic+Menu) |

### How it works (Transparency)

The tool modifies a specific registry key to override the new menu style.
**Registry Key Modified:**
`HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`

- **Enable Classic:** Creates this key with an empty default value.
- **Restore Modern:** Deletes this key.

### How to Use (Source Code)

If you prefer running the Python script instead of the executable:

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-user/win11-classic-context-menu.git
   ```
2. **Run:**
   ```bash
   python menu_contextual.py
   ```

### License

MIT License

---

## ESPAÑOL

**Restaura el menú contextual clásico de Windows 10 en Windows 11 con un solo clic.**
Esta herramienta soluciona la molestia de tener que hacer clic en "Mostrar más opciones", activando el menú completo de siempre.

### 🚀 Descarga

**[Descargar el ejecutable (v1.0.0)](https://github.com/your-user/win11-classic-context-menu/releases/latest)**
_(No requiere instalación. Solo descargar y ejecutar)_

> [!IMPORTANT] > **Aviso de Antivirus:** Al ser un ejecutable nuevo y sin firmar que modifica el registro, algunos antivirus pueden marcarlo como sospechoso. Es un falso positivo. Puedes revisar el código fuente abierto para verificar su seguridad.

### Características

- **Solución Rápida:** Cambia entre el menú Clásico (W10) y Moderno (W11) al instante.
- **Sin Dependencias:** El `.exe` funciona en cualquier PC sin necesidad de Python.
- **Automático:** Reinicia el Explorador de Windows para aplicar los cambios.
- **Seguro:** Puedes volver al menú original de Windows 11 cuando quieras.

### Capturas de Pantalla

|                          Antes (Moderno W11)                           |                         Después (Clásico W10)                          |
| :--------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| ![Menú Moderno](https://via.placeholder.com/300x400?text=Menu+Moderno) | ![Menú Clásico](https://via.placeholder.com/300x400?text=Menu+Clasico) |

### Transparencia (Qué hace exactamente)

El script modifica una clave de registro específica para anular el estilo nuevo.
**Clave del Registro:**
`HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`

- **Activar Clásico:** Crea esta clave con un valor vacío.
- **Restaurar Moderno:** Elimina esta clave.

### Uso (Código Fuente)

Si prefieres usar el script de Python:

1. **Clonar:**
   ```bash
   git clone https://github.com/tu-usuario/win11-classic-context-menu.git
   ```
2. **Ejecutar:**
   ```bash
   python menu_contextual.py
   ```

### Autor

slider66 | Basado en guías de Softzone
