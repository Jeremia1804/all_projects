create table objet(
    idObjet serial primary key,
    nomObjet varchar(40)
);


create table imageanalyse(
    idImageanalyse serial primary key,
    pathimage varchar(100),
    idObjet int,
    foreign key (idObjet) references objet(idObjet)
);


create table Info(
    idInfo serial primary key,
    imageProfil varchar(100),
    titre varchar(50),
    texte text,
    idObjet int,
    foreign key (idObjet) references objet(idObjet)
);

create table objetDeleted(
    id serial primary key,
    idObjet int,
    foreign key (idObjet) references objet(idObjet)
);

create table utilisateur(
    idUser serial primary key,
    nomuser varchar(20),
    email varchar(50),
    cle varchar(10),
    isConnect int default 0
);

insert into utilisateur values(default,'Jeremia','hasina20.jeremia@gmail.com','2020s2121g');
insert into utilisateur values(default,'Sergio','sergio@gmail.com','1234a567f');



create table administrateur(
    id serial primary key,
    email varchar(50),
    motdepasse varchar(10)
);

create view v_objet as (select * from objet ob where ob.idobjet not in (select idobjet from objetdeleted));

insert into objet values (default,'OeuvreJaune');
insert into objet values (default,'OeuvreCouleur');

insert into info values(default,'/home/jeremia/BAOVOLA/SARY_AMPIANARINA/image_profil/OeuvreJaune_original2.jpg','Majesté Africaine','Dans cette œuvre captivante, une femme africaine est représentée de profil, vue de droite. Son visage n''est pas peint, créant ainsi une dimension intrigante et énigmatique. Un imposant collier, composé de perles et de matériaux précieux, témoignant de l''opulence et du statut de ces femmes influentes. Chaque détail de ce collier est soigneusement travaillé pour refléter l''art et l''artisanat traditionnels.
\nC''est une œuvre qui rend hommage aux femmes africaines anciennes, à leur rôle essentiel dans l''économie et à leur contribution à la société. Elle transporte le spectateur dans le passé, captivant par son authenticité et sa représentation émouvante de l''histoire africaine.',1);
insert into info values(default,'/home/jeremia/BAOVOLA/SARY_AMPIANARINA/image_profil/OeuvreBeCouleur_original1.jpg','L''Emblematique femme aux motifs','Échos de l''Âme est une toile envoûtante où une femme africaine, représentée avec une palette de couleurs éclatantes, se trouve plongée dans ses pensées. Son visage sans expression est mis en valeur par un fond coloré qui dépeint l''énergie et la vivacité de ses réflexions profondes. Les nuances chatoyantes du fond créent une atmosphère dynamique qui contraste avec son visage serein, donnant ainsi une impression de force intérieure et de contemplation profonde. Son regard perçant, dirigé légèrement vers la gauche, se fond harmonieusement avec les teintes vibrantes qui l''entourent, créant ainsi une composition visuellement stimulante et introspective.',2);

-- update info set imageProfil='/home/jeremia/BAOVOLA/SARY_AMPIANARINA/imageanalyse/OeuvreJaune_original2.png' where idobjet = 1;
-- update info set imageProfil='/home/jeremia/BAOVOLA/SARY_AMPIANARINA/sary_baovola/OeuvreBeCouleur_original1.png' where idobjet = 2; 

-- insert into subtitle values (default,'Histoire','Blablablablablablablablablablabla blablablablablablabla blablablablablablablabla blablablablabla',1);
-- insert into subtitle values (default,'Idee','Bloblobloblobloblboblobloblo bloblbobloblobloblobloblo blobloblobloblobloblobloblo bloblobloblobloblobloblobloblobl',1);
-- insert into subtitle values (default,'Formule','Blebleblebleblebleblebleblebl ebleblebleblebleblebleblebleble bleblebleblebleblebleblel bleblebleblebleblebleble',2);
-- insert into subtitle values (default,'Cours','Blublublublublublublublu blublublublubl blublublublublu ublublublublublu blublublublublublublublu blublublublu',2);

insert into imageanalyse values(default,'/home/jeremia/BAOVOLA/SARY_AMPIANARINA/imageanalyse/1/OeuvreJaune_original2.png',1);
insert into imageanalyse values(default,'/home/jeremia/BAOVOLA/SARY_AMPIANARINA/imageanalyse/2/OeuvreBeCouleur_original1.png',2);

drop table imageanalyse;
drop table info;
drop table subtitle;
drop table objetdeleted;
drop table objet;

alter table utilisateur
add column isConnect int default 0;