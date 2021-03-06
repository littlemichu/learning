angular.module("sportsStore")
.controller("cartSummaryCtrl", function ($scope, cart) {

	$scope.cartData = cart.getProducts();

	$scope.total = function () {
		total = 0;
		for (var i = 0; i < $scope.cartData.length; i++) {
			total += $scope.cartData[i].count * $scope.cartData[i].price;
		}
		return total;
	}

	$scope.remove = function (id) {
		cart.removeProduct(id);
	}
});
