import requests

def get_language_list(username):

    data = requests.get('https://api.github.com/users/{username}/repos?per_page=100'.format(username=username)).json()

    languages_list = [item['language'] for item in data]
    return languages_list

def get_unique_language_list(username):

    data = requests.get('https://api.github.com/users/{username}/repos?per_page=100'.format(username=username)).json()

    return_array = []
    languages_list = data

    for lang in languages_list:
        if lang not in return_array:
            return_array.append(lang)
    return return_array

def copyright():
        return 'Nabil Ridhwanshah (C) 2019'