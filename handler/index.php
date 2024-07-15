<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insertion d'Utilisateur</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h2>Formulaire d'Insertion d'Utilisateur</h2>
        <form action="auth.php" method = "POST" >
            <label for="nom">Nom :</label>
            <input type="text" id="nom" name="nom" ]required>
            
            <label for="email">Email :</label>
            <input type="email" id="email" name="email" required>
            
            <label for="telephone">Téléphone :</label>
            <input type="tel" id="telephone" name="telephone" >
            
            <input type="submit" value = "Valider" >
        </form>
    </div>
</body>
</html>