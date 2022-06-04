class Event(object):
    def __init__(self, event_type, occurrence, biz_id):
        self.event_type = event_type
        self.occurrence = occurrence
        self.biz_id = biz_id

def get_active_business(events):

    if not events or len(events) == 0:
        return []

    # event_type: photo_views, ads, page_views, reviews
    # compute the average value for each event_type and count the unique biz_ids
    ids = set()
    ph_view = ph_events = ads = ads_events = pg_view = pg_events = review = rv_events = 0
    for i in range(0, len(events)):

        ids.add(events[i].biz_id)
        if events[i].event_type == "photo_views":
            ph_view += events[i].occurrence
            ph_events += 1

        if events[i].event_type == "ads":
            ads += events[i].occurrence
            ads_events += 1

        if events[i].event_type == "page_views":
            pg_view += events[i].occurrence
            pg_events += 1

        if events[i].event_type == "reviews":
            review += events[i].occurrence
            rv_events += 1

    # find out the active business by ids.
    active = []
    for i in range(0, len(ids)):
        id = ids.pop()

        # determine whether or not the a given id is active
        aver_across = 0
        for j in range(0, len(events)):

            if events[j].biz_id == id:

                if events[j].event_type == "photo_view" and \
                        events[j].occurrence >= (ph_view/ph_events):
                    aver_across += 1

                if events[j].event_type == "ads" and\
                        events[j].occurrence >= (ads/ads_events):
                    aver_across += 1

                if events[j].event_type == "page_views" and \
                        events[j].occurrence >= (pg_view/pg_events):
                    aver_across += 1

                if events[j].event_type == "reviews" and\
                        events[j].occurrence >= (review/rv_events):
                    aver_across += 1

        if aver_across >= 2:
            active.append(id)

    # sort the active biz_id in ascending order
    active.sort()
    return active


event1 = Event("ads", 7, 3)
event2 = Event("ads", 8, 2)
event3 = Event("ads", 5, 1)
event4 = Event("page_views", 11, 2)
event5 = Event("page_views", 12, 3)
event6 = Event("photo_views", 10, 3)
event7 = Event("reviews", 7, 2)

events = [event1, event2, event3, event4, event5, event6, event7]
arr = get_active_business(events)
print(arr)