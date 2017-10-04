'use strict';

/* Controladores de cada vista */

function ControladorInicio($scope) {

}

function ControladorAcercaDe($scope, $log, $http) {
    $scope.getMiembros = function () {

        $log.log("Obteniendo los miembros");

        // get the URL from the input
        var userInput = $scope.url;

        // fire the API request
        $http.post('/integrantes', {}).
        success(function (results) {
            $scope.miembros = results.Integrantes;
            $log.log(results);
        }).
        error(function (error) {
            $log.log(error);
        });

    };
    $scope.getMiembros();

}

function ControladorReconocimiento($scope, $log, $http) {

    $scope.test_clasificar = function () {

        $log.log("Test de clasificación");
        
        var filePath = $('#InputFile').val();
        $log.log(filePath);

        // fire the API request
        $http.post('/test_clasificar/' + "..$datos$otro$26_7.pgm", {}).
        success(function (results) {
            $scope.resultadoTest = results;
            $log.log(results);
        }).
        error(function (error) {
            $log.log(error);
        });

    };
    $scope.test_clasificar();

    /*var postsQuery = Post.get({}, function (posts) {
        $scope.posts = posts.objects;
    });*/
}

function ControladorEntrenamiento($scope) {
    /*var postQuery = Post.get({
        postId: $routeParams.postId
    }, function (post) {
        $scope.post = post;
    });*/
}
