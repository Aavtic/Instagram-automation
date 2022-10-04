import MainApi

cookies = {}
headers = {}
main = MainApi.InstaVideoDownloader(cookies=cookies, headers=headers)
link =  'THE INSTAGRAM VIDEO LINK'
link = main.get_info(link)
main.get_raw(link)