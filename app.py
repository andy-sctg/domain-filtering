import requests

bad_tld = [
  '.ru',
  '.poop',
]
bad_words = [
  'booty',
  'd34th',
]

def isWorthyDomain(domain):
  for tld in bad_tld:
    if domain.endswith(tld):
      return False
  for word in bad_words:
    if word in domain:
      return False
  return True

def cleanDomain(domain):
  domain = domain.strip()
  domain = domain.strip('/')
  return domain

def getStatus(domain, prefix='https://'):
  url = prefix + domain
  try:
    r = requests.get(url)
    return r.status_code
  except:
    return -1

def checkDomain(domain):
  secureStatus = getStatus(domain)
  # insecureStatus = getStatus(domain, prefix='http://')
  return [domain, secureStatus]


my_file = open('domains.txt', 'r')
all_domains = my_file.readlines()
all_domains = map(cleanDomain, all_domains)

target_domains = filter(isWorthyDomain, all_domains)
domain_status = map(checkDomain, target_domains)

with open('sales_goals.csv', 'w') as f:
  f.write('web domain,website response code\n')
  for data in domain_status:
    line = data[0] + ',' + str(data[1]) + '\n'
    f.write(line)
