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

my_file = open('domains.txt', 'r')
all_domains = my_file.readlines()
all_domains = map(cleanDomain, all_domains)

target_domains = filter(isWorthyDomain, all_domains)
with open('sales_goals.txt', 'w') as f:
    for domain in target_domains:
        f.write("%s\n" % domain)