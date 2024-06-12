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

## Assumptions
1. Traffic going to the API are clean and trustworthy
2. Scaling the web application is not a priority for our purposes

## Strategy

### Feasibility
1. Create a docker env for the flask application with the help of co-pilot.
2. Sign up on BBG to explore the site.
3. Check if a public API is available. See what data points are available.
4. Test how to access the public API programatically

## Technology
1. Docker: For the environment to be easily portable
2. Python: To utilize data libraries and my experience
3. Flask: Micro Web Framework to avoid unnecessary bloat
