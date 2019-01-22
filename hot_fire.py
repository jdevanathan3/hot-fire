import os
# TODO: implement scraping script that gets next best lofi hit name and finds youtube URL
# playlist_url = https://www.youtube.com/playlist?list=PLxSfZBSiUBset-lBJZRZlIfP0zBy2Ip4Y
input_url = 'https://www.youtube.com/watch?v=6Rn_taZxrXg'
os.system('youtube-dl ' + input_url)
# TODO: implement script that loads downloaded file into garageband project and opens it