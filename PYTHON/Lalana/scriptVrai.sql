create or replace view details_simba as (
select e.*,a.coordonnee2,pk2 from 
(select idsimba,simba.idlalana,niveau,st_astext(coordonnee) as coordonnee1,valeur as pk1 from simba join pk on (pk.idpk=idpk1))as e join 
(select idsimba, st_astext(coordonnee) as coordonnee2,valeur as pk2  from simba join pk on (pk.idpk=idpk2)) as a on 
e.idsimba=a.idsimba ); 


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

insert into lalana values(default,'RN2',359,5,1);
insert into lalana values(default,'RN7',359,5,1);

//Simba1
insert into pk values(default, 'point(48.0467218 -18.8768764)', 342, 1);
insert into pk values(default, 'point(48.0519575 -18.8725314)', 342, 1);

//simba2
insert into pk values(default, 'point(47.9894283 -18.8873931)', 342, 1);
insert into pk values(default, 'point(47.9991486 -18.8915144)', 342, 1);

//simba3
insert into pk values(default, 'point(48.1629958 -18.9085121)', 342, 1);
insert into pk values(default, 'point(48.1721582 -18.9155357)', 342, 1);

insert into coordonneeInfra values(default,2,'Sekoly 1','Point(47.9995262 -18.8921933)',0);
insert into coordonneeInfra values(default,2,'Sekoly 2','Point(47.989484 -18.8878385)',0);
insert into coordonneeInfra values(default,2,'Sekoly 3','Point(48.1631291 -18.9107643)',0);
insert into coordonneeInfra values(default,2,'Sekoly 4','Point(47.0606723 -19.9156356)',0);
insert into coordonneeInfra values(default,2,'Sekoly 5','Point(47.0605435 -19.9255611)',0);
insert into coordonneeInfra values(default,2,'Sekoly 6','Point(47.0789636 -20.0647593)',0);
insert into coordonneeInfra values(default,2,'Sekoly 7','Point(47.081796 -20.0755622)',0);
insert into coordonneeInfra values(default,2,'Sekoly 8','Point(47.0966332 -19.7966552)',0);
insert into coordonneeInfra values(default,2,'Sekoly 9','Point(47.1104734 -19.7966148)',0);



insert into infra values(default,'hopital');
insert into infra values(default,'ecole');
insert into infra values(default,'population');

insert into simba values(default, 1, 1, 2, 70);


insert into cout values(default, 125000, 2, '2022-02-26');




insert into types values(default,'goudron');

insert into lalana values(default,'RN2',359,5,1);
insert into lalana values(default,'RN7',1000,5,1);

-- rn2
insert into pk values(default,'point(48.0467218 -18.8768764)',28, 1);
insert into pk values(default,'point(48.0519575	-18.8725314)',51, 1);

insert into pk values(default,'point(47.9894283	-18.8873931)',100, 1);
insert into pk values(default,'point(47.9991486	-18.8915144)',134, 1);

insert into pk values(default,'point(48.1629958	-18.9085121)',200, 1);
insert into pk values(default,'point(48.1721582	-18.9155357)',299, 1);

-- rn7
insert into pk values(default,'point(47.0975661	-19.7917772)',50, 2);
insert into pk values(default,'point(47.0953075 -19.7959843)',128, 2);

insert into pk values(default,'point(47.0587143 -20.0669718)',350, 2);
insert into pk values(default,'point(47.0626196 -20.0775529)',420, 2);

insert into pk values(default,'point(47.0450248 -19.9137168)',863, 2);
insert into pk values(default,'point(47.0451168 -19.9268152)',900, 2);



insert into simba values(default, 1, 1, 2, 29);
insert into simba values(default, 1, 3, 4, 65);
insert into simba values(default, 1, 5, 6, 10);

insert into simba values(default, 2, 7, 8, 19);
insert into simba values(default, 2, 9, 10, 54);
insert into simba values(default, 2, 11, 12, 12);