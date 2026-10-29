# Pre-configured HAPI FHIR R4 Server with Synthetic Clinical Data

A plug-and-play FHIR server pre-loaded with **111 synthetic patient records** and **34,800+ clinical resources** generated via Synthea.

Designed for MedTech developers, digital health startups, and Healthcare AI researchers to bypass days of setup and test FHIR APIs instantly.

---

## Features

* **HAPI FHIR R4 Server** running on Docker.
* **PostgreSQL 16** persistence store.
* **Nginx Reverse Proxy** optimized for large transaction bundles.
* **Pre-loaded Synthea Data:** 111 Patients, 34,843 total FHIR resources (Encounters, Observations, Conditions, Procedures, Prescriptions, and more).
* **Automated Data Ingestion:** Includes `load_synthetic.py` for continuous synthetic dataset imports.

---

## Deployment via Community AMI

You can launch a fully configured instance using our pre-built Community AMI:

* **AMI ID:** `ami-0da39775ee58ade04`
* **Region:** `eu-central-1`
* **Recommended Spec:** `t3.medium` (4 GB RAM)

### Quick Start with AMI

1. Launch an EC2 instance using the AMI ID above.
2. Ensure Inbound Security Group rules allow **HTTP (Port 80)** and **SSH (Port 22)**.
3. Access the FHIR API directly via:
   ```text
   http://<YOUR_EC2_PUBLIC_IP>/fhir/Patient

