import requests, json

class github:
    def __init__(self, account, account_type = 'orgs'):
        self.api_url = 'https://api.github.com/'
        self.account = account
        self.actype = account_type
    # get json data of avaliable repos for 
    # specified orgs or user account
    def get_repos(self):
        url = self.api_url + self.actype + '/' + self.account + '/repos'
        return self.__get_json__(url)

    # get latest commit of github repos
    def get_commits(self,repo,count = 10):
        url = self.api_url + 'repos/%s/%s/commits?page=1&amp;per_page=%s&amp;callback=voidcommits&amp;sha=master' % (self.account,repo,str(count))
        print(url)
        return json.loads(requests.get(url= url).text.replace('/**/voidcommits(','')[1:])

    # get json from url
    def __get_json__(self, url): 
        return json.loads(requests.get(url= url).text.replace('/**/voidcommits(',''))

