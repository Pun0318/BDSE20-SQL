create table productioncompany (
pc_id int(20) , 
movie_id int(20),
movie_title varchar(150) null,
pc_name varchar(150) null,
pc_country varchar(150) null,
FOREIGN KEY (movie_id) REFERENCES moviedata(movie_id)
);