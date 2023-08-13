import whois

domain = input("Digite o domínio que deseja consultar: ")
w = whois.whois(domain)
print(w)