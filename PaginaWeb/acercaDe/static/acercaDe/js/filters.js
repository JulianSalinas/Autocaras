'use strict';

/* Archivo para implementar filtros */

/*Ejemplo o plantilla*/
angular.module('angularFlaskFilters', []).filter('uppercase', function() {
	return function(input) {
		return input.toUpperCase();
	}
});