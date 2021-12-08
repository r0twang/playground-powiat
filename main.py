from requests_oauthlib.compliance_fixes import facebook

from turn import play_turn
from PIL import Image
from log import log_info, log_error
from datetime import datetime
from twitter import *
import facebook as fb
from export import create_map
from select_turn_type import select_turn_type
import json
import twitter
import tweepy
import twython

i = 0
while i < 5:
    try:
        post_message, powiaty_left, powiaty_ammount = select_turn_type()
        i = 10
        items_to_sort = [(v, k) for (k, v) in zip(powiaty_ammount.keys(), powiaty_ammount.values())]
        items_to_sort.sort(reverse = True)
        with open('map-data/names.json', encoding='utf-8') as f:
            powiaty_names = json.load(f)

        if (len(items_to_sort) > 10):
            range_len = 10
        else:
            range_len = len(items_to_sort)
        message = 'Top {} regiony by number of controlled territories:'.format(range_len)
        for j in range(range_len):
            powiat_name = powiaty_names[items_to_sort[j][1]]
            message = '{}\n{}: {}'.format(message, powiat_name, items_to_sort[j][0])
        log_info(message)
    except Exception as e:
        i += 1
        log_error('An error {} occured, trying again [{}/{}].'.format(e, i, 5))
        if (i == 5):
            quit()

# i = 0
# while i < 5:
#     try:
#         was_posted = False
#
#         if (not was_posted):
#             image = Image.open('overall-map.png')
#             bbox = image.convert('RGBa').getbbox()
#             image = image.crop(bbox)
#             image.save('overall-map.png')
#             image = Image.open('detail-map.png')
#             bbox = image.convert('RGBa').getbbox()
#             image = image.crop(bbox)
#             image.save('detail-map.png')
#
#             with open('api-key.txt', 'r') as f:
#                 # api_key = f.readline().rstrip()
#                 consumer_key = f.readline().rstrip()
#                 consumer_secret = f.readline().rstrip()
#                 access_token = f.readline().rstrip()
#                 access_token_secret = f.readline().rstrip()
#
#             # facebook = fb.GraphAPI(access_token = api_key)
#             twitter_api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)
#             tweepy_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#             tweepy_auth.set_access_token(access_token, access_token_secret)
#             tweepy_auth.secure = True
#             tweepy_api = tweepy.API(tweepy_auth)
#             twython_api = twython.Twython(consumer_key, consumer_secret, access_token, access_token_secret)
#             # post_response = facebook.put_photo(image = open('overall-map.png', 'rb'), message = post_message)
#             twitter_post_response = twitter_api.PostUpdate(post_message, media=open('overall-map.png', 'rb'))
#             print("twitter_post_reponse: ", twitter_post_response)
#
#         was_posted = True
#         twitter_post_id = twitter_post_response.id
#         print("twitter_post_id ", twitter_post_id)
#         # twitter_image_response =twitter_post_response.UpdateImage(image='detail-map.png')
#         # twitter_photo_id = twitter_image_response
#
#         # post_id = post_response['post_id']
#         # log_info('Post was created at {} with id {}'.format(datetime.now(), post_id))
#         # image_response = facebook.put_photo(image = open('detail-map.png', 'rb'), no_story = True, published = False)
#         # photo_id = image_response['id']
#
#         with open('map-data/names.json', encoding='utf-8') as f:
#             powiaty_names = json.load(f)
#
#         items_to_sort = [(v, k) for (k, v) in zip(powiaty_ammount.keys(), powiaty_ammount.values())]
#         items_to_sort.sort(reverse = True)
#
#         if (len(items_to_sort) > 10) :
#             range_len = 10
#         else:
#             range_len = len(items_to_sort)
#
#         message = 'Top {} regiony by number of controlled territories:'.format(range_len)
#         for j in range(range_len):
#             powiat_name = powiaty_names[items_to_sort[j][1]]
#             message = '{}\n{}: {}'.format(message, powiat_name, items_to_sort[j][0])
#
#         detail_map = open('detail-map.png', 'rb')
#         response = twython_api.upload_media(media=detail_map)
#         print('response[''media_id''] :', response['media_id'])
#         print('')
#         # twython_api.update_status(status=message, media_ids=[response['media_id']])
#         # twython_api.update_status(status=message, in_reply_to_status_id=twitter_post_id)
#         # twython_api.update_status(m='@wepeko3', status=message, media_ids=[response['media_id']])
#         # twython_api.update_status(status=message, media_ids=response['media_id'], in_reply_to_status_id=twitter_post_id)
#         # twython_api.update_status(m='@wepeko3', status=message,
#         #                           media_ids=response['media_id'], in_reply_to_status_id=twitter_post_id)
#         twython_api.update_status(m='@wepeko3',
#                                   status=message, media_ids=response['media_id'],
#                                   in_reply_to_status_id=twitter_post_id)
#         # twython_api.update_status(auto_populate_reply_metadata=True,
#         #                           status='prawmapopodobnie', in_reply_to_status_id=twitter_post_id)
#
#         # comment_response = facebook.put_object(parent_object = post_id, message = message, connection_name = 'comments', attachment_id = photo_id)
#         # comment_id = comment_response['id']
#         # facebook.put_comment(comment_id, 'prawmapopodobnie')
#
#         print(message)
#
#         with open('map-data/status.txt', 'a') as f:
#             f.write('{}'.format(items_to_sort[0][1]))
#
#         i = 10
#     except Exception as e:
#         i += 1
#         log_error('An error {} occured, trying again [{}/{}].'.format(e, i, 5))
#         if (i == 5):
#             quit()

create_map()
