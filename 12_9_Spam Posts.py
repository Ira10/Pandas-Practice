Calculate the percentage of spam posts in all viewed posts by day. A post is considered a spam if a string "spam" is inside keywords of the post. 
Note that the facebook_posts table stores all posts posted by users. The facebook_post_views table is an action table denoting if a user has viewed a post.


											
											
											
facebook_posts_ = facebook_posts.merge(facebook_post_views, left_on = 'post_id', right_on = 'post_id', how='inner')											
spam_ = facebook_posts_[facebook_posts_['post_keywords'].str.contains('spam')].groupby('post_date')['post_id'].count().reset_index(name= 'count_spam')											
all_ = facebook_posts_.groupby('post_date')['post_id'].count().reset_index(name= 'count_all')											
merged = spam_.merge(all_, left_on ='post_date', right_on ='post_date' )											
merged['spam_share']= (merged['count_spam']/merged['count_all'])*100											
merged[['post_date','spam_share']]											
											
											
