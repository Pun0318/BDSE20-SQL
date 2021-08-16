create table genres(
movie_id int ,
genre varchar(255) null,
FOREIGN KEY (movie_id) REFERENCES moviedata(movie_id)
);
