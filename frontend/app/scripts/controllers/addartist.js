'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
  .controller('AddArtistCtrl', function ($scope, $http, $sanitize) {
	$scope.failed = $scope.success = $scope.submitted = false;
	this.addArtist = function()
	{
		$scope.failed = $scope.success = $scope.submitted = false;
		$scope.adding = true;
		$http({method: 'PUT',
				url: 'http://54.194.90.142:8000/api/artists/',
				data: $sanitize($scope.artistName)}
				).then(function success(response){
					$scope.submitted = true;
					$scope.success = true;
					$scope.adding = false;
				}, function error(response) {
					$scope.submitted = true;
					$scope.failed = true;
					$scope.adding = false;
				});
	}
  });
