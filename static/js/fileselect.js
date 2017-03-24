$(document).ready(function () {
   $('.list-group-item').click(function () {
       $(this).toggleClass('active');
       $('.del').removeClass('disabled');
   });
   $('input').addClass('form-control');

   // skyward
   	$('.querC').click(function(){
		var start = $('.start').val();
		var limit = $('.limit').val();
    if ( limit == " ") {
      limit = start + 50;
    }
		for (i = start; i < limit; i++) {
			$('.spawn').append('<div onclick="alert(' + i + ')" ><img style="float: left; cursor: pointer;" width="100" height="150" class="thumbnail" src="https://www2.wrdc.wa-k12.net/pictures/bainbrs/0' + i + '.JPG" /></div>');
		}
	});
	$('.errorlist').hide();
	$('label').hide();
	$('#id_title').attr('placeholder', 'Note Title');
	$('#id_content').attr('placeholder', 'Note Content');
	$('#id_content').attr('cols', '67');
	$('#id_content').addClass('form-control');

});
