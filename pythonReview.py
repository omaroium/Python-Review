def create_youtube_video(title,discription):
	video={"title":title, "discription":discription ,"like":0,"dislike":0,"comments":{}}
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

video1=create_youtube_video(12,25)
like(video1)
add_comment(video1,"omar","hello")
print(video1)