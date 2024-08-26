import requests
import base64

class ManipulaRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        # Store the access token securely, such as in an environment variable or a configuration file
        self.access_token = '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'
        self.headers = {'Authorization': 'bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'}
        
    def cria_repo(self, nome_repo):
        data = {
            "name": nome_repo,
            "description": "Dados dos repositórios de algumas empresas",
            "private": False
        }
        response = requests.post(f'{self.api_base_url}/user/repos', json=data, headers=self.headers)
        print(f'status_code criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):

        with open(caminho_arquivo, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        #Realizando upload

        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}"
        data = {
            "message": "Adicionando arquivo",
            "content": encoded_content.decode('utf-8')
        }
        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')

#instanciando um objeto
novo_repo = ManipulaRepositorios('Vinicius199820')

#criando o repositorio
nome_repo = 'Linguagens-reposotorios-diversas-empresas'
novo_repo.cria_repo(nome_repo)

#add arquivos salvos no repositorio criado

novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
novo_repo.add_arquivo(nome_repo, 'seguidores_amazn.csv', 'dados/seguidores_amzn.csv')

#pra executar o script python3 manipula_repos.py por exemplo