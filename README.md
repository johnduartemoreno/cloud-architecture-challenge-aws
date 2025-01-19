# Cloud Architecture Challenge (AWS + Terraform)

Este repositorio contiene una arquitectura de referencia para un sistema de procesamiento de datos escalable en AWS, aprovisionado con Terraform.

## Estructura General

- **terraform/**: Contiene los módulos (VPC, IAM, Kinesis, Lambda, etc.) y `main.tf` para orquestarlos.
- **app/**: Scripts de Python para ingesta (`kinesis_producer.py`, `stormglass_ingestion.py`) y procesamiento en tiempo real (`kinesis_lambda.py`) y batch (`batch_ingestion.py`).
- **logs/**: Carpeta en la raíz para almacenar logs generados por los scripts.
- **slides/**: Presentación (3-5 slides) con el resumen de la arquitectura, trade-offs y mejoras futuras.

## Configuración del Entorno para Python

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

### **4. Probar los Scripts**

#### **Ejecutar los Scripts de Ingesta**

1. **Simulador IoT:**
   ```bash
   python app/ingestion/kinesis_producer.py
   ```

2. **API StormGlass:**
   ```bash
   python app/ingestion/stormglass_ingestion.py
   ```

3. **Batch Ingestion (Netflix Dataset):**
   ```bash
   python app/ingestion/batch_ingestion.py
   ```

---

### **5. Verificar los Resultados**

#### **Logs Locales**
- Los logs generados por los scripts estarán en la carpeta `logs/` en la raíz del proyecto.
  - Ejemplo: `logs/netflix_data.log`

#### **Objetos en S3**
- El archivo procesado por el script de batch ingestion se sube a S3 en la ruta:
  - `s3://aws-data-ingestion-data-bucket/processed/netflix_titles_processed.csv`

#### **Registros en Kinesis**
- Listar shards:
  ```bash
  aws kinesis list-shards --stream-name aws-data-ingestion-data-stream
  ```
- Leer registros de un shard:
  ```bash
  aws kinesis get-records --shard-iterator <ShardIterator>
  ```
- Decodificar un registro:
  ```bash
  echo "<Base64String>" | base64 --decode
  ```

---

## Infraestructura

### **Despliegue con Terraform**

1. Inicializa Terraform:
   ```bash
   terraform init
   ```

2. Verifica el plan:
   ```bash
   terraform plan
   ```

3. Aplica los cambios:
   ```bash
   terraform apply
   ```

Esto creará los recursos necesarios en AWS:
- Bucket S3 para almacenamiento.
- Stream Kinesis para ingesta en tiempo real.
- Roles IAM con permisos mínimos necesarios.
- Lambda para procesamiento en tiempo real.

---

### **Mejoras Futuras**

1. **Integración de Cost Optimization:**
   - Uso de instancias spot para procesamiento batch.

2. **Monitoreo Avanzado:**
   - Incorporar AWS CloudWatch para crear alarmas personalizadas y tableros de monitoreo.

3. **Pruebas Automatizadas:**
   - CI/CD con validaciones automáticas para los scripts y configuración de Terraform.

---

### Instalación y Ejecución Resumida

1. Clona el repositorio:
   ```bash
   git clone https://github.com/johnduartemoreno/cloud-architecture-challenge-aws.git
   cd cloud-architecture-challenge-aws
   ```

2. Configura el entorno:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r app/requirements.txt
   ```

3. Despliega la infraestructura:
   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

4. Ejecuta los scripts de ingesta:
   ```bash
   python app/ingestion/kinesis_producer.py
   python app/ingestion/stormglass_ingestion.py
   python app/ingestion/batch_ingestion.py
   ```

