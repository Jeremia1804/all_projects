<?php
include('./Connexion.php');

class MysqlSessionHandler implements SessionHandlerInterface {
    private $db;

    public function __construct() {
        $this->db = connect();
    }

    public function read($id) {
        $sql = "SELECT data FROM sessions WHERE id = :id";
        $stmt = $this->db->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        return ($result) ? $result['data'] : '';
    }

    public function write($id, $data) {
        $sql = "INSERT INTO sessions (id, data, timestamp) VALUES (:id, :data, :timestamp)";
        $stmt = $this->db->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->bindParam(':data', $data);
        $stmt->bindValue(':timestamp', time());
        // echo($tmt);
        $stmt->execute();
        return true;
    }

    public function destroy($id) {
        $sql = "DELETE FROM sessions WHERE id = :id";
        $stmt = $this->db->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return true;
    }
    

    public function gc($maxlifetime) {
        $sql = "DELETE FROM sessions WHERE timestamp < :timestamp";
        $stmt = $this->db->prepare($sql);
        $stmt->bindParam(':timestamp', time() - $maxlifetime);
        $stmt->execute();

        return true;
    }

    public function close(): bool {
        return true; 
    }

    public function open($path, $name): bool {
        return true; 
    }

    public function create_sid(): string {
        $newSessionId = uniqid();
        return $newSessionId;
    }
    

}


?>
