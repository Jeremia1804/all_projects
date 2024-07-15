    create table admin(
    id serial primary key,
    email varchar(50),
    password varchar(50)
);
-- insert into admin('email','password') values('admin@gmail.com', 'admin');

        create table finition(
    idfinition serial primary key,
    libelle varchar(30),
    augmentation double precision
);

    create table typetravaux(
    idtypetravaux serial primary key,
    libelle varchar(60)
);

    create table travaux(
    idtravaux serial primary key,
    libelle varchar(100),
    unite varchar(20),
    pu double precision
);

        create table maison(
    idmaison serial primary key,
    libelle varchar(30),
    duree double precision
);

create table maisontravaux(
    idmaisontravaux serial primary key,
    idmaison int,
    idtravaux int,
    quantite double precision,
    dateheure timestamp,
    foreign key(idmaison) references maison(idmaison),
    foreign key(idtravaux) references travaux(idtravaux)
);

    create table devis(
    iddevis serial primary key,
    idmaison int,
    idfinition int,
    idclient varchar,
    debuttravaux date,
    augmentation double precision,
    duree double precision,

    foreign key(idmaison) references maison(idmaison),
    foreign key(idfinition) references finition(idfinition)
);

    create table paiement(
    idpaiement serial primary key,
    iddevis int,
    montant double precision,
    dateheure date,
    foreign key(iddevis) references devis(iddevis)
);

    create table detaildevis(
    iddetailsdevis serial primary key,
    iddevis int,
    idtravaux int,
    quantite double precision,
    pu double precision,
    foreign key(iddevis) references devis(iddevis),
    foreign key(idtravaux) references travaux(idtravaux)
);


-- Insertion dans la table finition
insert into finition (libelle, augmentation) values
('Standard', 0),
('Premium', 10),
('Gold', 20),
('VIP', 30);

-- Insertion dans la table typetravaux
insert into typetravaux (libelle) values
('Peinture'),
('Plomberie'),
('Électricité'),
('Revêtement de sol');

-- Insertion dans la table travaux
insert into travaux (libelle, unite, pu, code) values
('Peinture murale', 'm2', 25, '100'),
('Installation de robinetterie', 'unité', 50, '200'),
('Installation de prises électriques', 'unité', 30, '300'),
('Pose de parquet', 'm2', 40, '201');

-- Insertion dans la table maison (représentant les types de bâtiments à rénover)
insert into maison (libelle, duree, surface) values
('Appartement', 30, 168),
('Maison individuelle', 60, 200),
('Commerce', 90, 651),
('Bureau', 45, 34),
('Entrepot', 120, 75),
('Ecole', 75, 92);

-- Insertion dans la table maisontravaux (supposons que chaque type de bâtiment a les mêmes travaux)
insert into maisontravaux (idmaison, idtravaux, quantite) 
select idmaison, idtravaux, 1 from maison, travaux;

-- Insertion dans la table devis (idclient supposé être présent dans une autre table)
insert into devis (idmaison, idfinition, idclient, debuttravaux, augmentation, duree, datedevis) 
select idmaison, 1, 1, now(), 0.1, 60, now() from maison;

-- Insertion dans la table paiement (supposons que chaque devis a un paiement)
insert into paiement (iddevis, montant, dateheure) 
select iddevis, 5000, now() from devis;

-- Insertion dans la table detaildevis (supposons que chaque devis a tous les travaux)
insert into detaildevis (iddevis, idtravaux, quantite, pu) 
select iddevis, idtravaux, 1, pu from devis, travaux;


create view V_mtdevistrav as (
    select d.iddevis,sum(d.quantite*d.pu) as montant from detaildevis d
    group by d.iddevis
);

create or replace view V_mtdevispaye as (
    select de.iddevis,case when vu.montant is null then 0 else vu.montant end as montant from devis de
    left join
    (select d.iddevis,sum(d.montant) as montant from paiement d
    group by d.iddevis) vu on de.iddevis = vu.iddevis
);

create or replace view v_devis as (
    select vu.*,(vu.total - vu.paye) as reste from ( 
    select d.idclient,d.iddevis,m.libelle as maison, f.libelle as finition,d.lieu,d.reference,d.datedevis, (tot.montant + (tot.montant*d.augmentation/100)) as total,
    paye.montant as paye,
    d.debuttravaux as debut,
    Date(d.debuttravaux + (d.duree || ' days')::interval) AS fin
    from devis d
    join maison m on m.idmaison = d.idmaison
    join finition f on f.idfinition = d.idfinition
    join V_mtdevistrav tot on tot.iddevis = d.iddevis
    join V_mtdevispaye paye on paye.iddevis = d.iddevis
    ) vu
);

create view v_board as (
select sum(total) as total, sum(paye) as paye, sum(reste) as reste from v_devis
);


CREATE TABLE moi (
    num INT PRIMARY KEY,
    libelle VARCHAR(255)
);

INSERT INTO moi (num, libelle) VALUES 
(1, 'Janvier'),
(2, 'Février'),
(3, 'Mars'),
(4, 'Avril'),
(5, 'Mai'),
(6, 'Juin'),
(7, 'Juillet'),
(8, 'Août'),
(9, 'Septembre'),
(10, 'Octobre'),
(11, 'Novembre'),
(12, 'Décembre');

CREATE TABLE annee (
    annee INT PRIMARY KEY
);

-- Insertion des données de 2019 à 2024
INSERT INTO annee (annee) VALUES 
(2019),
(2020),
(2021),
(2022),
(2023),
(2024);

select annee.annee, moi.num from annee cross join moi;

create or replace view histogramme as (
select row_NUMBER() OVER () AS LIGNE ,vu1.*,moi.libelle,case when vu2.montant is null then 0 else vu2.montant end as montant from 
(select annee.annee, moi.num as moi from annee cross join moi) vu1
left join 
(select vu.annee,vu.moi,sum(vu.montant) as montant from (
select EXTRACT(YEAR FROM datedevis) as annee,EXTRACT(MONTH FROM datedevis) as moi, v_devis.total as montant from v_devis
) vu
group by vu.annee, vu.moi
) vu2 on vu2.annee = vu1.annee and vu2.moi = vu1.moi
join moi on moi.num = vu1.moi
);

