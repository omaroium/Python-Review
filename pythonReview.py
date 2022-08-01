def create_youtube_video(title,discription):
	video={"title":title, "discription":discription ,"like":0,"dislike":0,"comments":{},"hashtag":[]}
	for i in range(0,5):
		video['hashtag'].append(input("Enter your value: "))
	return video

def like(video):
	if "like" in video:
		video["like"]+=1
	return video 

def dislike(video):
	if "dislike" in video:
		video["dislike"]+=1
	return video 

def add_comment(video,username,comment_text):
	video["comments"][username]=comment_text
	return video
video=create_youtube_video(15,25)
video1=create_youtube_video(12,25)
like(video1)
add_comment(video1,"omar","hello")
print(video1)
def similarity(video,video1):
	count=0
	for i in range(0,5):
		for j in range(0,5):
			if video1['hashtag'][i]==video1['hashtag'][j]:
				count+=1
	print(count*4)			
similarity(video,video1)