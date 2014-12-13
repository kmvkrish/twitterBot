import tweepy

auth = tweepy.OAuthHandler("your consumer key here", "Your consumer secret here")
auth.set_access_token("your access token here", "your access token secret here")

api = tweepy.API(auth,timeout=5,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if api:
    print "Authenticated"

list = []

tweets = []

follower = []

def find_friends(username):
    user = api.get_user(username)
    if username == api.me().screen_name:
        print "I am "+username+"\n"
    else:
        print "Hello "+api.me().screen_name+". I am "+user.screen_name
    for friends in user.friends():
        list.append(friends.screen_name)
    print list


def get_tweets(username):
    for tweet in api.user_timeline(username):
        tweets.append(tweet.text)
    print tweets    

def get_followers(username):
    for followers in api.followers(username):
        follower.append(followers.screen_name)
    print follower

def update(status):
    if len(status) > 10 :
        if api.update_status(status):
            print "Status updated"
    else:
        print "Enter message between 10-140 characters"

def message(username,text):
    sent = api.send_direct_message(screen_name=username,text=text)
    if sent:
         print "Message is sent ",sent.id,"\n"
    else:
        print "Message Not sent"

def destroy_message(id):
    if api.destroy_direct_message(id):
        print "Message deleted"
    else:
        print "Error occured"

def check_friendship(source,target):
    fs = api.show_friendship(source_screen_name=source,target_screen_name=target)
    if fs:
        print fs
    else:
        print "Some error occured!"

print "1. Find Friends 2. Get Tweets of User 3. Get Followers List 4. Update Status 5. Send Direct Message 6. Undo Last Message 7. Check Friendship\n"

choice = int(raw_input("Enter a choice"))

if choice == 1:
    find_friends(raw_input("Enter a username"))

elif choice == 2:
    get_tweets(raw_input("Enter a username"))

elif choice == 3:
    get_followers(raw_input("Enter a username "))

elif choice == 4:
    update(raw_input("Enter a message below 140 characters:"))

elif choice == 5:
    username = raw_input("Enter a recipient name")
    text = raw_input("Enter message")
    if (len(text) > 10) and (len(text) < 140):
        message(username,text)
    else:
        print "Enter message between 10-140 characters"

elif choice == 6:
    destroy_message(raw_input("Enter last message ID"))
   
elif choice == 7:
    source = raw_input("Enter a username")
    target = raw_input("Enter another username")
    if len(source) > 0 and len(target) > 0:
        check_friendship(source,target)

else:
    print "Please Enter a valid Option\n"
