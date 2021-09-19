class Article:

    """
    article class defining article objects

    """

    def __init__(self, name, author, title, description, publishedAt, imageUrl, url):

        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.imageUrl = imageUrl
        self.url = url
