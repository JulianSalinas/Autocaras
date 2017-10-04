'use strict';

angular.module('AngularFlask', ['angularFlaskServices'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/inicio.html',
			controller: ControladorInicio
		})
		.when('/acercaDe', {
			templateUrl: 'static/partials/about.html',
			controller: ControladorAcercaDe
		})
		.when('/reconocimiento', {
			templateUrl: 'static/partials/reconocimiento.html',
			controller: ControladorReconocimiento
		})
		.when('/entrenamiento', {
			templateUrl: '/static/partials/entrenamiento.html',
			controller: ControladorEntrenamiento
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
	}])
;