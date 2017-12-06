/**
 * Created by Admin on 11/28/2017.
 */
$(function(){
    $('#search').keyup(function(){

    $.ajax({
        type: "POST",
        url: "products/search/",
        data: {
            'search_text' : $('#search').val(),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success : searchSuccess,
        datatype : 'html'

        });
    });

});

function searchSuccess(data){
    $('#search-results').html(data);
}


 $(function() {
	$( ".opensearch" ).on( 'click', tapHandler );

	function tapHandler( event ) {
	  $('.search_field').slideToggle();
	  setTimeout(function(){
		 $('#search').focus();
		},0);
	}

});
