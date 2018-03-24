import sys, webbrowser, requests

if len(sys.argv) > 1:
    address = sys.argv[1:]
else:
    print('No argument entered')

webbrowser.open(str(address[0]))