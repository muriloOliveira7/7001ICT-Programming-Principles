#7001ICT Programming Principles, Workshop 11, Problem 1 and 2
import time
import sys

class DNS:
    def __init__(self):
        self.ipa = {}
    
    def add_ip(self, ipa, domain):
        """Add a new IP and domain."""
        print ('Adding the new IP and domain...')
        time.sleep(2)
        if ipa not in self.ipa:
            self.ipa[ipa] = list()
        self.ipa[ipa].append(domain)
        print (domain + ' was successfully add to ' + ipa)

    def lookup_ip (self, ipa):
        """Search for the domains in the provided IP."""
        print ('Searching the domains of '+ipa+' ...')
        time.sleep(2)
        if ipa in self.ipa.keys():
            print (*self.ipa[ipa])
        else:
            print('This IP is not registered!')

    def lookup_domain(self, domain):
        """Search for the IP of the provided domain."""
        result = 'This domain is not registered!'
        print ('Searching the IP of '+domain+'...')
        time.sleep(2)
        for key, values in self.ipa.items():
            if domain in values:
                result = (key)
        print (result)

    def update_domain(self, ipa, domain):
        """Update the IP of the provided domain or add as a new one."""
        checkUpdate = 0
        for key, values in self.ipa.items():
            if domain in values:
                print ('Deleting domain '+ domain +' from the IP: '+ key +' ...')
                self.ipa[key].remove(domain)
                time.sleep(2)
                self.add_ip(ipa,domain)
                checkUpdate = 1
        
        if checkUpdate == 0:
                print ('This domain is not registered!')
                self.add_ip(ipa,domain)
                return None
    
    def admin_func(self):
        print (self.ipa)

def main_program():
    print("Welcome to the DNS Server command line.\nAvailable commands: find, findip, add, block and help for more information")
    while True:
        try:
            userInput = input('$ ')

            if userInput.lower() == 'findip':
                domain = input('Domain: ')
                dns.lookup_domain(domain)    

            elif userInput.lower() == 'find':
                ipa = input('IP: ') 
                dns.lookup_ip(ipa)

            elif userInput == 'add':
                domain = input('Enter domain: ')
                ipa = input('Enter IP Address: ')
                dns.add_ip(ipa, domain)

            elif userInput.lower() == 'block':
                ipa = input('Enter IP Address: ')
                dns.add_DomainBlocklist(ipa)

            elif userInput.lower() == 'update':
                domain = input('Enter Domain: ')
                ipa = input('Enter new IP: ')
                dns.update_domain(ipa, domain)

            elif userInput.lower() == 'help':
                print('This is the help section for the DNS command line. \nAvailable commands:\n\nfind: will provide a list of domains of an IP\nfindip: will provide the IP of a domain\nadd: will add a domain to an IP\nblock: will block an IP\n')

            elif userInput.lower() == 'sudo ls -a':
                dns.admin_func()

            elif userInput.lower() == 'quit':
                animation = "|/-\\"
                for i in range(40):
                    time.sleep(0.1)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()
                print("\nCYA!!!")
                break

            else:
                print('Command not found')

        except:
            print("Available commands: find, add, block")

dns = DNS()
main_program()

