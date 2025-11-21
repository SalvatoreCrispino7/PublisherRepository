import subprocess

# Sostituisci <id> con il valore reale dell'ID da aggiornare
id_editore = "6920cf6f97d2026da822c4b6"

curl_command = [
    "curl",
    "-X", "PUT",
    f"http://localhost:8888/publishers/{id_editore}",
    "-H", "Content-Type: application/json",
    "-d", '{"name": "prova aggiornata", "founded_year": 1910, "country": "Italia"}'
]

result = subprocess.run(curl_command, capture_output=True, text=True)

print("Output:", result.stdout)
print("Errore:", result.stderr)
