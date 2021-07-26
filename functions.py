import requests
headers = {"Authorization": "token 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"}


def run_query(query):
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Query failed to run by returning code "
                        f"of {request.status_code}. {query}")


def findGitData(login):
    query = """
        {
          user(login:"%s") {
          name
            repositories(first: 100){
              nodes {
                name
              }
            }
          }
        }
        """ % login
    result = run_query(query)
    data = {}
    data['name'] = result['data']['user']['name']
    repositories = []
    for i in result["data"]["user"]["repositories"]['nodes']:
        repositories.append(i['name'])
    data['repositories'] = repositories
    return data
