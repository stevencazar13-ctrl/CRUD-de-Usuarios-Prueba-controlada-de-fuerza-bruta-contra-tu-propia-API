import requests

url = "http://localhost:8000"

def get_users():
    resp = requests.get(f"{url}/List")
    resp.raise_for_status()
    return resp.json()

def get_credentials():
    users = get_users()
    
    if not users:
        print("Error al encontar usuarios")
        return
    
    print("\nDatos obtenidos:")
    for user in users:
        print(f"\nID: {user['id']}")
        print(f"Email: {user['email']}")
        print(f"Password: {user['password']}\n")

get_credentials()