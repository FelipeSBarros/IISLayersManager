import requests

def getPaperMetaData(doi = '10.1016/j.tree.2019.01.013'):
    sub = ''
    orcid = ''

    empty_result = {'paper_title': '',
              'paper_link': '',
              'paper_subject': sub,
              'paper_author_ORCID': orcid,
              'paper_author': '',
              'paper_year': ''
              }

    if doi == '':
        print("No DOI passed")
        result = empty_result
        return result
    else:
        print("DOI passed")
        paper_url = f"https://api.crossref.org/works/{doi}"
        # retriving paper metadata
        paper_metadata = requests.get(paper_url)
        # Testing if paper found
        if paper_metadata.status_code != 200:
            # This means something went wrong.
            print("Error on finding paper metadata!")
            result = empty_result
            return result
        else:
            print("Paper found!")
            paper_dict = paper_metadata.json()

            if 'subject' in paper_dict['message'].keys():
                sub = paper_dict['message']['subject']

            if 'ORCID' in paper_dict['message']['author'][0].keys():
                orcid = paper_dict['message']['author'][0]['ORCID']

            result = {'paper_title': paper_dict['message']['title'][0],
                'paper_link': paper_dict['message']['URL'],
                'paper_subject': sub,
                'paper_author_ORCID': orcid,
                'paper_author': paper_dict['message']['author'][0]['given'] + ' ' + paper_dict['message']['author'][0]['family'],
                'paper_year': paper_dict['message']['published-print']['date-parts'][0][0]
                      }
            return result
