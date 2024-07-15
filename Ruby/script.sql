create table lalana(
    id serial primary key,
    p int,
    v int,
    d int
);

create table formule(
    id serial primary key,
    fo varchar(20)
);

insert into lalana values(default,2,6,8);
insert into lalana values(default,3,4,5);

insert into formule values(default,'4*p + 8*v + 2*d');

je voulais faire une requete comme celle ci-dessous mais ca ne marchar pas
select (select fo from formule where id=1) from lalana;

pouvez vous me donner la bonne