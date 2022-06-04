# find topic occurrence in review

# solution 1: start with review
def find_topic_occur_in_review_1(topics, reviews):

    rs = {}
    for review in reviews:

        # iterate over each topic: Price, Business Specialties, Harry Shrub
        for topic in topics.keys():
            # iterate over keywords under each topic, EX Price: cheap, expensive, price
            for keyword in topics[topic]:
                # if any of the keywords appear in current review, record it and move to next topic
                if keyword in review.lower():

                    if topic not in rs:
                        rs[topic] = 1
                    else:
                        rs[topic] += 1

                    break

    return rs

# solution 2: start with topics
def find_topic_occur_in_review_2(topics, reviews):

    rs = {}
    for topic in topics.keys():
        for review in reviews:
            for keyword in topics[topic]:
                if keyword in review.lower():
                    if topic not in rs:
                        rs[topic] = 1
                    else:
                        rs[topic] += 1

                    break

    return rs


topics = {
            "Price": ["cheap", "expensive", "price"],
            "Business specialties": ["gnome", "gnomes"],
            "Harry Shrub": ["harry shrub"]
         }

reviews = [
            "Harry Shrub did a great job with my garden, but I expected more gnomes for the price.",
            "I love my new gnomes, they are so cute! My dog loves them too! Thanks Harry!",
            "Very expensive at fifty dollars per game. Next time I'll buy from Cheap Gnomes Warehouse"
          ]

arr1 = find_topic_occur_in_review_1(topics, reviews)
print(arr1)

arr2 = find_topic_occur_in_review_2(topics, reviews)
print(arr2)
