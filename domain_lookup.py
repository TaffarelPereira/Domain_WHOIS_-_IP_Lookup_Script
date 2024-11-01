import requests
from ipwhois import IPWhois

def get_ip(domain):
    try:
        response = requests.get(f'https://dns.google/resolve?name={domain}').json()
        ip = response['Answer'][0]['data']
        return ip
    except Exception as e:
        print(f"Erro ao obter IP: {e}")
        return None

def get_whois_info(ip):
    try:
        obj = IPWhois(ip)
        whois_info = obj.lookup_rdap()
        return whois_info
    except Exception as e:
        print(f"Erro ao obter informações WHOIS: {e}")
        return None

def display_info(whois_info):
    netblock = whois_info.get('network', {}).get('cidr', 'N/A')
    inetnum = whois_info.get('network', {}).get('handle', 'N/A')
    aut_num = whois_info.get('asn', 'N/A')

    print(f"Netblock: {netblock}")
    print(f"Inetnum: {inetnum}")
    print(f"Aut-num: {aut_num}")

def main():
    domain = input("Digite o domínio: ")
    ip = get_ip(domain)
    
    if ip:
        print(f"IP do domínio {domain}: {ip}")
        whois_info = get_whois_info(ip)
        
        if whois_info:
            print("\nInformações WHOIS:")
            display_info(whois_info)
        else:
            print("Não foi possível obter informações WHOIS.")
    else:
        print("Não foi possível obter o IP do domínio.")

if __name__ == "__main__":
    main()
