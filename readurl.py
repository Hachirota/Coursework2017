"""
Generic reader for internet URLs
This takes a url as input and tries to give output if it can otherwise throws an error. It stores downloaded data in a
directory called '.cache' so that it doesn't have to download the same data again if it hasn't changed.
You can enter a url (standalone mode) or call it from a program and it will return a tuple containing headers and body
decoded as per the encoding supplied in the input. Encoding defaults to utf-8. If there is an error it will return False
so you chould check for this.
Usage:
1. Standalone mode:
    Enter the URL and encoding at the appropriate prompts.
2. You can also import this into your programs:
    import read_url
    result = read_url.get_url(your_url, your_encoding)
    --or--
    from read_url import get_url
    result = get_url(your_url, your_encoding)
"""

def get_url(url, encoding='utf-8'):

    import httplib2

    try:
        h = httplib2.Http(".cache")
        headers, body = h.request(url)
        decoded = body.decode(encoding)

        return (headers, decoded)
    except Exception as e:
        print(e)
        return False


def main():
    url = input("Enter a URL: ")
    encoding = input("Enter a text encoding scheme (defaults to utf-8): ")
    if not encoding:
        encoding = 'utf-8'

    result = get_url(url, encoding)
    if result:
        headers = result[0]
        print("-"*50)
        for header in headers:
            print("{}: {}".format(header, headers[header]))
        print("-"*50)

        decoded = result[1]
        print(decoded)
        print("-"*50)
    else:
        print("There was an error.")


if __name__ == "__main__":
    main()