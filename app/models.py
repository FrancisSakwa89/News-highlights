class News:
    def __init__(self,source,link,country,id,description):
        self.source = source
        self.link = link
        self.country = country
        self.id = id
        self.description = description


class Articles:
    def __init__(self,author,title,description,url,poster,time):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.poster = poster
        self.time = time       

class Review:

    all_reviews = []

    def __init__(self,author,title,description,url,poster,time,review):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.poster = poster
        self.time = time     
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.articles_id == id:
                response.append(review)

        return response        