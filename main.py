from googleapiclient.discovery import build
from halo import Halo

spinner = Halo(text='Loading', spinner='dots', text_color='magenta')
my_api_key = "Your API Key"
my_cse_id = "Your CSE ID"


def google_search(search_term, site, api_key, cse_id, **kwargs):
    try:
        i = 0
        service = build("customsearch", "v1", developerKey=api_key)

        list = []
        for r in range(0, 10, 9):
            check = service.cse().list(q=search_term, start=r, cx=cse_id, **kwargs).execute()
            if check:
                list.append(check)

        for x in list:
            for y in x['items']:
                i = i + 1
                # print(y['displayLink'], i)
                if y['displayLink'] == site or 'www' + site:
                    return y['displayLink'], i
                # sits.append(y['displayLink'])
        return '\nNot Found'
    except ValueError:
        return '\nInvalid input. Please enter a valid number.'
    except ZeroDivisionError:
        return '\nCannot divide by zero.'
    except KeyboardInterrupt:
        return 'Keyboard Stoped'


if __name__ == '__main__':
    name = input('name:')
    site = input('site:')
    spinner.start()
    result = google_search(name, site, my_api_key, my_cse_id)
    spinner.stop()
    print(result)
