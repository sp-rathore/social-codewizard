import pymongo, bcrypt
from pymongo import MongoClient

import bcrypt

class Posts:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):
        print(" The data content is : ", data.content)
        inserted = self.Posts.insert({"username" : data.username, "content" : data.content })
        return True

    def get_all_posts(self):
        all_posts = self.Posts.find()
        new_post = []

        for post in all_posts:
            post["user"] = self.Users.find_one({"username" : post["username"]})
            new_post.append(post)
        return new_post