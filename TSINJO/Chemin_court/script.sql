create table ip(
    id serial primary key,
    valeur varchar(30)
);

create table site(
    id serial primary key,
    nom varchar(30),
    url varchar(100)
);

create table ipSite(
    id serial primary key,
    idIP int,
    idSite int,
    foreign key (idIp) references ip(id),
    foreign key (idSite) references site(id)
);

create table lienIp(
    id serial primary key,
    idIP1 int,
    idIP2 int,
    poids double precision,
    foreign key (idIP1) references site(id),
    foreign key (idIP2) references site(id)
);

insert into ip values(default, '192.28.197');
insert into ip values(default, '192.056.91');
insert into ip values(default, '192.168.27');
insert into ip values(default, '192.55.102');
insert into ip values(default, '192.234.11');

insert into site values(default, 'youtube', 'youtube.com');
insert into site values(default, 'facebook', 'facebook.com');
insert into site values(default, 'pinterest', 'pinterest.fr');
insert into site values(default, 'instagram', 'instagram.com');
insert into site values(default, 'twitter', 'twitter.com');

insert into ipSite values(default,1,1);
insert into ipSite values(default,2,2);
insert into ipSite values(default,2,3);
insert into ipSite values(default,4,4);
insert into ipSite values(default,5,5);
insert into ipSite values(default,1,4);
insert into ipSite values(default,2,5);
insert into ipSite values(default,3,3);
insert into ipSite values(default,3,2);
insert into ipSite values(default,4,1);
insert into ipSite values(default,4,2);
insert into ipSite values(default,4,3);
insert into ipSite values(default,5,3);
insert into ipSite values(default,5,4);
insert into ipSite values(default,5,1);

insert into lienIp values(default, 1,2, 0.2);
insert into lienIp values(default, 1,3, 1.5);
insert into lienIp values(default, 2,3, 0.5);
insert into lienIp values(default, 2,4, 0.8);
insert into lienIp values(default, 3,4, 1);
insert into lienIp values(default, 3,5, 2);
insert into lienIp values(default, 4,5, 1);
insert into lienIp values(default, 4,5, 1);
insert into lienIp values(default, 5,1, 0.9);


create or replace view v_lien as (
    select v.id,idip1,idip2,valeur1,valeur as valeur2, poids from 
    (select lp.id as id,lp.idip1,idip2,valeur as valeur1,poids from lienIp as lp join ip on lp.idip1=ip.id) as v
    join ip on v.idip2=ip.id
);

create or replace view v_site as (
    select i.id,idip,idsite,nom,url from 
    ipsite as i 
    join site as s 
    on i.idsite=s.id
);