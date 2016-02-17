angular.module("cart", [])
.factory("cart", function () {

	var cartData = [];

	return {
		addProduct: function (id, name, price) {
			var alreadyAdded = false;

			for (var i=0; i < cartData.length; i++) {
				if (cartData[i].id == id) { // Product already added
					cartData[i].count++;
					alreadyAdded = true;
					break;
				}
			}

			if (!alreadyAdded) {
				cartData.push({
					count: 1, id: id, price: price, name: name
				});
			}
		},

		removeProduct: function (id) {
			for (var i=0; i < cartData.length; i++) {
				if (cartData[i].id == id) {
					cartData.splice(i, 1);
				}
			}
		},

		getProducts: function() {
			return cartData;
		}
	};
})
.directive("cartSummary", function (cart) {
	return {
		restrict: "E",
		templateUrl: "components/cart/cartSummary.html",
		controller: function ($scope) {

			var cartData = cart.getProducts();

			$scope.total = function () {
				total = 0;
				for (var i=0; i < cartData.length; i++) {
					total += cartData[i].count * cartData[i].price;
				}
				return total;
			}

			$scope.itemCount = function () {
				count = 0;
				for (var i=0; i < cartData.length; i++) {
					count += cartData[i].count;
				}
				return count;
			}
		}
	};
});
