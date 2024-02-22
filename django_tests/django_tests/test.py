all_tr = soup.find_all()


names = {'naam' : ['Naam:', 'Name:', ]}


for tr in all_tr:
    if tr.split(':')[0] in names['naam']:
        'do iets'

for tr in all_tr:
    for word in names['naam']:
        if word in tr:
            'do iest'




class Blog:
    def __init__(self, name, tagline):
        self.name = name
        self.tagline = tagline

# Direct instantiation
b2 = Blog(name="Cheddar Talk", tagline="Thoughts on cheese.")
b2.save()




blog_data = {
    "name": "Cheddar Talk",
    "tagline": "Thoughts on cheese."
}

b2 = Blog()
for key, value in blog_data.items():
    setattr(b2, key, value)
b2.save()







class Blog:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

# Your variable names and values as a dictionary
attributes = {
    "name": "Cheddar Talk",
    "tagline": "Thoughts on cheese."
}

# Creating an instance with dynamic attributes
b2 = Blog(**attributes)