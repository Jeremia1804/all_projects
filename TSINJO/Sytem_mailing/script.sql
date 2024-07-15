create database mailing;

\c mailing;

create table utilisateur(
    idUtilisateur serial primary key,
    nom varchar(20),
    compte varchar(50),
    mdp varchar(10)
);

create table mail(
    idMail serial primary key,
    objet varchar(100),
    texte text
);

create table response(
    idResponse serial primary key,
    idMail int,
    idMailmere int,
    foreign key (idMail) references mail(idMail),
    foreign key (idMailmere) references mail(idMail)
);

create table envoimessage(
    idEnvoiMessage serial primary key,
    idDestinateur int,
    idDestinataire int,
    idMail int,
    date_envoi timestamp,
    foreign key (idMail) references mail(idMail),
    foreign key (idDestinateur) references utilisateur(idUtilisateur),
    foreign key (idDestinataire) references utilisateur(idUtilisateur)
);

create table isSpam(
    idIsSpam serial primary key,
    idMail int,
    valeur VARCHAR(3) CHECK (valeur IN ('yes', 'no')),
    daty timestamp default now(),
    foreign key (idMail) references mail(idMail)
);

create table isRead(
    idIsRead serial primary key,
    idMail int,
    valeur int CHECK (valeur IN (1, 0)),
    daty timestamp default now(),
    foreign key (idMail) references mail(idMail)
);


insert into utilisateur values(default,'Jeremia','hasina20.jeremia@gmail.com','jeremia20');
insert into utilisateur values(default,'Liantsoa','randraina@yahoo.com','liantsoa06');
insert into utilisateur values(default,'Sergio','sergio@gmail.com','sergio18');


-- Insérer des données de spam dans la table "mail" avec des doubles apostrophes pour les apostrophes
INSERT INTO mail (objet, texte)
VALUES
    ('donnee de chatGPT', 'Gagnez 1000€ par jour en travaillant de chez vous !'),
    ('donnee de chatGPT', 'Augmentez votre taille avec notre produit révolutionnaire.'),
    ('donnee de chatGPT', 'Prêt personnel approuvé instantanément, même avec un mauvais crédit.'),
    ('donnee de chatGPT', 'Perdez du poids rapidement avec nos pilules miracles.'),
    ('donnee de chatGPT', 'Votre colis est en attente de livraison, veuillez cliquer pour confirmer.'),
    ('donnee de chatGPT', 'Vous avez gagné un iPhone X ! Réclamez-le maintenant.'),
    ('donnee de chatGPT', 'Réductions incroyables sur les montres de luxe - vente exclusive.'),
    ('donnee de chatGPT', 'Découvrez comment doubler vos revenus en une semaine.'),
    ('donnee de chatGPT', 'Vous avez été sélectionné pour une croisière gratuite aux Bahamas.'),
    ('donnee de chatGPT', 'Offre spéciale : Viagra à prix réduit sans ordonnance.'),
    ('donnee de chatGPT', 'Gagnez un voyage tous frais payés à Disneyland.'),
    ('donnee de chatGPT', 'Réclamez votre prix de loterie de 10 millions de dollars.'),
    ('donnee de chatGPT', 'Obtenez un diplôme universitaire en un temps record.'),
    ('donnee de chatGPT', 'Votre compte bancaire nécessite une mise à jour urgente.'),
    ('donnee de chatGPT', 'Multipliez vos followers sur les réseaux sociaux avec notre service.'),
    ('donnee de chatGPT', 'Faites fortune en investissant dans cette opportunité unique.'),
    ('donnee de chatGPT', 'Des prêts rapides et faciles sans vérification de crédit.'),
    ('donnee de chatGPT', 'Perdez du ventre en utilisant cette méthode secrète.'),
    ('donnee de chatGPT', 'Argent gratuit ! Cliquez ici pour le réclamer.'),
    ('donnee de chatGPT', 'Augmentez vos revenus en travaillant depuis votre canapé.'),
    ('donnee de chatGPT', 'Enrichissez-vous grâce à notre système automatisé.'),
    ('donnee de chatGPT', 'Vous avez été choisi pour une carte-cadeau Amazon de 100€.'),
    ('donnee de chatGPT', 'Boostez votre site web avec des milliers de visiteurs ciblés.'),
    ('donnee de chatGPT', 'Découvrez le secret des célébrités pour rester jeunes.'),
    ('donnee de chatGPT', 'Achetez des abonnés Instagram et devenez une star instantanée.'),
    ('donnee de chatGPT', 'Un membre de votre famille vous a envoyé un e-mail vocal.'),
    ('donnee de chatGPT', 'Préparez-vous à gagner à la loterie avec nos numéros chanceux.'),
    ('donnee de chatGPT', 'Réclamez votre argent perdu grâce à notre programme de récupération.'),
    ('donnee de chatGPT', 'Découvrez comment obtenir un prêt sans intérêt.'),
    ('donnee de chatGPT', 'Obtenez un iPhone dernier cri pour seulement 1€.'),
    ('donnee de chatGPT', 'Nous avons trouvé votre âme sœur - Inscrivez-vous maintenant !'),
    ('donnee de chatGPT', 'Augmentez votre score de crédit rapidement et facilement.'),
    ('donnee de chatGPT', 'Gagnez de l''argent en lisant des e-mails !'),
    ('donnee de chatGPT', 'Encaissez des chèques à domicile en quelques heures par jour.'),
    ('donnee de chatGPT', 'Obtenez un devis gratuit pour une assurance maladie avantageuse.'),
    ('donnee de chatGPT', 'Gagnez des milliers de dollars en répondant à des sondages en ligne.'),
    ('donnee de chatGPT', 'Vous avez été sélectionné pour tester le nouvel iPhone avant sa sortie.'),
    ('donnee de chatGPT', 'Économisez 90% sur vos achats en ligne grâce à nos offres spéciales.'),
    ('donnee de chatGPT', 'Devenez millionnaire grâce à notre programme d''investissement.'),
    ('donnee de chatGPT', 'Votre héritage vous attend - envoyez-nous vos coordonnées.'),
    ('donnee de chatGPT', 'Recevez gratuitement des échantillons de produits de marque.'),
    ('donnee de chatGPT', 'Augmentez la taille de votre poitrine avec nos pilules magiques.'),
    ('donnee de chatGPT', 'Découvrez comment gagner aux machines à sous en ligne.'),
    ('donnee de chatGPT', 'Réclamez votre voiture de luxe gratuite aujourd''hui !'),
    ('donnee de chatGPT', 'Vous avez gagné un bon d''achat de 500€ - Confirmez votre adresse.'),
    ('donnee de chatGPT', 'Encaissez des chèques et gardez une partie de l''argent pour vous.'),
    ('donnee de chatGPT', 'Ne payez plus jamais vos factures - découvrez notre astuce.'),
    ('donnee de chatGPT', 'Obtenez un financement garanti pour votre entreprise.'),
    ('donnee de chatGPT', 'Réductions exclusives sur les voyages et les séjours à l''hôtel.'),
    ('donnee de chatGPT', 'Encaissez des paiements en ligne avec notre plateforme facile à utiliser.');

-- Insérer des données de spam dans la table "mail" avec des doubles apostrophes pour les apostrophes
INSERT INTO mail (objet, texte)
VALUES
    ('donnee de chatGPT', 'Confirmation de votre inscription à notre bulletin d''information.'),
    ('donnee de chatGPT', 'Récapitulatif de votre commande sur notre site web.'),
    ('donnee de chatGPT', 'Votre facture pour le mois de juillet est disponible.'),
    ('donnee de chatGPT', 'Avis de livraison : Votre colis a été expédié.'),
    ('donnee de chatGPT', 'Invitation à participer à notre enquête de satisfaction client.'),
    ('donnee de chatGPT', 'Mise à jour de nos politiques de confidentialité.'),
    ('donnee de chatGPT', 'Notification de changement de mot de passe pour votre compte.'),
    ('donnee de chatGPT', 'Votre réservation de billets d''avion est confirmée.'),
    ('donnee de chatGPT', 'Avis de remboursement suite à un achat annulé.'),
    ('donnee de chatGPT', 'Confirmation de votre rendez-vous chez le médecin.'),
    ('donnee de chatGPT', 'Votre inscription à un événement a été validée.'),
    ('donnee de chatGPT', 'Mise à jour des conditions d''utilisation de notre service.'),
    ('donnee de chatGPT', 'Recevez nos meilleurs vœux pour votre anniversaire !'),
    ('donnee de chatGPT', 'Nouvelles offres et promotions exclusives pour nos membres.'),
    ('donnee de chatGPT', 'Félicitations pour avoir atteint un nouveau niveau sur notre plateforme.'),
    ('donnee de chatGPT', 'Résumé de votre compte bancaire pour le mois dernier.'),
    ('donnee de chatGPT', 'Votre réservation de table pour ce soir est confirmée.'),
    ('donnee de chatGPT', 'Avis de renouvellement de votre adhésion à notre club.'),
    ('donnee de chatGPT', 'Merci d''avoir participé à notre concours - voici les résultats.'),
    ('donnee de chatGPT', 'Confirmation de votre abonnement à notre chaîne YouTube.'),
    ('donnee de chatGPT', 'Nouvelle mise à jour disponible pour votre logiciel.'),
    ('donnee de chatGPT', 'Invitation à un webinaire exclusif sur un sujet pertinent.'),
    ('donnee de chatGPT', 'Dernières nouvelles et mises à jour de notre entreprise.'),
    ('donnee de chatGPT', 'Avis de réinitialisation de votre mot de passe.'),
    ('donnee de chatGPT', 'Mise à jour de votre statut de candidature à un poste.'),
    ('donnee de chatGPT', 'Confirmation de votre réservation d''hôtel pour vos prochaines vacances.'),
    ('donnee de chatGPT', 'Découvrez nos nouvelles fonctionnalités passionnantes !'),
    ('donnee de chatGPT', 'Votre ami vous a envoyé une carte virtuelle pour vous saluer.'),
    ('donnee de chatGPT', 'Recevez un bon de réduction de 20% sur votre prochain achat.'),
    ('donnee de chatGPT', 'Votre compte a été crédité d''un remboursement pour un produit en rupture de stock.'),
    ('donnee de chatGPT', 'Invitation à participer à notre programme de fidélité.'),
    ('donnee de chatGPT', 'Avis de livraison réussie pour votre colis.'),
    ('donnee de chatGPT', 'Votre compte a été mis à jour avec succès.'),
    ('donnee de chatGPT', 'Notification de mise à jour de votre application mobile.'),
    ('donnee de chatGPT', 'Recevez un livre électronique gratuit en vous inscrivant à notre newsletter.'),
    ('donnee de chatGPT', 'Avis de prolongation de la période d''essai de notre service.'),
    ('donnee de chatGPT', 'Félicitations pour avoir été choisi comme gagnant de notre tirage au sort.'),
    ('donnee de chatGPT', 'Votre abonnement à notre plateforme arrive à expiration.'),
    ('donnee de chatGPT', 'Confirmation de votre adhésion à une conférence.'),
    ('donnee de chatGPT', 'Invitation à un événement spécial dans notre magasin.'),
    ('donnee de chatGPT', 'Votre compte est maintenant connecté à notre nouveau programme de récompenses.'),
    ('donnee de chatGPT', 'Recevez une consultation gratuite avec notre expert en la matière.'),
    ('donnee de chatGPT', 'Nouvelle mise à jour de notre politique de retour pour faciliter vos achats.'),
    ('donnee de chatGPT', 'Confirmation de votre réservation de siège pour un spectacle.'),
    ('donnee de chatGPT', 'Votre demande de réinitialisation de mot de passe a été reçue.'),
    ('donnee de chatGPT', 'Recevez des nouvelles de notre équipe sportive préférée chaque semaine.'),
    ('donnee de chatGPT', 'Avis de remboursement suite à un achat en double.'),
    ('donnee de chatGPT', 'Invitation à rejoindre notre programme bêta pour tester de nouvelles fonctionnalités.'),
    ('donnee de chatGPT', 'Confirmation de votre inscription à un cours en ligne.'),
    ('donnee de chatGPT', 'Recevez une garantie étendue gratuite pour votre produit acheté.');

-- Insérer les étiquettes "yes" pour les spams et "no" pour les non-spams dans la table "isspam"
INSERT INTO isSpam (idMail, valeur) 
VALUES
    (1, 'yes'),  -- spam
    (2, 'yes'),  -- spam
    (3, 'yes'),  -- spam
    (4, 'yes'),  -- spam
    (5, 'yes'),  -- spam
    (6, 'yes'),  -- spam
    (7, 'yes'),  -- spam
    (8, 'yes'),  -- spam
    (9, 'yes'),  -- spam
    (10, 'yes'), -- spam
    (11, 'yes'), -- spam
    (12, 'yes'), -- spam
    (13, 'yes'), -- spam
    (14, 'yes'), -- spam
    (15, 'yes'), -- spam
    (16, 'yes'), -- spam
    (17, 'yes'), -- spam
    (18, 'yes'), -- spam
    (19, 'yes'), -- spam
    (20, 'yes'), -- spam
    (21, 'yes'), -- spam
    (22, 'yes'), -- spam
    (23, 'yes'), -- spam
    (24, 'yes'), -- spam
    (25, 'yes'), -- spam
    (26, 'yes'), -- spam
    (27, 'yes'), -- spam
    (28, 'yes'), -- spam
    (29, 'yes'), -- spam
    (30, 'yes'), -- spam
    (31, 'yes'), -- spam
    (32, 'yes'), -- spam
    (33, 'yes'), -- spam
    (34, 'yes'), -- spam
    (35, 'yes'), -- spam
    (36, 'yes'), -- spam
    (37, 'yes'), -- spam
    (38, 'yes'), -- spam
    (39, 'yes'), -- spam
    (40, 'yes'), -- spam
    (41, 'yes'), -- spam
    (42, 'yes'), -- spam
    (43, 'yes'), -- spam
    (44, 'yes'), -- spam
    (45, 'yes'), -- spam
    (46, 'yes'), -- spam
    (47, 'yes'), -- spam
    (48, 'yes'), -- spam
    (49, 'yes'), -- spam
    (50, 'yes'), -- spam
    (51, 'no'),  -- non-spam
    (52, 'no'),  -- non-spam
    (53, 'no'),  -- non-spam
    (54, 'no'),  -- non-spam
    (55, 'no'),  -- non-spam
    (56, 'no'),  -- non-spam
    (57, 'no'),  -- non-spam
    (58, 'no'),  -- non-spam
    (59, 'no'),  -- non-spam
    (60, 'no'),  -- non-spam
    (61, 'no'),  -- non-spam
    (62, 'no'),  -- non-spam
    (63, 'no'),  -- non-spam
    (64, 'no'),  -- non-spam
    (65, 'no'),  -- non-spam
    (66, 'no'),  -- non-spam
    (67, 'no'),  -- non-spam
    (68, 'no'),  -- non-spam
    (69, 'no'),  -- non-spam
    (70, 'no'),  -- non-spam
    (71, 'no'),  -- non-spam
    (72, 'no'),  -- non-spam
    (73, 'no'),  -- non-spam
    (74, 'no'),  -- non-spam
    (75, 'no'),  -- non-spam
    (76, 'no'),  -- non-spam
    (77, 'no'),  -- non-spam
    (78, 'no'),  -- non-spam
    (79, 'no'),  -- non-spam
    (80, 'no'),  -- non-spam
    (81, 'no'),  -- non-spam
    (82, 'no'),  -- non-spam
    (83, 'no'),  -- non-spam
    (84, 'no'),  -- non-spam
    (85, 'no'),  -- non-spam
    (86, 'no'),  -- non-spam
    (87, 'no'),  -- non-spam
    (88, 'no'),  -- non-spam
    (89, 'no'),  -- non-spam
    (90, 'no'),  -- non-spam
    (91, 'no'),  -- non-spam
    (92, 'no'),  -- non-spam
    (93, 'no'),  -- non-spam
    (94, 'no'),  -- non-spam
    (95, 'no'),  -- non-spam
    (96, 'no'),  -- non-spam
    (97, 'no'),  -- non-spam
    (98, 'no'),  -- non-spam
    (99, 'no'),  -- non-spam
    (100, 'no'); -- non-spam



-- insert into envoimessage values
--     (default,1,2,2,now()),
--     (default,1,2,4,now()),
--     (default,2,3,8,now()),
--     (default,1,3,9,now()),
--     (default,3,1,5,now()),
--     (default,2,1,3,now()),
--     (default,2,1,6,now()),
--     (default,3,2,1,now()),
--     (default,3,1,7,now());

-- insert into isSpam values
--     (default,1,'no'),
--     (default,2,'no'),
--     (default,3,'no'),
--     (default,4,'yes'),
--     (default,5,'no'),
--     (default,6,'no'),
--     (default,7,'yes'),
--     (default,8,'no'),
--     (default,9,'no');

-- insert into isSpam values(default,2,'yes');
-- insert into isSpam values(default,5,'yes');
-- insert into isSpam values(default,5,'no');

-- insert into isRead values
--     (default,1,0),
--     (default,2,1),
--     (default,3,0),
--     (default,4,1),
--     (default,5,1),
--     (default,6,1),
--     (default,7,1),
--     (default,8,0),
--     (default,9,1);

-- insert into isRead values(default,8,1);

create view v_isspam as (
select i.* from isspam as i
join 
(select idmail,max(idisspam) as idisspam from isSpam group by idmail) as vu
on i.idisspam = vu.idisspam and i.idmail = vu.idmail
);

create view v_isread as (
select i.* from isread as i
join 
(select idmail,max(idisread) as idisread from isread group by idmail) as vu
on i.idisread = vu.idisread and i.idmail = vu.idmail
);


create view v_mail as (
select m.*,s.valeur as spam, r.valeur as read from mail m
join v_isspam as s
on s.idmail = m.idmail
join v_isread as r
on r.idmail = m.idmail
);

create or replace view v_envoimessage as (
select e.*,desteur.comptedestinateur,destaire.comptedestinataire,desteur.nomdestinateur,destaire.nomdestinataire from envoimessage e
join
(select e.idEnvoiMessage,u.compte as comptedestinateur,u.nom as nomdestinateur from envoimessage e
join utilisateur u
on u.idUtilisateur = e.idDestinateur) desteur
on desteur.idEnvoiMessage = e.idEnvoiMessage
join
(select e.idEnvoiMessage,u.compte as comptedestinataire,u.nom as nomdestinataire from envoimessage e
join utilisateur u
on u.idUtilisateur = e.idDestinataire) destaire
on destaire.idEnvoiMessage = e.idEnvoiMessage
);


create or replace view mailfinal as (
select en.*,m.objet,m.texte,m.spam,m.read from v_envoimessage en
join v_mail m
on m.idmail = en.idmail
);

-- select texte,valeur from mail join v_isspam on mail.idmail = v_isspam.idmail;