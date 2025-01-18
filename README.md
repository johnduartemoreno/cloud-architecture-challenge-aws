# Cloud Architecture Challenge (AWS + Terraform)

Este repositorio contiene una arquitectura de referencia para un sistema de procesamiento de datos escalable en AWS, aprovisionado con Terraform.

## Estructura General

- **terraform/**: Contiene los módulos (VPC, IAM, Kinesis, Lambda, etc.) y `main.tf` para orquestarlos.
- **app/**: Scripts de Python para ingesta (`kinesis_producer.py`) y procesamiento en tiempo real (`lambda_realtime.py`) y batch.
- **slides/**: Presentación (3-5 slides) con el resumen de la arquitectura, trade-offs y mejoras futuras.

## Arquitectura

1. **Ingesta en Tiempo Real**:  
   - Se utilizan flujos de Kinesis para recibir datos de distintas fuentes (simuladas en `app/ingestion/kinesis_producer.py`).  

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
