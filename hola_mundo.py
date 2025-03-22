import os

def main():
    name = os.getenv("USERNAME")
    print(f"¡Hola, {name} desde GitHub Actions!")

if __name__ == "__main__":
    main()