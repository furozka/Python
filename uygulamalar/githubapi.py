import requests

class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
        self.token="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"
    def getUser(self, username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()

    def getRepos(self, username):
        response=requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()
    
    def createRepos(self, name):
        response=requests.post(self.api_url+"/user/repos?access_token="+self.token, json={
            "name": name,
            "description": "This is your third repository",
            "homepage": "http://furkanozkan.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()
    
    # def deleteRepos(self, username):
    #     response=requests.delete(self.api_url+"/users/"+username+"/repos")
    #     return(response)
github=Github()

while True:
    secim=input("1-Find User\n2-Get Repositories\n3-Create Repository\n4-Delete Repository\n5-Exit\nSecim: ")
    if secim=="5":
        break
    else:
        if secim=="1":
            username=input("Username: ")
            user=github.getUser(username)
            print(f'ID: {user["id"]}\nURL: {user["url"]}\nRepositories: {user["public_repos"]}\nFollowers: {user["followers"]}')
            
        elif secim=="2":
            username=input("Username: ")
            repos=github.getRepos(username)
            for i in repos:
                print(f'Repo Name: {i["name"]}\nDescription: {i["description"]}\nRepo URL: {i["html_url"]}')
        elif secim=="3":
            name=input("Repository Name: ")
            result=github.createRepos(name)
            print(result)
        elif secim=="4":
            owner=input("Owner: ")
            result=github.deleteRepos(owner)
            print(result)
        else:
            print("yanlis secim")
