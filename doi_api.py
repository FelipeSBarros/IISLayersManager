import requests

def getPaperMetaData(doi = '10.1016/j.tree.2019.01.013'):

    paper_url = f"https://api.crossref.org/works/{doi}"

    paper_metadata = requests.get(paper_url)

    if paper_metadata.status_code != 200:
        # This means something went wrong.
        print("Error on getPaperMetaData function!")
    else:
        print("Succes!")
        paper_dict = paper_metadata.json()
        result = {'paper_title': paper_dict['message']['title'][0],
            'paper_link': paper_dict['message']['URL'],
            'paper_subject': paper_dict['message']['subject'],
            'paper_author_ORCID': paper_dict['message']['author'][0]['ORCID'],
            'paper_author': paper_dict['message']['author'][0]['given'] + ' ' + paper_dict['message']['author'][0]['family'],
            'paper_year': paper_dict['message']['published-print']['date-parts'][0][0]
                  }
        return result
