'use strict';

/**
 * @ngdoc overview
 * @name frontendApp
 * @description
 * # frontendApp
 *
 * Main module of the application.
 */
angular
  .module('frontendApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider, $httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $routeProvider
      .when('/', {
        templateUrl: 'views/browseartists.html',
        controller: 'BrowseCtrl',
        controllerAs: 'browse'
      })
      .when('/addartist', {
        templateUrl: 'views/addartist.html',
        controller: 'AddArtistCtrl',
        controllerAs: 'addartist'
      })
      .otherwise({
        redirectTo: '/'
      });
  });