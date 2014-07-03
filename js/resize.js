// JavaScript Document


//<shared file>
var makeSizeContentHandler = function(imageSelector, divSelector){		
	return function() {
		if ($(window).width() >= 753) {
		   // download complicated script
		   // swap in full-source images for low-source ones
		   
		 
	  
	   var newHeight = $(imageSelector).height();
		$(divSelector).css("height", newHeight);
		}
		else{
			
			$(divSelector).css("height", '100%');
		}
	}
}
//</shared file>




   

//</page specific script>
	
	
