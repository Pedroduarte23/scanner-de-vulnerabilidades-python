import socket
import sys
from threading import Thread, Semaphore

print("=" * 50)
print("   SCANNER PROFISSIONAL DE VULNERABILIDADES")
print("=" * 50)


target = input("Digite o site ou IP: ").strip()


if target.startswith("http://"):
    target = target.replace("http://", "")
elif target.startswith("https://"):
    target = target.replace("https://", "")

target = target.strip("/")


try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\n[ERRO] Host inválido. Verifique o nome do site.")
    sys.exit()

print(f"\nIP resolvido: {target_ip}")
print(f"Escaneando {target}...\n")


max_threads = 100
semaforo = Semaphore(max_threads)


arquivo = open("resultado_scan.txt", "w")


portas_abertas = []
riscos = []


servicos_comuns = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

def scan(port):
    semaforo.acquire()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)

        resultado = sock.connect_ex((target_ip, port))
        servico = servicos_comuns.get(port, "Desconhecido")

        if resultado == 0:
            estado = "ABERTA"
            portas_abertas.append(port)

            
            if port == 21:
                riscos.append("FTP aberto (possível acesso não seguro)")
            elif port == 23:
                riscos.append("TELNET aberto (protocolo inseguro)")
            elif port == 25:
                riscos.append("SMTP aberto (possível abuso de email)")

            
            if port == 80 or port == 443:
                try:
                    sock.send(
                        b"GET / HTTP/1.1\r\n"
                        b"Host: " + target.encode() + b"\r\n"
                        b"User-Agent: Mozilla/5.0\r\n"
                        b"Connection: close\r\n\r\n"
                    )
                except:
                    pass

            try:
                banner = sock.recv(1024).decode(errors="ignore").strip()
            except:
                banner = "Sem resposta"

            saida = f"[{estado}] Porta {port} ({servico})\n    -> {banner}\n"

        elif resultado == 111:
            estado = "FECHADA"
            saida = f"[{estado}] Porta {port} ({servico})\n"

        else:
            estado = "FILTRADA"
            saida = f"[{estado}] Porta {port} ({servico})\n"

        print(saida)
        arquivo.write(saida + "\n")

        sock.close()

    except Exception as e:
        print(f"[ERRO] Porta {port}: {e}")

    finally:
        semaforo.release()


threads = []


portas_teste = [21, 22, 23, 25, 53, 80, 110, 143, 443]

for port in portas_teste:
    t = Thread(target=scan, args=(port,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


print("\n" + "=" * 50)
print("RELATÓRIO FINAL")
print("=" * 50)

if portas_abertas:
    print(f"\n[+] Portas abertas: {portas_abertas}")
else:
    print("\n[!] Nenhuma porta aberta encontrada.")

if riscos:
    print("\n⚠️ Possíveis riscos identificados:")
    for r in riscos:
        print(f"- {r}")
else:
    print("\n[+] Nenhum risco crítico identificado.")

print("\nScan finalizado!")

arquivo.close()