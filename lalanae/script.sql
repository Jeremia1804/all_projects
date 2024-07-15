create database lalana

create table types(
    idTypes serial primary key,
    nom varchar(15) 
);

create table lalana(
    idLalana serial primary key,
    nomLalana varchar(30),
    longueur double precision,
    largeur double precision,
    idTypes int,
    foreign key (idTypes) references types(idTypes)
);
insert into lalana values(default,'RN2',359,5,1);
insert into lalana values(default,'RN7',980,7,1);

create table simba(
    idSimba serial primary key,
    idLalana int,
    idpk1 int,
    idpk2 int,
    niveau double precision,
    foreign key (idLalana) references lalana(idLalana),
    foreign key (idpk1) references pk(idpk),
    foreign key (idpk2) references pk(idpk)
);

create table infra(
    idInfra serial primary key,
    intitule varchar(20)
);

create table coordonneeInfra(
    idcoordonneeInfra serial primary key,
    idInfra int,
    nom varchar(30),
    coordonnee geography(point),
    nombre int,
    foreign key (idInfra) references infra(idInfra)
);

create table cout(
    idCout serial primary key,
    prix double precision,
    duree double precision,
    daty date
);

insert into types values(default,'goudron');

insert into lalana values(default,'RN2',359,5,1);
insert into lalana values(default,'RN7',980,7,1);

create table pk(
    idPk serial primary key,
    coordonnee geography(point),
    valeur int,
    idLalana int,
    foreign key (idLalana) references lalana(idLalana)
);
insert into pk values(default,'point(-18.879470062305614 47.68748333903571)',28, 1);
insert into pk values(default, 'point(-18.924688788528606 47.815364061599055)', 51, 1);


insert into pk values(default, 'point(-18.921745582663483 47.88854545239351)', 68, 1);
insert into pk values(default, 'point(-18.946650048871643 48.257384019051)', 124, 1);


insert into pk values(default, 'point(-18.95134830389759 48.425869660654044)', 150, 1);
insert into pk values(default, 'point(-18.965016124903197 48.590643124846125)', 184, 1);


insert into pk values(default, 'point(-18.219942737407862 49.30148071293536)', 304, 1);
insert into pk values(default, 'point(-18.20367725780931 49.32285255452301)', 342, 1);



insert into simba values(default, 1, 1, 2, 70);
insert into simba values(default, 1, 3, 4, 12);
insert into simba values(default, 1, 5, 6, 53);
insert into simba values(default, 1, 7, 8, 29);


insert into infra values(default,'hopital');
insert into infra values(default,'ecole');
insert into infra values(default,'Tanana');

insert into coordonneeInfra values(default,1,'Hopital des Sacres Coeur','Point(-18.87802854822544 47.68752621326056)',0);
insert into coordonneeInfra values(default,1,'Hopital Manarapenitra','Point(-18.942712726172086 48.21792340481373)',0);
insert into coordonneeInfra values(default,1,'Hopital Miahy','Point(-18.198418168519590 49.34237903601498)',0);
insert into coordonneeInfra values(default,1,'Hopital SOA','Point(-18.965168283743917 48.590932776498406)',0);

insert into coordonneeInfra values(default,2,'Les abeilles','Point(-18.97929726688768 48.95529331882641)',0);
insert into coordonneeInfra values(default,2,'Lycee Manjakandriana','Point(-18.920202898781806 47.811405075965226)',0);
insert into coordonneeInfra values(default,2,'College prive Parc de Princes','Point(-18.924688788528619 47.815364061588991)',0);
insert into coordonneeInfra values(default,2,'Andraina','Point(-18.907664884082187 47.90780364576862)',0);
insert into coordonneeInfra values(default,2,'EPP Moramanga','Point(-18.94509744240085 48.22097039424061)',0);
insert into coordonneeInfra values(default,2,'EPP H','Point(-18.466306379272922 49.1409773255621)',0);
insert into coordonneeInfra values(default,2,'College ST Pierre','Point(-18.17415907653119 49.35400909437735)',0);

insert into coordonneeInfra values(default,3,'Tanana 1','Point(-18.878465071893764 47.688212858773824)',100);
insert into coordonneeInfra values(default,3,'Tanana 2','Point(-18.884200684286963 47.68899606379219)',50);
insert into coordonneeInfra values(default,3,'Tanana 3','Point(-18.92114676879917 47.80959190264673)',50);
insert into coordonneeInfra values(default,3,'Tanana 4','Point(-18.921562881839346 47.81071843044192)',120);
insert into coordonneeInfra values(default,3,'Tanana 5','Point(-18.920081108728837 47.81093300716481)',700);
insert into coordonneeInfra values(default,3,'Tanana 6','Point(-18.90697468745134 47.908082595508375)',20);
insert into coordonneeInfra values(default,3,'Tanana 7','Point(-18.943788389625794 48.21785903177754)',130);
insert into coordonneeInfra values(default,3,'Tanana 8','Point(-18.94297656880529 48.21692562303295)',300);
insert into coordonneeInfra values(default,3,'Tanana 9','Point(-18.951683146924076 48.4258428758319)',40);
insert into coordonneeInfra values(default,3,'Tanana 10','Point(-18.965472676521753 48.590396334691164)',80);
insert into coordonneeInfra values(default,3,'Tanana 11','Point(-18.979713234945272 48.954413554262544)',150);
insert into coordonneeInfra values(default,3,'Tanana 12','Point(-18.203891316924643 49.322906242090305)',600);
insert into coordonneeInfra values(default,3,'Tanana 13','Point(-18.20393208438625 49.32316373415778)',80);
insert into coordonneeInfra values(default,3,'Tanana 14','Point(-18.17415907653125 49.35400909437870)',85);


insert into cout values(default, 125000, 2, '2022-02-26');

create or replace view details_simba as (
select e.*,a.coordonnee2,pk2 from 
(select idsimba,simba.idlalana,niveau,st_astext(coordonnee) as coordonnee1,valeur as pk1 from simba join pk on (pk.idpk=idpk1))as e join 
(select idsimba, st_astext(coordonnee) as coordonnee2,valeur as pk2  from simba join pk on (pk.idpk=idpk2)) as a on 
e.idsimba=a.idsimba );

select co.idcoordonneeinfra from 
(select co.*,
st_distancesphere(st_astext(co.coordonnee),'POINT(-18.94266200951796 48.2170650528192)') d1,
st_distancesphere(st_astext(co.coordonnee),'POINT(-18.946650048871643 48.257384019051)') d2 
from coordonneeinfra co) co 
where co.d1<6000 and co.d2<6000 and idinfra=1;

create view priorite as
(select t1.*,t2.idcoordonneeInfra from
    (select min(st_distancesphere(st_makeline(coordonnee1,coordonnee2),st_astext(coordonnee))) as distance,idsimba
    from details_simba
    cross join coordonneeinfra
    where idinfra=1 group by idsimba) as t1
    join
    (select st_distancesphere(st_makeline(coordonnee1,coordonnee2),st_astext(coordonnee)) as distance,idsimba,idcoordonneeInfra
    from details_simba
    cross join coordonneeinfra
    where idinfra=1 group by idsimba,idcoordonneeInfra,distance) as t2
on t1.distance = t2.distance order by t1.distance)

select st_distancesphere(st_makeline(coordonnee1,coordonnee2),st_astext(coordonnee)) as distance,idsimba,idcoordonneeInfra
from details_simba
cross join coordonneeinfra
where idinfra=1 group by idsimba,idcoordonneeInfra,distance

create view priorite as
(select t1.*,t2.idcoordonneeInfra from 
    (select min(st_distancesphere(st_makeline(coordonnee1,coordonnee2),st_astext(coordonnee))) as distance,idsimba,idinfra
    from details_simba
    cross join coordonneeinfra
    group by idinfra,idsimba order by idsimba) as t1
    join
    (select st_distancesphere(st_makeline(coordonnee1,coordonnee2),st_astext(coordonnee)) as distance,idsimba,idcoordonneeInfra,idinfra
    from details_simba
    cross join coordonneeinfra
    group by idsimba,idcoordonneeInfra,distance) as t2
on t1.distance = t2.distance and t1.idinfra = t2.idinfra
where t1.idinfra!=3
order by t1.idsimba)