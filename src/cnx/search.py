

# SEARCH_URL = 'http://archive.cnx.org/search?'
#
# search_string = 'Biology'

# payload = {
#     'q': search_string,
#     'title': search_string,
#     'authorId': 'OpenStaxCollege',
#     'sort': 'popularity'
# }


# r = requests.get(SEARCH_URL, params=payload)
# # print r.text
#
# if r.status_code == 200:
#     data = r.json()
#
#     results = data['results']['items']
#
#     for i in results:
#         if any([item.get('id') == 'OpenStaxCollege' for item in i['authors']])\
#                 and ('title', 'Biology') in list(i.items()):
#             print json.dumps(i, indent=4)
# else:
#     print('Error')
