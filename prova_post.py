import subprocess

curl_command = [
    "curl",
    "-X", "POST",
    "http://localhost:8888/publishers",
    "-H", "Content-Type: application/json",
    "-d", '{"name": "prova", "founded_year": 1907, "country": "Italia"}'
]

result = subprocess.run(curl_command, capture_output=True, text=True)

print("Output:", result.stdout)
print("Errore:", result.stderr)
