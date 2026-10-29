import urllib.request
import json

# Synthea reposundan doğrudan çalışan güncel hasta paketi linki
URL = "https://raw.githubusercontent.com/synthetichealth/synthea/master/src/test/resources/generic/patient_bundle.json"

print("Sentetik veri indiriliyor ve HAPI FHIR sunucusuna yükleniyor...")

try:
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = response.read()

    post_req = urllib.request.Request(
        'http://localhost:8080/fhir',
        data=data,
        headers={'Content-Type': 'application/fhir+json'}
    )
    with urllib.request.urlopen(post_req) as post_response:
        print(f"Başarıyla yüklendi! (HTTP Status: {post_response.status})")
except Exception as e:
    print(f"Hata oluştu: {e}")

