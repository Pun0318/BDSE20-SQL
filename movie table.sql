create table moviedata(
movie_id int(20) Primary key not null, 
movie_title varchar(150) null,
belongs_to_collection bool,
movie_popularity int(20) null,
movie_releasedate date null,
movie_runtime int(20) null,
movie_budget int(20) null,
movie_revenue int(20) null,
movie_imdb_id char(50) null

);