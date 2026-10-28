#  Pre-configured HAPI FHIR R4 Server with Synthetic Clinical Data

A plug-and-play FHIR server pre-loaded with **115 synthetic patient records** and **80,000+ clinical events** generated via Synthea. 

Designed for MedTech developers, digital health startups, and Healthcare AI researchers to bypass days of setup and test FHIR APIs instantly.

---

##  Features
- **HAPI FHIR R4 Server** running on Docker.
- **PostgreSQL 16** persistence store.
- **Pre-loaded Synthea Data:** 115 Patients, 35k+ Observations, 16k+ Procedures, 3k+ Prescriptions, and more.

## Deployment via Community AMI

You can launch a fully configured instance using our pre-built Community AMI:

- **AMI ID:** `ami-0fd53112ed419887a`
- **Region:** `eu-central-1`
- **Recommended Spec:** `t3.medium` (4 GB RAM)

### Quick Start with AMI
1. Launch an EC2 instance using AMI ID `ami-0fd53112ed419887a`.
2. Ensure Inbound Security Group rules allow **HTTP (Port 80)** and **SSH (Port 22)**.
3. Access the FHIR API via `http://<YOUR_EC2_PUBLIC_IP>/fhir/Patient` using Basic Auth credentials.

