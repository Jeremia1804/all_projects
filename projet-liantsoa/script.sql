create table genre(
    idGenre int primary key,
    libelle varchar(30)
);

create table personnes(
    idPersonnes int primary key,
    nom varchar(30),
    idgenre int,
    foreign key idgenre references idgenre(genre)
)

create table import(
    NumSeance varchar(10),
    Film varchar(50),
    Categorie varchar(50),	
    Salle varchar(20),
    Date varchar(50),
    Heure varchar(50)
);

create table categorie(
    idCategorie serial primary key,
    libelle varchar(20)
);

create table film(
    idFilm serial primary key,
    titre varchar(50),
    auteur varchar(20),
    duree double precision,
    idcategorie int,
    foreign key (idcategorie) references categorie(idcategorie)
);

create table salle(
    idSalle serial primary key,
    numero varchar(10)
);

create table seance (
    idseance serial primary key,
    idfilm int,
    idsalle int,
    dateheure timestamp,
    foreign key (idfilm) references film(idfilm),    
    foreign key (idsalle) references salle(idsalle)
);



-- j/


CREATE TABLE table1 (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255)
);
CREATE TABLE table2 (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255)
);
CREATE TABLE association (
    id SERIAL PRIMARY KEY,
    table1_id INT,
    table2_id INT,
    FOREIGN KEY (table1_id) REFERENCES table1(id),
    FOREIGN KEY (table2_id) REFERENCES table2(id)
);

INSERT INTO table1 (nom) VALUES 
('Donnée1'),
('Donnée2'),
('Donnée3'),
('Donnée4');

INSERT INTO table2 (nom) VALUES 
('DonnéeA'),
('DonnéeB'),
('DonnéeC'),
('DonnéeD');

create table importation(
    id serial primary key,
    nom1 varchar(30),
    nom2 varchar(30)
);

INSERT INTO importation (nom1,nom2) VALUES 
('Donnée1','DonnéeA'),
('Donnée2','DonnéeB'),
('Donnée3','DonnéeC'),
('Donnée4','DonnéeD');

create view ass as (
select t1.id as id1,t2.id as id2 from importation as im
join table1 as t1 on im.nom1 = t1.nom
join table2 as t2 on im.nom2 = t2.nom
);

insert into association (table1_id, table2_id) select * from ass;