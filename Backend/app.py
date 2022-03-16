from flask import Flask

@app.post("/api/login")
def post_login():
success = False
try:
username = request.json["username"]
password = request.json["password"]
success, user = db.attempt_login(username, password)
except:
return Response("Authentication Failure", mimetype=“plain/text”, status=401)
if (success):
user_json = json.dumps(user, default=str)
return Response(user_json, mimetype=“application/json”, status=200)
else:
return Response("Authentication Failure", mimetype=“plain/text”, status=401)

@app.delete("/api/login")
def delete_login()
success = False
try:
    delete = request.delete["logintoken"]
except:
    if (success)
    return Response("User has been deleted")
    else:
        return Response("bad Gateway" mimetype= plain/text status=502)

@app.get("/api/users")
def get_users()
success = False
try:
    get = request.json["username"]
    get = request.json["password"]
except:
    return Response("BAD REQUEST" mimetype= plain/text status=400)
    if (success)
    return Response( user.json mimetype= plaintext status= 100)
    
    else:
        return Response("NotFound" mimetype= plain/text status=404)


@app.post("/api/user")
def post_user()
success = False
try:
    post = tweet.json("create tweets")
except:
    if(success):
        post.json = json.dumps(tweet,default=str)
    else:
        return Response ("Unauthorized" mimetype= plain/text status= 401):

@app.patch("/api/user")
def patch_user()
success =False
try:
    patch = request.json("updates")
except:
    if (success)
    patch.json = json.dumps(update, default=str)
    else:
        return Response ("Unauthorized" mimetype= plain/text status=401):

@app.delete("/api/user")
def delete_user()
success = False
try:
    delete = request.delete["login_token"]
except:
    if (success):
        return Response("User has been Deleted")
    else:
        return Response("Bad Gateway" mimetype= plain/text status=502):

@app.get("/api/tweets")
def get_tweets()
success = False
try:
    get = request.json["tweets"]
except:
    return Response ("Bad Gateway" mimetype= plain/text status=502)
    if (success):
        return Response(tweet.json mimetype= application/json)
    else:
        return response ("Bad Gateway" mimetype= plain/text status=502)


@app.patch("/api/tweets")
def patch_tweets()
success =False
try:
    patch = request.patch["tweets"]
except:
    return response ("Bad Request" mimetype= plain/text status= 400)
    if (success):
        patch.json = json.dump (update, default= str)
    else:
        return response("Bad request" mimetype= plain/text status= 400)



@api.get("/api/followers")
def get_followers()
success = False
try:
    followers = request.json["followers"]
except:
    return response("bad request" mimetype= plain/text status= 400)
if (success):
    return response ("followers.json" mimetype= application/data)
else:
    return reponse ("Bad Gateway" mimetype= plain/text status= 502)


@api.get("/api/follow")
def get_follow()
success = False
try:
    follow = request.json ["follow"]
except:
    return Response("bad request" mimetype = plain/text status= 400)
if (success)
    return response(follows.json mimetype= application/data)
else:
    return response("Bad Gateway" mimetype= plain/text status= 502)


@api.post("/api/follow")
def post_follow()
success =False
try:
    post = request.json["follow"]
except:
    return Response("Bad Request" mimetype= plain/text status= 400)
if (success):
    post.json(json.dump defaut= str)
else:
    return Response("Bad Gateway" mimetype= plain/text status= 502)

@api.delete("/api/follow")
def delete_follow()
success = False
try:
    delete = request.delete["follow"]
except:
    return response("Bad Request" mimetype= plain/text status=400)
if (success):
    return Response("Successfully deleted")
else:
    return Response("Bad Gateway" mimetype= plain/text status= 502)

@api.post("/api/tweets")
def post_tweets()
success = False
try:
    post = request.json["tweets"]
except:
    return reponse("Bad Request" mimetype= plain/text status= 400)
if (success):
    post.json(json.dumps default= str)
else:
    return Response("Bad Gateway" mimetype= plain/text status= 502)

@api.get("/api/tweets")
def get_tweets()
success = False
try:
    get= request.json["tweets"]
except:
    return Response("Bad Request" mimetype= plain/text status= 400)
if (success):
    return Response(tweet.json mimetype=application/data)
    tweet.json(json.dump, default=str)
else:
    return Response("Bad Gateway" mimetype= plain/text status= 502)

@api.patch("/api/tweets")
def patch_tweets()
success = False
try:
    patch = request.patch["tweets"]
except:
    return Response("Bad Request"mimetyp= plain/text status= 400)
if (success):
    return Response(patch.tweets mimetype=application/data)
    patch.tweets(json.dumps default=str)
else:
    return Response("Bad Gateway"mimetype= plain/text status=502)

@api.delete("/api/tweets")
def delete_tweets()
success = False
try:
    delete = request.delete["tweets"]
except:
    return Response("Bad Request" mimetype= plain/text status= 400)
if (success):
    return ("This tweet has been deleted")
else:
    return Response ("Bad Gateway"mimetype=plain/text status=502)

@api.get("/api/tweet_likes")
def get_likes()
success =False
try:
    get = request.json("tweets_likes")
except:
    return Respose ("Bad Request" mimetype= plain/text status= 400)
if (success):
    return response(tweet_likes mimetype= application/data)
else:
    return response("Bad Gateway"mimetype= plain/text status=502)

@api.post("/api/tweet_likes")
def post_likes()
success = False
try:
    post = request.json["tweet_likes"]
except:
    return response("Bad Request"mimetype= plain/text status=400)
if (success):
    return response(post.json default= str)
else:
    return response("Bad Gateway"mimetype= plain/text status=502)


@api.delete("/api/tweet_likes")
def delete_likes()
success = False
try:
    delete_likes = request.delete["tweet_likes"]
except:
    return response ("Bad Request"mimetype= plain/text status= 400)
if (success):
    return response("like has been deleted")
else:
    return response("Bad Gateway"mimetype=plain/text status=502)

@api.get("/api/comments")
def get_comments()
success = False
try:
    get.comments= request.json["comments"]
except:
    Return Response("Bad Request"mimetype= plain/text status=400)
if (success):
    return Response(get.comments mimetype=application/data)
else: 
    return Response("Bad Gateway"mimetype=plain/text status=502)

@api.post("/api/comments")
def post_comments()
success = False
try:
    post.comments = request.json["comments"]
except:
    return Response("Bad Request"mimetype= plain/text status= 400)
if (success):
    return Response( post.comments mimetype= application/data)
else:
    return response ("Bad Gateway" mimetype= plain/text status=502)

@api.delete("/api/comments")
def delete_comments()
success = False
try:
    delete.comments = request.delete["comments"]
except:
    return Response("Bad Request" mimetype=plain/text status=400)
if (success):
    return response("Comment has been deleted")
else:
    return response("Bad Gateway" mimetype= plain/text status= 502)

@api.patch("/api/comments")
def patch_comments()
success = False
try:
    patch.comments = Request.json["comments"]
except:
    return response("Bad Request"mimetype=plain/text status=400)
if (success):
    return  response(patch.comments default=str)
else:
    return response ("Bad Gateway"mimetype=plain/text status=502)

@api.get("/api/comment_likes")
def get_commentlikes()
success = False
try:
    get.comment_likes = request.json["comment_likes"]
except:
    return response("Bad Request"mimetype=plain/text status=400)
if (success):
    return get.comment_likes(json.dump default=str)
else:
    return response ("Bad Gateway"mimetype= plain/text status=502)

@api.delete("/api/comment_likes")
def delete_commentlikes()
success = False
try:
    delete.comment_likes = request.delete["comment_likes"]
except:
    return Response("Bad Request"mimetype= plain/text status=400)
if (success):
    return response ("this like has been deleted")
else:
    return response ("Bad Gateway"mimetype= plain/text status=502)

@api.post("/api/comment_likes")
def post_commentlikes()
success = False
try:
    post.comment_likes = request.json["comment_likes"]
except:
    return Response ("Bad Request"mimetype=plain/text status=400)
if (success):
    return response(post.comment_likes mimetype= application/data)
else:
    return response ("Bad Gateway"mimetype=plain/text status=502)


