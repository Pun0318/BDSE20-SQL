create table crew (
crew_id int(20) ,
movie_id  int(20),
crew_name varchar(150) null,
known_for_department varchar(150) null,
department varchar(150) null,
job varchar(150) null,
FOREIGN KEY (movie_id) REFERENCES moviedata(movie_id)
);