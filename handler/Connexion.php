<?php
 function connect(){
     $host = "localhost"; // Adresse du serveur MySQL
     $dbname = "handler"; // Nom de la base de données
     $user = "postgres"; // Nom d'utilisateur MySQL
     $password = "root"; // Mot de passe MySQL
 
     try {
        $db = new PDO("pgsql:host=$host;dbname=$dbname", $user, $password);
        return $db;
        } catch (PDOException $e) {
        echo "Erreur de connexion : " . $e->getMessage();
        return null; 
      }
}
// connect();
?>