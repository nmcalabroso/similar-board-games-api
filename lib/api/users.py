from flask import Blueprint, request, current_app
from lib.users.similarity_scorer import SimilarityScorer

users = Blueprint('users', __name__)


@users.route('/similarity_score', methods=['GET'])
def similarity_score():
    current_app.logger.info('Processing similarity_score request...')
    username1 = request.args.get('username1')
    username2 = request.args.get('username2')

    similarity_score = SimilarityScorer().calculate_similarity(username1, username2)
    return {
        'similarity_score': {
            'username1': username1,
            'username2': username2,
            'score': similarity_score,
            'rating': 'high' if similarity_score > 80 else 'low'
        }
    }

user = Blueprint('user', __name__)
@user.route('/<username>/similar_geeks', methods=['GET'])
def similar_geeks(username):
    current_app.logger.info('Processing similar_geeks request')
    # Find similar geeks based on liked board games
    similar_geeks = []
    return {
        'user': {'username': username},
        'similar_geeks': similar_geeks
    }
