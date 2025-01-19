# Cloud Architecture Challenge (AWS + Terraform)

Este repositorio contiene una arquitectura de referencia para un sistema de procesamiento de datos escalable en AWS, aprovisionado con Terraform.

## Estructura General

- **terraform/**: Contiene los módulos (VPC, IAM, Kinesis, Lambda, etc.) y `main.tf` para orquestarlos.
- **app/**: Scripts de Python para ingesta (`kinesis_producer.py`) y procesamiento en tiempo real (`lambda_realtime.py`) y batch.
- **slides/**: Presentación (3-5 slides) con el resumen de la arquitectura, trade-offs y mejoras futuras.

### Configuración del Entorno para Python

Si no tienes la carpeta `venv` y deseas asegurarte de que las dependencias estén disponibles para probar el script con el archivo `requirements.txt`, aquí tienes los pasos a seguir para crear un entorno limpio y reproducible:

---

### **1. Crear un Entorno Virtual**
Un entorno virtual ayuda a aislar las dependencias para evitar conflictos con otras aplicaciones.

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` en tu proyecto.

---

### **2. Activar el Entorno Virtual**
Dependiendo de tu sistema operativo, activa el entorno virtual:

- **En Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate
  ```

- **En Git Bash o Linux/MacOS:**
  ```bash
  source venv/bin/activate
  ```

---

### **3. Instalar las Dependencias**
Con el entorno virtual activado, instala las dependencias desde el archivo `requirements.txt`:

```bash
pip install -r app/requirements.txt
```

Esto descargará e instalará las versiones específicas de las dependencias listadas en el archivo.

---

### **4. Probar el Script**
Ahora puedes ejecutar el script en el entorno virtual:
```bash
python app/ingestion/kinesis_producer.py
```

---

### **5. Documentar el Proceso**
En el `README.md` del repositorio, agrega instrucciones para los evaluadores sobre cómo configurar el entorno:

```markdown
### Instalación y Ejecución

1. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual:**
   - En Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate
     ```
   - En Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r app/requirements.txt
   ```

4. **Ejecutar el script:**
   ```bash
   python app/ingestion/kinesis_producer.py
   ```
```

---

### **6. Evitar Versionar la Carpeta `venv`**
Asegúrate de que la carpeta `venv` no se suba al repositorio. Esto ya debería estar gestionado por tu `.gitignore`:
```plaintext
venv/
```

---

### **7. Verificar**
Si sigues estos pasos, cualquier evaluador podrá configurar el entorno y ejecutar el script sin problemas. ¿Necesitas alguna ayuda adicional? 😊

## B. Arquitectura

1. **Ingesta en Tiempo Real**:  
   - Se utilizan flujos de Kinesis para recibir datos de distintas fuentes (simuladas en `app/ingestion/kinesis_producer.py`).  

### **2. Probar el Script**
```bash
python app/ingestion/kinesis_producer.py
```

#### 3. **Listar registros (requiere un consumidor en Kinesis)**
     ```bash
     aws kinesis list-shards --stream-name aws-data-ingestion-data-stream
     ```
#### 4. **Obtener el iterador del shard:**
     ```bash
     aws kinesis get-shard-iterator \
    --stream-name aws-data-ingestion-data-stream \
    --shard-id shardId-000000000000 \
    --shard-iterator-type TRIM_HORIZON

     ```
#### 5. ** Leer registros del shard: Usa el iterador obtenido para leer registros:**
     ```bash
     aws kinesis get-records --shard-iterator <ShardIterator>
     ```
#### 6. **  Decodificar registro en Base64. **
     ```bash
     echo "eyJzZW5zb3JfaWQiOiAxLCAic2Vuc29yX3R5cGUiOiAidGVtcCIsICJ2YWx1ZSI6IDI5LjksICJ0aW1lc3RhbXAiOiAxNjg1NzQ2NTIwfQ==" | base64 --decode

     ```
2. **Procesamiento en Tiempo Real (Lambda)**:  
   - Una función Lambda suscrita a Kinesis (`Event Source Mapping`) procesa y almacena la data “cruda” en S3.  

3. **Almacenamiento**:  
   - S3 para datos “raw”.  
   - DynamoDB (o RDS) para almacenar datos procesados.  

4. **Batch Processing (Step Functions)**:  
   - Un workflow (State Machine) orquesta la lectura de datos de S3 y los procesa en modo batch, para finalmente dejarlos en DynamoDB (o en otra capa “curated”).  

5. **Seguridad**:  
   - VPC privada, subnets, NAT gateway, IAM con políticas de mínimo privilegio, cifrado en S3 y en el stream de Kinesis, etc.

## Despliegue Rápido

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/johnduartemoreno/cloud-architecture-challenge-aws.git
   cd cloud-architecture-challenge-aws/terraform
