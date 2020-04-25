from twitter_spider import TwitterSpider

def main():
	s = TwitterSpider(
		username="naval",
		csrf_token="f71f99829e0babf53c8644d8f1866ffd",
		guest_token="1254097993827078145"
	)

	s.get_tweets(s.username_to_user_id)
	
if __name__ == '__main__':
	main()