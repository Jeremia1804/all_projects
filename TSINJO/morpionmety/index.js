/* Globals */
var NUM_ROWS = 3,
    NUM_COLS = 3,
    NUM_SQUARES = NUM_ROWS * NUM_COLS,
    GAMEBOARD = new Array(NUM_SQUARES),
    WIN_COMBOS = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],
                  [1,4,7],[2,5,8],[0,4,8],[2,4,6]],
    MAX_DEPTH,
    AI_MOVE,
    PLAYER_CLASS = 'cross',
    COMPUTER_CLASS = 'nought',
    poidsPositions = [
      3,2,3,2,4,2,3,2,3
    ],
    RUNNING = false;
    niveau = 'moyenne';

$(document).ready(function() {
  /* Commence une nouvelle partie */
  new_game();

  /* Le symbole de paramètres a été cliqué, affiche le menu des paramètres */
  $(".board__settings-cog").click(function() {
    if ($(".board__settings").css('visibility') == 'hidden') {
      $(".board__settings").css('visibility', 'visible');
    } else {
      $(".board__settings").css('visibility', 'hidden');
    }
  });

  /* La classe du joueur a été modifiée à partir du menu des paramètres */
  $(".board__settings__choice-cross").click(function() {
    PLAYER_CLASS = 'cross';
    COMPUTER_CLASS = 'nought';
    $(".board__settings").css('visibility', 'hidden');
    console.log('classe définie sur cross');
  });

  $(".board__settings__choice-nought").click(function() {
    PLAYER_CLASS = 'nought';
    COMPUTER_CLASS = 'cross';
    $(".board__settings").css('visibility', 'hidden');
  });

  /* Difficulté sélectionnée */
  $("div[class*=board__difficulty__button]").click(function() {
    var difficulty = $(this).attr("id");

    if (difficulty === 'easy') {
      poidsPositions = [
        3,2,3,
        2,4,2,
        3,2,3
      ],
      MAX_DEPTH = 1; 
      niveau = 'facile';
    }
    else if (difficulty === 'medium') MAX_DEPTH = 3;
    else MAX_DEPTH = 10;

    $(".board__difficulty").removeClass('slideDown').addClass('slideUp');
    new_game();
    if(COMPUTER_CLASS == 'cross') IACommence();
  });

  /* Traite un clic sur une case */
  $(".board__slot").click(function() {
    if (RUNNING) {
      var pos = Number($(this).attr("id"));

      /* Si la case est vide, traite le clic */
      if (GAMEBOARD[pos] == "") {
        $(this).addClass(PLAYER_CLASS + ' player-color');
        GAMEBOARD[pos] = "X";

        if (full(GAMEBOARD)) {
          RUNNING = false;
          $(".board__header-difficulty").html("C'est une égalité !");
          $(".board__difficulty").removeClass('slideUp').addClass('slideDown');
        } else if (wins(GAMEBOARD, "X")) {
          RUNNING = false;
          $(".board__header-difficulty").html("Tu as gagné !");
          $(".board__difficulty").removeClass('slideUp').addClass('slideDown');
        } else {
          setTimeout(() =>{
          if(MAX_DEPTH == 10){
            minimax(GAMEBOARD, "O", 0);
          }else{
            // let noeud = new Noeud(null,GAMEBOARD);
            parcour(niveau);
            // tourIA(niveau);

          }
          GAMEBOARD[AI_MOVE] = "O";
          $(".board__slot[id=" + AI_MOVE + "]").addClass(COMPUTER_CLASS + ' computer-color');

          if (wins(GAMEBOARD, "O")) {
            RUNNING = false;
            $(".board__header-difficulty").html("Tu as perdu !");
            $(".board__difficulty").removeClass('slideUp').addClass('slideDown');
          }
          if (full(GAMEBOARD)) {
            RUNNING = false;
            $(".board__header-difficulty").html("C'est une égalité !");
            $(".board__difficulty").removeClass('slideUp').addClass('slideDown');
          }
        },1000);
        }
      }
    }
  });
});

function IACommence(){
  // minimax(GAMEBOARD, "O", 0);
  AI_MOVE = 4;
  GAMEBOARD[AI_MOVE] = "O";
  $(".board__slot[id=" + AI_MOVE + "]").addClass(COMPUTER_CLASS + ' computer-color');
}

/* Démarre une nouvelle partie */
function new_game() {
  /* Efface la table */
  $(".board__slot").each(function() {
    $(this).removeClass(PLAYER_CLASS + ' player-color computer-color ' + COMPUTER_CLASS);
  });

  /* Efface le GAMEBOARD de jeu */
  for (var i = 0; i < NUM_SQUARES; i++) {
    GAMEBOARD[i] = "";
  }

  RUNNING = true;
  
}

/* Pour un état donné du GAMEBOARD, renvoie tous les coups disponibles */
function get_available_moves(state) {
  var all_moves = Array.apply(null, {length: NUM_SQUARES}).map(Number.call, Number);
  return all_moves.filter(function(i) { return state[i] == ""; });
}

/* Pour un état donné du GAMEBOARD, renvoie true si le GAMEBOARD est plein */
function full(state) {
  return !get_available_moves(state).length;
}

/* Pour un état donné du GAMEBOARD, renvoie true si le joueur spécifié a gagné */
function wins(state, player) {
  var win;
  for (var i = 0; i < WIN_COMBOS.length; i++) {
    win = true;
    for (var j = 0; j < WIN_COMBOS[i].length; j++) {
      if (state[WIN_COMBOS[i][j]] != player) {
        win = false;
      }
    }
    if (win) {
      return true;
    }
  }
  return false;
}

/* Pour un état donné du GAMEBOARD, renvoie true si le GAMEBOARD est plein ou si un joueur a gagné */
function terminal(state) {
  return full(state) || wins(state, "X") || wins(state, "O");
}

/* Renvoie la valeur d'un état du GAMEBOARD */
function score(state) {
  if (wins(state, "X")) {
    return 10;
  } else if (wins(state, "O")) {
    return -10;
  } else {
    return 0;
  }
}

/* Trouve la décision optimale pour l'IA */
function minimax(state, player, depth) {
  if (depth >= MAX_DEPTH || terminal(state)) {
    return score(state);
  }

  var max_score,
    min_score,
    scores = [],
    moves = [],
    opponent = (player == "X") ? "O" : "X",
    successors = get_available_moves(state);
    
    for (var s in successors) {
      var possible_state = state;
    possible_state[successors[s]] = player;
    scores.push(minimax(possible_state, opponent, depth + 1));
    possible_state[successors[s]] = "";
    moves.push(successors[s]);
  }

  if (player == "X") {
    AI_MOVE = moves[0];
    max_score = scores[0];
    for (var s in scores) {
      if (scores[s] > max_score) {
        max_score = scores[s];
        AI_MOVE = moves[s];
      }
    }
    return max_score;
  } else {
    AI_MOVE = moves[0];
    min_score = scores[0];
    for (var s in scores) {
      if (scores[s] < min_score) {
        min_score = scores[s];
        AI_MOVE = moves[s];
      }
    }
    return min_score;
  }
}

function calculerPoidsCase(position) {
  return poidsPositions[position];
}

function tourIA(tena) {
  // Calculer les poids des positions pour chaque case du GAMEBOARD de jeu
  var poidsCases = [];
  var egalite = [];
  for (var i = 0; i < GAMEBOARD.length; i++) {
    if (GAMEBOARD[i] === "") {  // Vérifier si la case est vide
      poidsCases[i] = calculerPoidsCase(i);
    } else {
      poidsCases[i] = 0;  // La case est déjà occupée, donc le poids est 0
    }
  }

  // Trouver la case avec le poids le plus élevé
  var caseChoisie = 0;
  var poidsMax = poidsCases[0];
  for (var j = 1; j < poidsCases.length; j++) {
    if (poidsCases[j] > poidsMax) {
      poidsMax = poidsCases[j];
      caseChoisie = j;
    }
  }
  var nb = 0;
  for (var j = 0; j < poidsCases.length; j++) {
    if (poidsCases[j] == poidsMax) {
      egalite [nb] = j;
      nb ++;
    }
  }
  // Placer le marqueur de l'IA dans la case choisie
  if(nb==0){
    AI_MOVE = caseChoisie;
  }else{
    let cond = 0;
    for (var j = 0; j < egalite.length; j++) {
      GAMEBOARD[egalite[j]] = "O";
      let etat =  score(GAMEBOARD);
      GAMEBOARD[egalite[j]] = "";
      if(etat == -10){
        AI_MOVE = egalite[j];
        cond = 1;
        break;
      }
    }
    
    if(tena === 'moyenne'){
      if(cond == 0){
        for (var j = 0; j < poidsCases.length; j++) {
          if (GAMEBOARD[j] === "") {  // Vérifier si la case est vide
            GAMEBOARD[j] = "X";
            let etat =  score(GAMEBOARD);
            GAMEBOARD[j] = "";
            if(etat == 10){
            console.log("oui");
            AI_MOVE = j;
            cond = 1;
            break;
          } 
        }
      }
      if(cond == 0){
        AI_MOVE = caseChoisie;
      }
    }
  }else{
    if(cond == 0) AI_MOVE = caseChoisie;
  }
  }

}

function parcours(state, player,noeud) {
  if (terminal(state)) {
    let sco = score(state);
    if(sco == -10){
      let toi = noeud;
      while (toi.getNoeud() != null){
        toi = toi.getNoeud();
      }
      return toi;
    }else{
      return null;
    }
  }

    var moves = [],
    opponent = (player == "X") ? "O" : "X",
    successors = get_available_moves(state);

  for (var s in successors) {
    var possible_state = state;

    possible_state[successors[s]] = player;
    let no = new Noeud(possible_state,noeud,successors[s]);
    let me = parcours(possible_state, opponent,no);
    if(me != null){
      console.log(me);
      return me;
    }
    possible_state[successors[s]] = "";
    moves.push(successors[s]);
  }
}


















































































function parcour(tena) {
  // Calculer les poids des positions pour chaque case du GAMEBOARD de jeu
  var poidsCases = [];
  var egalite = [];
  for (var i = 0; i < GAMEBOARD.length; i++) {
    if (GAMEBOARD[i] === "") {  // Vérifier si la case est vide
      poidsCases[i] = calculerPoidsCase(i);
    } else {
      poidsCases[i] = 0;  // La case est déjà occupée, donc le poids est 0
    }
  }

  // Trouver la case avec le poids le plus élevé
  var caseChoisie = 0;
  var poidsMax = poidsCases[0];
  for (var j = 1; j < poidsCases.length; j++) {
    if (poidsCases[j] > poidsMax) {
      poidsMax = poidsCases[j];
      caseChoisie = j;
    }
  }
  var nb = 0;
  for (var j = 0; j < poidsCases.length; j++) {
    if (poidsCases[j] == poidsMax) {
      egalite [nb] = j;
      nb ++;
    }
  }
  // Placer le marqueur de l'IA dans la case choisie
  if(nb==0){
    AI_MOVE = caseChoisie;
  }else{
    let cond = 0;
    for (var j = 0; j < egalite.length; j++) {
      GAMEBOARD[egalite[j]] = "O";
      let etat =  score(GAMEBOARD);
      GAMEBOARD[egalite[j]] = "";
      if(etat == -10){
        AI_MOVE = egalite[j];
        cond = 1;
        break;
      }
    }
    
    if(tena === 'moyenne'){
      if(cond == 0){
        for (var j = 0; j < poidsCases.length; j++) {
          if (GAMEBOARD[j] === "") {  // Vérifier si la case est vide
            GAMEBOARD[j] = "X";
            let etat =  score(GAMEBOARD);
            GAMEBOARD[j] = "";
            if(etat == 10){
            console.log("oui");
            AI_MOVE = j;
            cond = 1;
            break;
          } 
        }
      }
      if(cond == 0){
        AI_MOVE = caseChoisie;
      }
    }
  }else{
    if(cond == 0) AI_MOVE = caseChoisie;
  }
  }

}