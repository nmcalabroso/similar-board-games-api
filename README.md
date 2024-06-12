# similar-board-games-api
Web App that tells you how similar users are based on their taste in board games

# Set Up
1. Clone repository
2. `docker-compose up -d`
3. The app will be available at port 8081

## Endpoints

GET /users/similarity_score?username1=<username1>&username2=<username2>

GET /user/<username>/similar_geeks

## Assumptions
1.

## Strategy
1. Create a flask application with the help of co-pilot
2. Sign up on BBG to explore the site
3. Check if a public API is available. See what data points are available.
4. Test how to access the public API programatically