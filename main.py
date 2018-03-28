#para requisição ao roteador
import requests
#importa classe APP do módulo kivy
from kivy.app import App
#importa BoxLayout do módulo Kivy
from kivy.uix.boxlayout import BoxLayout

class Tela(BoxLayout):
    """Classe da tela principal do aplicativo"""
    
    def login(self):
        """Requisita a função de Loguin do roteador."""
        cookies = {
            'login': '`elho.`elho.r`wd',
        }

        headers = {
            'Host': '192.168.1.1',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://192.168.1.1/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '61',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
        }

        data = 'loginUsername=admin&loginPassword=admin&rememberMe=rememberMe'
        #faz a requisição de login
        response = requests.post('http://192.168.1.1/goform/login', headers=headers, cookies=cookies, data=data, verify=False)
        

    def reboot(self):
        """Requista a função de reiniciar o roteador"""
        
        self.login()
    
        cookies = {
            'login': '`elho.`elho.r`wd',
        }

        headers = {
            'Host': '192.168.1.1',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://192.168.1.1/RgSetup.asp',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '194',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
        }

        data = 'LocalIpAddressIP0=192&LocalIpAddressIP1=168&LocalIpAddressIP2=1&LocalIpAddressIP3=1&WanLeaseAction=0&WanConnectionType=0&MtuSize=0&RestoreFactoryNo1=0x00&ApplyRgSetupAction=0&ApplyRebootAction=1'

        response = requests.post('http://192.168.1.1/goform/RgSetup', headers=headers, cookies=cookies, data=data, verify=False)
        
        

class RebootRouter(App):

    def build(self):
        return Tela()


if __name__ == "__main__":
    RebootRouter().run()
