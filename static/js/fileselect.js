$(document).ready(function () {
   $('.list-group-item').click(function () {
       $(this).toggleClass('active');
       $('.del').removeClass('disabled');
   });
   $('input').addClass('form-control');
});