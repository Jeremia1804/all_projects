<?php
   include('MysqlSessionHandler.php');
    $sessionHandler = new MysqlSessionHandler();
    session_set_save_handler($sessionHandler, true);
    session_start(); 
    session_destroy();
    header('location: index.php');
?>