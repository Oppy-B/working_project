from urllib.parse import urlparse

def get_domain_name(url):
    try:
        parse_url = urlparse(url).netloc
        results = parse_url.split('.')
        return results[-2] + '.' + results[-1]

    except:
        return ''

a = get_domain_name('http://eportal.oauife.edu.ng')
print(a)