class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.pairs = defaultdict(SortedList)
        self.food = {}  
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.pairs[cuisine].add((-rating, food))
            self.food[food] = (cuisine, rating)
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, old_rating = self.food[food]
        self.food[food] = (cuisine, newRating)
        self.pairs[cuisine].discard((-old_rating, food))
        self.pairs[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.pairs[cuisine][0][1]        
