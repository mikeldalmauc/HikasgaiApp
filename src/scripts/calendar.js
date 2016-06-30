var $ = require('jquery'); //Importo la libreria jquery

var descargarCalendario = function() {
  var loadingDiv = $(".loading")[0]; //Cacheo el el bloque donde ira el loading

  var textFile = null,
    makeTextFile = function(text) {
      var data = new Blob([text], {
        type: 'text/plain'
      });


      if (textFile !== null) {
        window.URL.revokeObjectURL(textFile);
      }

      textFile = window.URL.createObjectURL(data);

      return textFile;
    }; //Toda esta funcion es la que se encarga de crear el fichero

  // Se leen los campos de la pagina
  var create = document.getElementById('create'),
    textbox = document.getElementById('textbox'); //Sigo cacheando objetos


  create.addEventListener('click', function() {
    // Se hace visible el logo de cargar
    $(loadingDiv).removeClass("hidden");
    //
    var link = document.getElementById('downloadlink');
    var url = "/calendario2";
    //TODO: Esto es lo que teneis que hacer:
    /* 1. La variable data tiene que ser un objeto JSON, con un atributo
    * llamado "asignaturas" que tendra un array con objetos donde ira la informacion de la asignaturas
    * Este es el ejemplo de data
    * data = {
    *   "asignaturas": [
    *     {
    *       "campus": "GI",
    *       "codigoGrado": "GINFOR20",
    *       "codigoAsig": "25972",
    *       "idioma": "es",
    *       "grupo": "01"
    *     },
    *     {..}
    *  ]
    * }
    *
    * Os he dejado ya una variable data creada a mano pero teneis que gestionarlo para recibir
    * los datos desde el template, lo haria yo pero no me pagan lo suficiente.
    *
    * Puede que tengais algun problema porque no os pilla el codigo, teneis que ejecutar antes
    * el comando: "npm install" o "npm install i -D jquery", el segundo funciona seguro, porque he metido jquery en los modulos de node.
    *
    */
    var data = {
      "cursoAcademico":"2016/2017",
      "inicioCuatrimestreUno":"2016/09/05 MON",
      "inicioCuatrimestreDos":"2017/01/24 TUE",
      "finCuatrimestreUno":"2016/12/23 FRI",
      "finCuatrimestreDos":"2017/05/23 WED"
    }

    var success = function(data) { //Si todo tira bien se ejecuta esto
      link.href = makeTextFile(data);
      link.style.display = 'block';
      $(loadingDiv).addClass("hidden", 500);
    };

    var error = function(request, status, error){ //Si hay algun error pues esto
      console.log(request);
      console.log(request.responseText);
      $(loadingDiv).addClass("hidden", 500);
      alert("Error, mira la consola para ver los logs");
    };

    $.ajax({
      type: "POST",
      url: url,
      data: JSON.stringify(data),
      success: success,
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      error: error
    });

  }, false);
}

exports.descargarCalendario = descargarCalendario;
