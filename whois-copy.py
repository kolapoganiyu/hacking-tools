import whois

def is_registered(domain_name):
    """ This funcition will check if the site is 
        registered 
    """
    try:
        w = whois.whois(domain_name) # confirming if the website is registered
    except Exception: 
        return False
    else:
        return bool(w.domain_name)
    

if __name__ == "__main__":
    print(is_registered("google.com"))
    print(is_registered("ahiohhioih.com"))
