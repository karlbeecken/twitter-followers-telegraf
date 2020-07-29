#!/usr/bin/env python3
import argparse
import json
import urllib.request

parser = argparse.ArgumentParser()

parser.add_argument('channelname', metavar='name', type=str,
                    help='the Twitter username')

args = parser.parse_args()

channelname = args.channelname

apiurl = "https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names={channelname}".format(
    channelname=channelname)

req = urllib.request.Request(apiurl)
r = urllib.request.urlopen(req).read()
jsonreponse = json.loads(r.decode('utf-8'))

followers_count = jsonreponse[0]['followers_count']

print(followers_count)
