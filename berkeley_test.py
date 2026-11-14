# zegary w ms od 12:00:00.000
master = 0
client_a = 60
client_b = 30

delay = 10

# master mierzy czas od wyslania do odpowiedzi
start = master
end = master + delay * 2 #rtt 
rtt = end - start

# klienci odpisuja po 10 ms od wyslania
reply_a = client_a + delay
reply_b = client_b + delay

# master szacuje czas klientow w momencie odebrania odpowiedzi
a_now = reply_a + rtt / 2
b_now = reply_b + rtt / 2
master_now = end

# ile zegary roznia sie od mastera
diff_a = a_now - master_now
diff_b = b_now - master_now
average = (0 + diff_a + diff_b) / 3


# przesun  zegar do wspolnej sredniej
master_after = master_now + average
a_after = a_now + (average - diff_a)
b_after = b_now + (average - diff_b)

print("berkeley")
print(f"przed: master {master} ms | a {client_a} ms | b {client_b} ms")
print(f"rtt: {rtt} ms")
print(f"roznice: a +{diff_a:.0f} ms | b +{diff_b:.0f} ms")
print(f"srednia: {average:.0f} ms")
print(f"korekty: master +{average:.0f} ms | a {average - diff_a:+.0f} ms | b {average - diff_b:+.0f} ms")
print(f"po: master {master_after:.0f} ms | a {a_after:.0f} ms | b {b_after:.0f} ms")
