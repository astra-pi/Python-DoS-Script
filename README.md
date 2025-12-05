![Banner](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=25&duration=3000&pause=1000&color=FF0000&center=true&vCenter=true&width=600&lines=☠️+Python+DoS+Simulation;Educational+Security+Script)

<p align="center">
  <img src="https://img.shields.io/badge/Protocol-UDP%2FHTTP-blue?style=for-the-badge&logo=internetexplorer&logoColor=white" alt="Protocol">
  <img src="https://img.shields.io/badge/Type-Stress_Testing-red?style=for-the-badge&logo=kali-linux&logoColor=white" alt="Security">
  <img src="https://img.shields.io/badge/Environment-Lab_Only-green?style=for-the-badge&logo=labview" alt="Lab">
</p>

---

## 📖 Descripción Técnica

Un ataque de **Denegación de Servicio Distribuido (DDoS)** consiste en que varios sistemas informáticos comprometidos atacan un objetivo (servidor, sitio web o recurso de red), provocando una denegación de servicio a los usuarios legítimos.

> ⚠️ **Impacto:** La avalancha de mensajes entrantes, solicitudes de conexión o paquetes malformados ralentiza o bloquea el sistema objetivo.

Esta herramienta está diseñada para simular estas condiciones en **entornos de laboratorio** para probar la calidad de servicio (QoS) y la resistencia de la infraestructura.

---

## ⚙️ Valores Predeterminados (Defaults)

Si no se especifican banderas (flags) personalizadas, el script opera bajo las siguientes condiciones:

| Parámetro | Valor por defecto |
| :--- | :--- |
| **Protocolo** | UDP (Puertos de destino aleatorios). |
| **Tamaño de Paquete** | Aleatorio (a menos que se use `--size` o `--bandwidth`). |
| **Duración** | Inundación continua (detener con `Ctrl+C` o `--time`). |
| **Velocidad** | Velocidad de línea (máxima capacidad) a menos que se use `--delay`. |

---

## 🛠️ Instrucciones de Uso y Parámetros

El script soporta argumentos para personalizar la auditoría de estrés:

* **`--time`**: Duración de la ejecución del ataque en segundos.
* **`--bandwidth`**: Especifica el ancho de banda límite a utilizar en kbps.
* **`--interval`**: Retraso en milisegundos (ms) entre el envío de paquetes.
* **`--size`**: Tamaño del paquete en bytes.

> **Nota sobre el tamaño:** El tamaño especificado corresponde al datagrama IP (incluyendo encabezados IP y UDP). El tamaño real en la interfaz puede variar debido a la encapsulación de Capa 2 (Ethernet).

### Reglas de lógica:
1.  El parámetro `--size` se ignora si se especifican simultáneamente `--bandwidth` y `--delay`.
2.  Si se usa `--bandwidth` sin `--size`, el tamaño del paquete se fija automáticamente en **256 bytes**.

---

## ⚖️ Advertencias y Exenciones de Responsabilidad (Disclaimer)

**El uso de este software está sujeto a las siguientes condiciones éticas:**

1.  **Terceros:** La inundación de redes o hosts de terceros sin autorización escrita se considera una actividad delictiva en la mayoría de las jurisdicciones.
2.  **Self-Hosting:** Inundar sus propios hosts o redes de producción puede causar pérdidas de servicio reales; hágalo con precaución.
3.  **Propósito:** Se utiliza principalmente en **entornos de laboratorio** para pruebas de Calidad de Servicio (QoS).
4.  **Rendimiento:** Para pruebas de estrés empresarial a gran escala, se recomiendan soluciones de hardware dedicado.

---

<p align="center">
  Research & Education | <a href="https://github.com/astra-pi">astra-pi</a>
</p>
