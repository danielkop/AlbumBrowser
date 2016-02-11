'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontendApp
 */
 
angular.module('frontendApp')
  .controller('BrowseCtrl', function ($scope, $http) {
	$scope.reverse = false;
    $scope.artists = [];
	$scope.artistError = false;
	$scope.albumError = false;
	$scope.albumLoading = false;
	this.setOrder = function(orderBy)
	{
		if($scope.order === orderBy)
		{
			$scope.reverse = !$scope.reverse;
		}
		else
		{
			$scope.order = orderBy;
			$scope.reverse = false;
		}
	};
	this.getArrow = function(orderBy)
	{
		if($scope.order !== orderBy)
		{
			return '';
		}
		return $scope.reverse ? '▲' : '▼';
	};
	this.showAlbums = function(id)
	{
		$scope.currentArtistId = id;
		$scope.albums = [];
		$scope.albumLoading = true;
		$scope.order = 'name';
		$scope.reverse = false;
		$scope.searchstring = '';
		$http.get('http://54.194.90.142:8000/api/artists/' + id + '/albums/').then(function success(response)
		{
			$scope.albums = response.data[0].albums;
			$scope.albumLoading = false;
			$scope.albumError = false;
		}, 
		function error(/*response*/)
		{
			$scope.albumLoading = false;
			$scope.albumError = true;
		});
	};
	this.getArtists = function()
	{
		$scope.artistLoading = true;
		$http.get('http://54.194.90.142:8000/api/artists/').then(
		function success(response)
		{
			$scope.artistLoading = false;
			$scope.artistError = false;
			$scope.artists = response.data.artists;
		}, 
		function error(/*response*/)
		{
			$scope.artistLoading = false;
			$scope.artistError = true;
		});
	};
	this.getArtists();
  });
