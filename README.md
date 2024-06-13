# similar-board-games-api
Web App that tells you how similar users are based on their taste in board games

# Set Up
1. Clone repository
2. `docker-compose up -d`
3. The REST API will be available at port 8081: http://localhost:8081

## Endpoints

**GET** /users/similarity_score?username1=*username1*&username2=*username2*
```bash
curl -X GET 'http://localhost:8081/users/similarity_score?username1=user1&username2=user2'
{
  "similarity_score": {
    "score": 0,
    "username1": "user1",
    "username2": "user2"
  }
}
```

**GET** /user/*username*/similar_geeks
```bash
curl -X GET 'http://localhost:8081/user/user1/similar_geeks'
{
  "similar_geeks": [],
  "user": {
    "username": "user1"
  }
}
```

## Example
```bash
curl -X GET 'http://localhost:8081/users/similarity_score?username1=nmcalabroso&username2=nmcalabroso'
{
  "similarity_score": {
    "rating": "high",
    "score": 100.0,
    "username1": "nmcalabroso",
    "username2": "nmcalabroso"
  }
}
```

## Assumptions
1. Traffic going to the API are clean and trustworthy
2. Scaling the web application is not a priority for our purposes
3. Currently only happy path is being considered. Non-existing users and empty collections are not being handled.

## Strategy

### Feasibility
1. Create a docker env for the flask application with the help of co-pilot.
2. Sign up on BBG to explore the site.
3. Check if a public API is available. See what data points are available.
4. Test how to access the public API programatically
5. Once familiarize with the data, think about the similarity model that we will be using.

## Technology
1. Docker: For the environment to be easily portable
2. Python: To utilize data libraries and my experience
3. Flask: Micro Web Framework to avoid unnecessary bloat
4. PostgreSQL: Database

## Struggles
1. Spent most of the time familiarizing myself with the data format of the BGG
2. XML is not that easy to work with but was a nice experience (O.o)
3. Kind of treated this as a hackathon overnighter and wasn't able to allocate time accordingly for it. My bad on that front.

## Future Work / Compromises
1. Ran out of time to implement saving user and collections to the local database when fetching from the XML API to avoid repetitive things
2. Tests will also be deprioritized instead of having a full TDD approach in the interest of time
3. (Putting it here just in case I don't finish) My strategy on getting a similarity score between 2 collections is to get all owned boardgames of each user and plot the category these games belong to. I would then create a dataframe for it and use some similarity algorithm (either euclidian or something else but honestly no definite idea at this point)
4. Haven't done the bonus points. But probably it would require to get the whole user database of BGG to do this. Or maybe just the ones with common games for a user. Although if done correctly, I would assume the similarity score should be computed from the background instead of on the fly.
5. I would love to have a proper python objects to work with to make the code easier to manage but I guess it's for future work. For now, I'll be contented with raw data manipulation.
6. Maybe a better study of similarity score strategy would be nice as I don't have good experience on this front. I initially thought that this will be clustering problem but apparently not.