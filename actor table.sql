create table actor(
movie_id int,
actor_id int ,
actor_name char(150),
actor_gender int(20),
actor_character char(150),
popularity int(20),
FOREIGN KEY (movie_id) REFERENCES moviedata(movie_id)
);