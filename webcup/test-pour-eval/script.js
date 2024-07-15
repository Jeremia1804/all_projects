// Fonction pour cocher ou décocher toutes les cases à cocher des colonnes
function checkAllColumns(checkbox) {
    var checkboxes = document.getElementsByName('colonne');
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = checkbox.checked;
    }
    updateTable();
}

// Fonction pour mettre à jour l'affichage de la table en fonction des colonnes sélectionnées
function updateTable() {
    var checkboxes = document.getElementsByName('colonne');
    var table = document.getElementById('maTable');

    // Parcours des colonnes de la table
    for (var i = 0; i < table.rows.length; i++) {
        var row = table.rows[i];
        for (var j = 0; j < row.cells.length; j++) {
            var cell = row.cells[j];
            // Affiche ou masque la cellule en fonction de l'état de la case à cocher correspondante
            if (checkboxes[j].checked) {
                cell.style.display = '';
            } else {
                cell.style.display = 'none';
            }
        }
    }
}

// Appel de la fonction updateTable() lors du chargement de la page
window.onload = updateTable;
