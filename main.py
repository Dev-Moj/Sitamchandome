from googleapiclient.discovery import build
from halo import Halo

spinner = Halo(text='Loading', spinner='dots', text_color='magenta')
my_api_key = "AIzaSyCbdKgFgr4Olg0Cwx_InLaSIi72B77in58"
my_cse_id = "55ef8e5c221f8461c"


def google_search(search_term, url, api_key, cse_id, **kwargs):
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
                if y['displayLink'] == url or y['displayLink'] == 'www.' + url:
                    print('www' + url)
                    return y['displayLink'], i
        return '\nNot Found'
    except ValueError:
        return '\nInvalid input. Please enter a valid number.'
    except ZeroDivisionError:
        return '\nCannot divide by zero.'
    except KeyboardInterrupt:
        return 'Keyboard Stoped'


if __name__ == '__main__':
    name = input('Search Text:')
    site = input('Site Url:')
    spinner.start()
    result = google_search(name, site, my_api_key, my_cse_id)
    spinner.stop()
    print(result)
