// JavaScript Document
(function ($) {
//@credit: http://stackoverflow.com/a/12269923
    $.fn.getWidthInPercent = function () {
        var width = parseFloat($(this).css('width'))/parseFloat($(this).parent().css('width'));
        return 100*width;
    };

})(jQuery);

//<shared file>
var makeSizeContentHandler = function(imageSelector, divSelector){		
	return function() {
		var width = $(window).width();
		if ( width >= 753) {
		   // download complicated script
		   // swap in full-source images for low-source ones
		   
		 
	  var imagePercentage = $(imageSelector).getWidthInPercent();
	  var containerWidth = $('#container').width();
	   var newHeight = containerWidth * (imagePercentage / 100.0);
		$(divSelector).css("height", newHeight);
		}
		else{
			
			$(divSelector).css("height", '100%');
		}
	}
}
//</shared file>




   

//</page specific script>
	
	
