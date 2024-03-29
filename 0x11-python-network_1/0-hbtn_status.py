#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print(
            'Body response:\n\t- type: {}\n\t- content: {}\n\t- \
utf8 content: {}'.format(type(html), html, str(html, 'utf-8'))
        )
