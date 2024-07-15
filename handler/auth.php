<?php
   include('MysqlSessionHandler.php');
    $sessionHandler = new MysqlSessionHandler();
    session_set_save_handler($sessionHandler, true);
    session_start();
    $_SESSION['nom'] = $_POST['nom'];
    $_SESSION['email'] = $_POST['email'];
    $_SESSION['telephone'] = $_POST['telephone'];
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page d'accueil</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            text-align: center;
        }

        header {
            background-color: #007BFF;
            color: #fff;
            padding: 20px 0;
        }

        h1 {
            font-size: 28px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        p {
            font-size: 18px;
            margin: 10px 0;
        }

        a {
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>BIENVENUE</h1>
    </header>

    <div class="container">
        <p>Nom: <?php echo $_SESSION['nom']; ?></p>
        <p>Email: <?php echo $_SESSION['email']; ?></p>
        <p>Téléphone: <?php echo $_SESSION['telephone']; ?></p>

        <a href="exit.php">Déconnexion</a>
    </div>
</body>
</html>
