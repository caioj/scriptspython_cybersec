import dns.resolver

alvo = 'google.com' #Alvo a ser verificado

result = dns.resolver.resolve(alvo, 'A')
for ipval in result:
    print('IP: ', ipval.to_text())
    ip_alvo = ipval.to_text()

#--------------------------------------------------------------------

print("--------------------")

try:
    result = dns.resolver.resolve(alvo, 'CNAME')
    for cnameval in result:
        print('CNAME: ', cnameval.target)
except:
    pass

#--------------------------------------------------------------------

print("--------------------")

result = dns.resolver.resolve(alvo, 'AAAA')

for val in result:
    print('AAAA: ', ipval.to_text())

#--------------------------------------------------------------------

print("--------------------")

result = dns.resolver.resolve(ip_alvo+'.in-addr.arpa', 'PTR')

for val in result:
    print('PTR: ', val.to_text())

#--------------------------------------------------------------------

print("--------------------")

result = dns.resolver.resolve(alvo,'NS')

for val in result:
    print('NS: ', val.to_text())

#--------------------------------------------------------------------

print("--------------------")

result = dns.resolver.resolve(alvo,'MX')

for exdata in result:
    print('MX: ', exdata.to_text())

#--------------------------------------------------------------------

print("--------------------")

result = dns.resolver.resolve(alvo,'SOA')

for val in result:
    print('SOA: ', val.to_text())

#--------------------------------------------------------------------

print("--------------------")

result = dns.resolver.resolve(alvo,'TXT')

for val in result:
    print('TXT: ', val.to_text())
