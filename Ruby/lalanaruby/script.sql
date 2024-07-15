create database lalana

create table types(
    idTypes serial primary key,
    nom varchar(15) 
);
insert into types values(default,'goudron');

create table lalana(
    idLalana serial primary key,
    nomLalana varchar(30),
    longueur double precision,
    largeur double precision,
    idTypes int,
    formule varchar(80),
    foreign key (idTypes) references types(idTypes)
);

insert into lalana values(default,'RN2',359,5,1,' ');
insert into lalana values(default,'RN7',980,7,1,' ');
update lalana set nomlalana='RN1',largeur='6' where idlalana=1;
update lalana set nomlalana='RN2',largeur='8' where idlalana=2;
insert into lalana values(default,'RN4',980,7,1,'4*v + 9*a');
create table simba(
    idSimba serial primary key,
    idLalana int,
    pk1 int,
    pk2 int,
    niveau double precision,
    foreign key (idLalana) references lalana(idLalana)
);
insert into simba values(default,1,18,41,65);
insert into simba values(default,1,70,99,12);
insert into simba values(default,1,175,231,34);
insert into simba values(default,1,297,320,50);

insert into simba values(default,2,45,82,20);
insert into simba values(default,2,199,267,81);
insert into simba values(default,2,534,600,42);

create table prestataire(
    idprestataire serial primary key,
    nom varchar(30),    
    prix double precision,      --ar
    datecreation date,          
    vitesse double precision,   --m3/jour
    penalite double precision   --ar
);

insert into prestataire values(default,'presta 1',130000,'2015-04-15',4,2);
insert into prestataire values(default,'presta 2',120000,'2006-01-05',5,1);
insert into prestataire values(default,'presta 3',100000,'2010-02-02',6,2);
update prestataire set vitesse=6 where idprestataire=8;
-- insert into prestataire values(default,'prestataire 4',5000,'2022-10-24',5,1000000);
-- insert into prestataire values(default,'prestataire 5',4000,'2019-10-24',12,300000,56);

create or replace view prestataires as
(
    select 
    idprestataire,
    nom,
    prix,
    extract(year from age(now(),datecreation)) as a,
    vitesse as v,
    penalite as p,
    nbemploi as nb
    from prestataire
);

alter view prestataires
rename column annee a;

create or replace function eval(idL int, idP int)
returns double precision
language plpgsql
AS $$ 
declare
    rep double precision;
    equation varchar(20);
BEGIN
    equation:=(select f.fo from lalana l join formules f on l.idlalana=f.idlalana where l.idlalana=idL);
    execute 'SELECT ' || equation || ' from prestataires where idprestataire='||idP into rep;
    return rep;
END;
$$;

create or replace view rapport as
(select *,(qualite/prix) as rapport from
(select *,eval(idL,idP) as qualite from 
(select p.idprestataire as idP,p.nom ,l.idLalana as idL,l.nomLalana,p.prix,p.v from prestataires p
cross join
lalana l) as alias) as lk);

create table formule(
    idFormule serial primary key,
    idLalana int,
    fo varchar(70),
    daty timestamp,
    foreign key (idLalana) references lalana(idLalana)
);

insert into formule values(default,1,'4*vitesse + 5*annee',now());
insert into formule values(default,1,'6*vitesse + 3*annee',now());
insert into formule values(default,2,'2*vitesse + 5*annee',now());
insert into formule values(default,2,'3*vitesse + 8*annee',now());

insert into formule values(default,1,'(4*v + 3*a - 4*p)*1000',now());
insert into formule values(default,2,'(2*v + 2*a - 2*p)*1000',now());
insert into formule values(default,3,'(1*v + 1*a - 1*p)*1000',now());

select max(daty) as da,idlalana from formule group by idlalana
create or replace view formules as (select formule.* from formule join (select max(daty) as da,idlalana from formule group by idlalana) as i on formule.idlalana = i.idlalana and formule.daty=i.da)
select * from lalana join (select max(daty) as da,idlalana from formule group by idlalana) as i on lalana.idlalana=i.idlalana;






