# poczatkowe zegary w ms 
server = 0
client_a = 60
client_b = 30

delay = 10

# klienci zapisuja czas wyslania zapytania
start_a = client_a
start_b = client_b

# serwer odsyla swoj czas po otrzymaniu pytania
server_reply = server + delay

# klienci zapisuja czas otrzymania odpowiedzi
end_a = client_a + delay * 2
end_b = client_b + delay * 2

# kazdy klient sam liczy rtt
rtt_a = end_a - start_a
rtt_b = end_b - start_b

# czas serwera plus polowa rtt = nowy czas klienta
a_after = server_reply + rtt_a / 2
b_after = server_reply + rtt_b / 2

# korekta to nowy czas minus obecny czas klienta
correction_a = a_after - end_a
correction_b = b_after - end_b
server_after = server + delay * 2

print("cristian")
print(f"przed: serwer {server} ms | a {client_a} ms | b {client_b} ms")
print(f"rtt: a {rtt_a} ms | b {rtt_b} ms")
print(f"korekty: a {correction_a:+.0f} ms | b {correction_b:+.0f} ms")
print(f"po: serwer {server_after} ms | a {a_after:.0f} ms | b {b_after:.0f} ms")
