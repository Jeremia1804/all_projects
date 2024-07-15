(function($) {
    /* "use strict" */

	
	/* function draw() {
		
	} */

 var dzSparkLine = function(){
	let draw = Chart.controllers.line.__super__.draw; //draw shadow
	
	var screenWidth = $(window).width();

	var updateYearDropdown = function() {
        // Générer une liste d'années de 2019 à l'année actuelle
        var currentYear = new Date().getFullYear();
        var years = [];
        for (var year = 2019; year <= currentYear; year++) {
            years.push(year);
        }

        // Mettre à jour le dropdown avec les années générées
        var dropdownMenu = $('.dropdown-menu');
        dropdownMenu.empty(); // Vide le contenu acdonnee['date_debut']tuel du dropdown
        years.forEach(function(year) {
            var menuItem = $('<a class="dropdown-item" href="javascript:void(0);">' + year + '</a>');
            menuItem.data('year', year); // Stocke l'année dans les données de l'élément
            dropdownMenu.append(menuItem); // Ajoute l'élément au dropdown
        });
    };

	$('.dropdown-menu').on('click', '.dropdown-item', function() {
        var year = $(this).data('year'); // Récupère l'année stockée dans les données de l'élément
        $('.dropdown-toggle').text(year); // Affiche l'année sélectionnée dans le dropdown
        getYearlyData(year); // Récupère les données correspondantes à l'année sélectionnée
    });

	var getYearlyData = function(year) {
        // Faire une requête AJAX pour obtenir les données correspondant à l'année
        $.ajax({
            url: '/getdatahisto',
            type: 'POST',
			dataType: 'json',
            data: { year: year},
            success: function(response) {
                barChart1(response.libelle,response.valeur); 
            },
            error: function(error) {
                console.error('Erreur lors de la récupération des données : ' + error);
            }
        });
    };
	
	var barChart1 = function(libelle, valeur) {
		if (jQuery('#barChart_1').length > 0) {
			const barChart_1 = document.getElementById("barChart_1").getContext('2d');
	
			// Effacer le graphique existant
			if (window.barChartInstance !== undefined)
				window.barChartInstance.destroy();
	
			// Créer un nouveau graphique avec les nouvelles données
			window.barChartInstance = new Chart(barChart_1, {
				type: 'bar',
				data: {
					defaultFontFamily: 'Poppins',
					labels: libelle,
					datasets: [{
						label: "Montant: ",
						data: valeur,
						borderColor: 'rgba(19, 180, 151, 1)',
						borderWidth: "0",
						backgroundColor: 'rgba(19, 180, 151, 1)'
					}]
				},
				options: {
					legend: false,
					scales: {
						yAxes: [{
							ticks: {
								beginAtZero: true
							}
						}],
						xAxes: [{
							barPercentage: 0.5
						}]
					}
				}
			});
		}
	};
	

	/* Function ============ */
		return {
			init: function() {
				updateYearDropdown();
			},
			
			
			load:function(){
				updateYearDropdown();
				// barChart1(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],[65, 59, 80, 81, 56, 55, 40]);
			},
			
			resize:function(){
				updateYearDropdown();
				// barChart1(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],[65, 59, 80, 81, 56, 55, 40]); 
			}
		}
	
	}();

	jQuery(document).ready(function(){
	});
		
	jQuery(window).on('load',function(){
		dzSparkLine.load();
	});

	jQuery(window).on('resize',function(){
		dzSparkLine.resize();
		
	});     

})(jQuery);