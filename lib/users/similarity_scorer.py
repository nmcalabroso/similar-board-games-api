from flask import current_app
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

from lib.bgg.api import BoardGameGeekAPI

class SimilarityScorer:
    def __init__(self):
        pass

    def calculate_similarity(self, username1, username2):
        bgg_api = BoardGameGeekAPI()

        user1 = bgg_api.get_user(username1)
        user1_collection = bgg_api.get_collection(username1)
        user1 = {
            'user': user1,
            'collection': user1_collection
        }

        user2 = bgg_api.get_user(username2)
        user2_collection = bgg_api.get_collection(username2)
        user2 = {
            'user': user2,
            'collection': user2_collection
        }

        df = self._initialize_df(user1, user2)
        current_app.logger.info(f'DataFrame: {df}')

        cosine_similarity_matrix = cosine_similarity(df)
        current_app.logger.info(f'Cosine similarity matrix: {cosine_similarity_matrix}')

        # The cosine similarity between the two users is the off-diagonal element
        similarity_score = cosine_similarity_matrix[0][1]
        # Convert the similarity score from the range -1 to 1 to the range 0 to 100
        similarity_score = (similarity_score + 1) * 50
        return similarity_score
    
    #    g1 g2 g3 ... c1 c2 c3 ...
    # u1 r            0  
    # u2 0
    def _initialize_df(self, user1, user2):
        column_names = self._column_names(user1['collection'], user2['collection'])
        current_app.logger.info(f'Column names: {column_names}')
        row1 = self._row(user1['collection'], column_names)
        current_app.logger.info(f'Row 1: {row1}')
        row2 = self._row(user2['collection'], column_names)
        current_app.logger.info(f'Row 2: {row2}')

        return pd.DataFrame([row1, row2], columns=column_names, index=[user1['user']['username'], user2['user']['username']])

    def _row(self, collection, column_names):
        row = [0] * len(column_names)
        for item in collection:
            row[column_names.index(item['name'].lower())] = item['user_rating']
            for rank in item['ranks']:
                row[column_names.index(rank['@name'].lower())] = rank['@value']
        return row

    def _column_names(self, collection1, collection2):
        combined_collections = collection1 + collection2
        combined_games = [c['name'].lower() for c in combined_collections]
        combined_categories = [[r['@name'].lower() for r in c['ranks']] for c in combined_collections]
        combined_categories = [item for sublist in combined_categories for item in sublist]
        return list(set(combined_games + combined_categories))