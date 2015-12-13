$("#vote").val('34');

// Create a click handler for your increment button
$("#increaseButton").click(function () {
    var newValue = 1 + parseInt($("#vote").val());
    $("#vote").val(newValue);
	this.disabled='true';
	//$("#decreaseButton").disabled='false';
});
// .. and your decrement button
$("#decreaseButton").click(function () {
    var newValue = parseInt($("#vote").val()) - 1;
    $("#vote").val(newValue);
	this.disabled='true';
	//$("#increaseButton").disabled='false';
});