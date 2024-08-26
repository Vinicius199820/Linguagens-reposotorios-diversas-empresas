import requests
import pandas as pd

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'Authorization': 'bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'}
        
    # Método para listar os repositórios, passando de pagina em pagina
    def lista_repositorios(self):
        repos_list = []
        for page_num in range(1,20):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list
    
    #Realizando a seleção apenas dos nomes dos repositorios
    def nomes_repos (self, repos_list): 
        repo_names=[] 
        for page in repos_list:
                for repo in page:
                        try:
                            repo_names.append(repo['name'])
                        except: 
                                pass
        return repo_names
    #Seleção dos nomes das linguagens utilizadas nos repositorios

    def nomes_linguagens(self, repos_list):
        repo_languages=[]
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass
        return repo_languages

    def cria_df_linguagens(self):
        #criando um dataframe com os dados dos repositórios, as variaveis recebem as funções e sao puxadas pelo dataFrame

        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados
    
    # Método para listar os seguidores, passando de pagina em pagina
    def seguidores_amzn(self):
        followers_list = []
        page_num = 1
        seguidores = []
    
        while True:
            try:
                url = f'{self.api_base_url}/users/{self.owner}/followers?page={page_num}'
                response = requests.get(url, headers=self.headers)
                if not response.json():  
                    break
                followers_list.append(response.json())
                page_num += 1
            except:
                followers_list.append(None)
                break
        total_followers = 0
        for page in followers_list:
            total_followers += len(page)
    
        for page in followers_list:
            for follower in page:
                seguidores.append(follower['login'])
        return seguidores
    
    #Criando um dataframe com os seguidores
    def cria_df_seguidores(self):
        seguidores = self.seguidores_amzn()
        dados = pd.DataFrame()
        dados['seguidores'] = seguidores
        return dados
    
    #
    
#amazon_rep = DadosRepositorios('amzn')
#ling_mais_usadas_amzn = amazon_rep.cria_df_linguagens()

#netflix_rep = DadosRepositorios('netflix')
#ling_mais_usadas_netflix = netflix_rep.cria_df_linguagens()

#spotify_rep = DadosRepositorios('spotify')
#ling_mais_usadas_spotify = spotify_rep.cria_df_linguagens()

#amazon_seguidores = DadosRepositorios('amzn')
#seguidores_amzn = amazon_seguidores.cria_df_seguidores()

# Salvando os dados

#ling_mais_usadas_amzn.to_csv('dados/linguagens_amzn.csv')
#ling_mais_usadas_netflix.to_csv('dados/linguagens_netflix.csv')
#ling_mais_usadas_spotify.to_csv('dados/linguagens_spotify.csv')
#seguidores_amzn.to_csv('dados/seguidores_amzn.csv')



#pra executar o script python3 dados_repos.py por exemplo