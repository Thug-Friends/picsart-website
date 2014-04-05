
$(document).ready(function($){
    var url = window.location.pathname;
    $('.nav a[href="'+url+'"]').parent().addClass('active');
});