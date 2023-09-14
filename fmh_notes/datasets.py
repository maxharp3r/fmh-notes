import os
import urllib
import zipfile
from dataclasses import dataclass

import pandas as pd
import torch
from sklearn import model_selection, preprocessing


class MovieLensDataset:
    def __init__(self, users, movies, ratings):
        self.users = users
        self.movies = movies
        self.ratings = ratings

    # len(movie_dataset)
    def __len__(self):
        return len(self.users)

    # movie_dataset[1]
    def __getitem__(self, item):
        users = self.users[item]
        movies = self.movies[item]
        ratings = self.ratings[item]

        return {
            "users": torch.tensor(users, dtype=torch.long),
            "movies": torch.tensor(movies, dtype=torch.long),
            "ratings": torch.tensor(ratings, dtype=torch.long),
        }


@dataclass
class MovieLens:
    df: pd.DataFrame
    n_users: int
    n_movies: int
    train_dataset: MovieLensDataset
    val_dataset: MovieLensDataset


class MovieLensBuilder:
    URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

    def __init__(self, datadir):
        self.datadir = datadir

    def download(self):
        if os.path.isdir(self.path()):
            print("MovieLens already downloaded")
            return self

        zip_path, _ = urllib.request.urlretrieve(self.URL)
        with zipfile.ZipFile(zip_path, "r") as f:
            f.extractall(self.datadir)
        return self

    def build(self) -> MovieLens:
        fn = os.path.join(self.path(), "ratings.csv")
        df = pd.read_csv(fn)

        lbl_user = preprocessing.LabelEncoder()
        df.userId = lbl_user.fit_transform(df.userId.values)
        lbl_movie = preprocessing.LabelEncoder()
        df.movieId = lbl_movie.fit_transform(df.movieId.values)

        n_users = len(lbl_user.classes_)
        n_movies = len(lbl_movie.classes_)

        df_train, df_valid = model_selection.train_test_split(
            df, test_size=0.1, random_state=42, stratify=df.rating.values
        )

        train_dataset = MovieLensDataset(
            users=df_train.userId.values,
            movies=df_train.movieId.values,
            ratings=df_train.rating.values,
        )

        valid_dataset = MovieLensDataset(
            users=df_valid.userId.values,
            movies=df_valid.movieId.values,
            ratings=df_valid.rating.values,
        )

        return MovieLens(
            df=df,
            n_users=n_users,
            n_movies=n_movies,
            train_dataset=train_dataset,
            val_dataset=valid_dataset,
        )

    def path(self):
        return os.path.join(self.datadir, "ml-latest-small")
