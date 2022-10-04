import MainApi

cookies = {}
headers = {}
main = MainApi.InstaVideoDownloader(cookies=cookies, headers=headers)
link =  str(input('Enter the post url :> '))
link = main.get_info(link)
main.get_raw(link)
